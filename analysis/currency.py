import asyncio
import io
import math
from decimal import Decimal

import aiohttp
import pandas as pd
import requests

rus_cb_url = "https://www.cbr.ru/scripts/XML_daily.asp"


def cb_xml_parser(text: str, curr: str) -> float:
    xml_text = io.StringIO(text)
    xml = pd.read_xml(xml_text, parser="etree",
                      converters={"Nominal": Decimal,
                                  "Value": lambda fstr: Decimal(fstr.replace(",", "."))})
    xml = xml[xml["CharCode"] == curr]
    if xml.empty:
        return math.nan
    xml = xml.iloc[0]
    return float(xml["Value"] / xml["Nominal"])


def sync_get_currency(df: pd.DataFrame, cb_url: str = rus_cb_url):
    def inner(job: pd.Series) -> float:
        if job["salary_currency"] == "RUR" or isinstance(job["salary_currency"], float):
            return 1.0
        date: pd.Timestamp = job["published_at"].normalize() - pd.offsets.MonthBegin(1)
        req = requests.get(f"{cb_url}", {"date_req": date.strftime("%d/%m/%Y")})
        return cb_xml_parser(req.text, job["salary_currency"])

    return df.apply(inner, axis=1)


async def async_get_currency(df: pd.DataFrame, cb_url: str = rus_cb_url) -> pd.Series:
    async def fetch_currency(job: pd.Series) -> float:
        if job["salary_currency"] == "RUR" or isinstance(job["salary_currency"], float):
            return 1.0
        date: pd.Timestamp = job["published_at"].normalize() - pd.offsets.MonthBegin(1)
        async with aiohttp.ClientSession() as session:
            resp = await session.get(cb_url, params={"date_req": date.strftime("%d/%m/%Y")})
            content = await resp.text()
            return cb_xml_parser(content, job["salary_currency"])

    res = await asyncio.gather(*[fetch_currency(job) for index, job in df.iterrows()])
    return pd.Series(res)


def df_get_currency(currency_df: pd.DataFrame):
    def _inner(row: pd.Series) -> float:
        if (isinstance(row["published_at"], float) or
                isinstance(row["salary_currency"], float) or
                row["salary_currency"] == "RUR"):
            return 1.0
        try:
            return currency_df.loc[row["published_at"].strftime("%Y-%m")].loc[row["salary_currency"]]
        except KeyError:
            return math.nan

    return _inner


def fetch_data(url: str):
    def _inner(row: pd.Series) -> pd.DataFrame:
        date: pd.Timestamp = row["date"]
        req = requests.get(f"{url}", {"date_req": date.strftime("%d/%m/%Y")})
        xml_text = io.StringIO(req.text)
        xml = pd.read_xml(xml_text, parser="etree",
                          converters={"Nominal": Decimal,
                                      "Value": lambda fstr: Decimal(fstr.replace(",", "."))})
        xml = xml[["CharCode", "Nominal", "Value"]]
        xml["Value"] = xml["Value"] / xml["Nominal"]
        xml["Value"] = xml["Value"].apply(float)
        res = xml["Value"]
        res.index = xml["CharCode"]
        res["date"] = date.strftime("%Y-%m")
        return res

    return _inner


def load_from_cb(file_name: str):
    columns = ["date", "BYR", "USD", "EUR", "KZT", "UAH", "AZN", "KGS", "UZS", "GEL"]

    df = pd.DataFrame(columns=columns)
    df["date"] = pd.date_range("2003-01-1", "2024-01-01", freq="MS")
    df = df.apply(fetch_data(rus_cb_url), axis=1, result_type="expand")
    df = df[columns]
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    load_from_cb("tmp/currency.csv")
