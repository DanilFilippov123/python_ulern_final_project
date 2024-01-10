import matplotlib.figure
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    count_all_jobs = pd.read_csv("result/count_jobs_by_year_dynamic_all_jobs.csv",
                                 names=["Год", "Количество вакансий"], header=0)
    count_sys_admin = pd.read_csv("result/count_jobs_by_year_dynamic_sys_admin.csv",
                                  names=["Год", "Количество вакансий"], header=0)

    salary_all_jobs = pd.read_csv("result/salary_jobs_by_year_dynamic_all_jobs.csv",
                                  header=0, names=["Год", "Зарплата"])
    salary_sys_admin = pd.read_csv("result/salary_jobs_by_year_dynamic_sys_admin.csv",
                                   header=0, names=["Год", "Зарплата"])

    (sns.catplot(data=count_all_jobs, x="Год", y="Количество вакансий", kind="point", aspect=2)
     .fig.savefig("result/count_jobs_by_year_dynamic_all_jobs.png"))

    (sns.catplot(data=count_sys_admin, x="Год", y="Количество вакансий", kind="point", aspect=2)
     .fig.savefig("result/count_jobs_by_year_dynamic_sys_admin.png"))

    (sns.catplot(data=salary_all_jobs, x="Год", y="Зарплата", kind="point", aspect=2)
     .fig.savefig("result/salary_jobs_by_year_dynamic_all_jobs.png"))

    (sns.catplot(data=salary_sys_admin, x="Год", y="Зарплата", kind="point", aspect=2)
     .fig.savefig("result/salary_jobs_by_year_dynamic_sys_admin.png"))
    plt.show()

if __name__ == "__main__":
    main()
