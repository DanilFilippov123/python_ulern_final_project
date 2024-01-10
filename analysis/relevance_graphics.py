import pandas as pd
import seaborn as sns


def main():
    count_all_jobs = pd.read_html("result/count_jobs_by_year_dynamic_all_jobs.html")
    count_sys_admin = pd.read_html("result/count_jobs_by_year_dynamic_sys_admin.html")
    salary_all_jobs = pd.read_html("result/salary_jobs_by_year_dynamic_all_jobs.html")
    salary_sys_admin = pd.read_html("result/salary_jobs_by_year_dynamic_sys_admin.html")
    sns.lineplot(count_all_jobs, x="Год", y="Количество вакансий")


if __name__ == "__main__":
    main()
