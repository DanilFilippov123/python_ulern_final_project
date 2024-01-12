import pandas as pd
from collections import Counter
import numpy as np


def count_skills(x: np.ndarray | list):
   return Counter(np.concatenate(x)).most_common(20) if not isinstance(x, list) else Counter(x).most_common(20)


def skills(csv_file_name: str, by_year_file: str, by_city_file: str):
    df = pd.read_csv(csv_file_name,
                     parse_dates=["published_at"],
                     low_memory=False)
    df = df[~df["key_skills"].isna()]
    df["key_skills"] = df["key_skills"].apply(lambda x: x.split("\n"))
    by_city: pd.DataFrame = df.groupby("area_name")["key_skills"].agg(lambda x: x).apply(count_skills)
    by_city.to_csv(by_city_file)
    df["year"] = df["published_at"].apply(lambda x: x.year)
    by_year: pd.DataFrame = df.groupby("year")["key_skills"].agg(lambda x: x).apply(count_skills)
    by_year.to_csv(by_year_file)


def main():
    skills("tmp/vacancies_our_job.csv", "result/skill_by_year_sys_admin.csv", "result/skill_by_city_sys_admin.csv")


if __name__ == "__main__":
    main()
