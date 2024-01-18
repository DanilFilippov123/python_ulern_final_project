import pandas as pd
from collections import Counter
import numpy as np


def count_skills(x: np.ndarray | list):
    return Counter(np.concatenate(x) if isinstance(x, np.ndarray) else x).most_common(20)


def skills(csv_file_name: str, by_year_file: str, by_year_file_html: str):
    df = pd.read_csv(csv_file_name,
                     parse_dates=["published_at"],
                     low_memory=False)
    df = df[~df["key_skills"].isna()]
    df["key_skills"] = df["key_skills"].apply(lambda x: x.split("\n"))
    df["year"] = df["published_at"].apply(lambda x: x.year)
    by_year: pd.Series = df.groupby("year")["key_skills"].agg(lambda x: x).apply(count_skills)
    by_year.to_csv(by_year_file)
    by_year = by_year.apply(lambda x: ", ".join([f"{skill}: {count}" for (skill, count) in x]))
    by_year.reset_index().to_html(by_year_file_html, index=False)


def main():
    skills("tmp/vacancies_our_job.csv",
           "result/skill_by_year_sys_admin.csv",
           "result/html/skill_by_year_sys_admin.html")

    skills("tmp/vacancies_salary_currency.csv",
           "result/skill_by_year_all_jobs.csv",
           "result/html/skill_by_year_all_jobs.html")


if __name__ == "__main__":
    main()
