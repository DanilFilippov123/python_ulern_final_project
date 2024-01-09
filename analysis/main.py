import asyncio
import sys

import pandas as pd

import currency
import salary


def main():
    jobs_name = ["Разработчик"]

    if len(sys.argv) > 2:
        csv_file_name = sys.argv[1]
    else:
        csv_file_name = "vacancies.csv"

    df = pd.read_csv(csv_file_name,
                     parse_dates=["published_at"],
                     low_memory=False)

    df["curr_factor"] = asyncio.run(currency.async_get_currency(df))
    df["salary"] = salary.calc_salary(df)

    df.to_csv("tmp/vacancies_salary_currency.csv")

    jobs_by_name = salary.get_jobs_by_name(df, jobs_name)

    jobs_by_name.to_csv("tmp/vacancies_our_job.csv")

    salary_by_name_dynamic = salary.salary_by_year_dynamic(jobs_by_name)

    print(salary_by_name_dynamic)

    salary_by_name_dynamic.reset_index().to_html("result/salary_by_year_dynamic.html", index=False)


if __name__ == '__main__':
    main()
