import pandas as pd


def geography(csv_file: str, salary_by_city_file: str, job_percent_by_city_file: str, salary_by_city_file_html: str, job_percent_by_city_file_html: str):
    df = pd.read_csv(csv_file, low_memory=False)

    job_percent_by_city: pd.DataFrame = (df.groupby("area_name")
                                         .count()[["name"]]
                                         .sort_values(ascending=False, by="name"))

    job_percent_by_city.columns = ["count"]
    job_percent_by_city["percent"] = (job_percent_by_city["count"] / len(df)) * 100
    job_percent_by_city.to_csv(job_percent_by_city_file, float_format=lambda x: f"{x:.5f}")

    job_percent_by_city[:10].to_html(job_percent_by_city_file_html, float_format=lambda x: f"{x:.5f}")

    df = df[~(df["salary"].isna()) & (df["salary"] < 100_000_000)]

    salary_by_city = df.groupby("area_name")["salary"].mean().sort_values(ascending=False).reset_index()
    salary_by_city = salary_by_city[salary_by_city["area_name"].isin(job_percent_by_city.reset_index()["area_name"][:10])]
    salary_by_city.to_csv(salary_by_city_file, float_format=lambda x: f"{x:.3f}", index=False)

    salary_by_city.to_html(salary_by_city_file_html, float_format=lambda x: f"{x:.3f}", index=False)


def main():
    geography("tmp/vacancies_our_job.csv",
              "result/salary_by_city_sys_admin.csv",
              "result/job_percent_by_city_sys_admin.csv",
              "result/html/salary_by_city_sys_admin.html",
              "result/html/job_percent_by_city_sys_admin.html")

    geography("tmp/vacancies_salary_currency.csv",
              "result/salary_by_city_all_jobs.csv",
              "result/job_percent_by_city_all_jobs.csv",
              "result/html/salary_by_city_all_jobs.html",
              "result/html/job_percent_by_city_all_jobs.html")


if __name__ == "__main__":
    main()
