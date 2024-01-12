import pandas as pd


def geography(csv_file: str, salary_by_city_file: str, job_percent_by_city_file: str):
    df = pd.read_csv(csv_file, low_memory=False)

    job_percent_by_city: pd.DataFrame = (df.groupby("area_name")
                                         .count()[["name"]]
                                         .sort_values(ascending=False, by="name"))

    job_percent_by_city.columns = ["count"]
    job_percent_by_city["percent"] = job_percent_by_city["count"] / len(df)
    job_percent_by_city.to_csv(job_percent_by_city_file, float_format=lambda x: f"{x:.5f}%")

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    (df.groupby("area_name")["salary"]
     .mean()
     .sort_values(ascending=False)
     .to_csv(salary_by_city_file, float_format=lambda x: f"{x:.3f}"))


def main():
    geography("tmp/vacancies_our_job.csv",
              "result/salary_by_city_sys_admin.csv",
              "result/job_percent_by_city_sys_admin.csv")

    geography("tmp/vacancies_salary_currency.csv",
              "result/salary_by_city_all_jobs.csv",
              "result/job_percent_by_city_all_jobs.csv")


if __name__ == "__main__":
    main()
