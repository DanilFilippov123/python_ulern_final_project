import asyncio

import pandas as pd

import currency


def get_jobs_by_name(all_jobs: pd.DataFrame, jobs_names: list[str]) -> pd.DataFrame:
    return all_jobs[all_jobs["name"].str.contains("|".join(jobs_names), case=False)]


def calc_salary(jobs: pd.DataFrame) -> pd.Series:
    # salary_from, salary_to, curr_factor
    return jobs[["salary_from", "salary_to"]].mean(axis=1, skipna=True) * jobs["curr_factor"]


def prepare_data():
    jobs_name = ["Системный администратор", 'system admin', 'сисадмин', 'сис админ', 'системный админ',
                 'cистемный админ', 'администратор систем', 'системний адміністратор']

    csv_file_name = "vacancies.csv"

    df = pd.read_csv(csv_file_name,
                     parse_dates=["published_at"],
                     low_memory=False)
    currency_df = pd.read_csv("tmp/currency.csv", index_col="date")
    df["curr_factor"] = df.apply(currency.df_get_currency(currency_df), axis=1)
    df["salary"] = calc_salary(df)

    df.to_csv("tmp/vacancies_salary_currency.csv", index=False)

    jobs_by_name = get_jobs_by_name(df, jobs_name)

    jobs_by_name.to_csv("tmp/vacancies_our_job.csv", index=False)


if __name__ == '__main__':
    prepare_data()
