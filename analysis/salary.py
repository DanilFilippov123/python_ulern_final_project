import asyncio
from typing import Callable

import pandas as pd


def get_jobs_by_name(all_jobs: pd.DataFrame, jobs_names: list[str]) -> pd.DataFrame:
    return all_jobs[all_jobs["name"].str.contains("|".join(jobs_names), case=False)]


def calc_salary(jobs: pd.DataFrame) -> pd.Series:
    # salary_from, salary_to, curr_factor
    return jobs[["salary_from", "salary_to"]].mean(axis=1, skipna=True) * jobs["curr_factor"]


def salary_by_year_dynamic(jobs: pd.DataFrame) -> pd.DataFrame:
    # salary, published at
    jobs["year"] = jobs["published_at"].dt.year
    return jobs.groupby("year").mean(numeric_only=True)["salary"]
