import pandas as pd


def relevance(csv_file: str, count_file: str, salary_file: str, count_html_file: str, salary_html_file: str):
    df = pd.read_csv(csv_file,
                     parse_dates=["published_at"],
                     low_memory=False)
    df["year"] = df["published_at"].apply(lambda x: x.year)
    job_by_year = df.groupby("year").count()[["name"]]
    job_by_year.columns = ["count"]
    job_by_year.to_csv(count_file)

    job_by_year.to_html(count_html_file)

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    mean_salary_by_year: pd.DataFrame = df.groupby("year")["salary"].mean().reset_index()
    mean_salary_by_year.to_csv(salary_file, index=False, float_format=lambda x: f"{x:.3f}")

    mean_salary_by_year.to_html(salary_html_file, index=False, float_format=lambda x: f"{x:.3f}")


def main():
    relevance("tmp/vacancies_our_job.csv",
              "result/count_jobs_by_year_dynamic_sys_admin.csv",
              "result/salary_jobs_by_year_dynamic_sys_admin.csv",
              "result/html/count_jobs_by_year_dynamic_sys_admin.html",
              "result/html/salary_jobs_by_year_dynamic_sys_admin.html")

    relevance("tmp/vacancies_salary_currency.csv",
              "result/count_jobs_by_year_dynamic_all_jobs.csv",
              "result/salary_jobs_by_year_dynamic_all_jobs.csv",
              "result/html/count_jobs_by_year_dynamic_all_jobs.html",
              "result/html/salary_jobs_by_year_dynamic_all_jobs.html")


if __name__ == "__main__":
    main()
