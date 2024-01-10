import pandas as pd


def relevance(csv_file: str, count_file: str, salary_file: str):
    df = pd.read_csv(csv_file,
                     parse_dates=["published_at"],
                     low_memory=False)
    df["year"] = df["published_at"].apply(lambda x: x.year)
    df.groupby("year").count()[["name"]].to_csv(f"result/{count_file}")

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    mean_salary_by_year: pd.DataFrame = df.groupby("year")["salary"].mean().reset_index()
    mean_salary_by_year.to_csv(f"result/{salary_file}", index=False, float_format=lambda x: f"{x:.3f}")


def main():
    relevance("tmp/vacancies_our_job.csv",
              "count_jobs_by_year_dynamic_sys_admin.csv",
              "salary_jobs_by_year_dynamic_sys_admin.csv")
    relevance("tmp/vacancies_salary_currency.csv",
             "count_jobs_by_year_dynamic_all_jobs.csv",
             "salary_jobs_by_year_dynamic_all_jobs.csv")



if __name__ == "__main__":
    main()
