import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter


def percent_graphic(file_name: str, df: pd.DataFrame, top: int = 10):
    colors = sns.color_palette('vlag')

    top_10_percents = df["percent"][:top].to_dict()
    top_10_percents["Остальные"] = df["percent"][top:].sum()
    my_dpi = 120
    plt.figure(figsize=(1200 / my_dpi, 800 / my_dpi), dpi=my_dpi)
    plt.pie(top_10_percents.values(), labels=top_10_percents.keys(), colors=colors, autopct='%.0f%%', radius=1.25)
    plt.savefig(file_name)


def mean_salary_graphic(file_name: str, df: pd.DataFrame, top: int = 10):
    my_dpi = 120
    plt.figure(figsize=(1700 / my_dpi, 800 / my_dpi), dpi=my_dpi)
    plt.ticklabel_format(style="plain")

    df["Средняя зарплата"] = df["Средняя зарплата"].astype(int)
    df["Город"] = df["Город"].apply(lambda x: x.split()[0] if len(x) > 20 else x)
    city: pd.DataFrame = df[:top]
    sns.barplot(hue=city["Город"], data=city, x="Город", y="Средняя зарплата")
    plt.savefig(file_name)




def main():
    all_job_percents = pd.read_csv("result/job_percent_by_city_all_jobs.csv", index_col="area_name")
    sys_admin_percent = pd.read_csv("result/job_percent_by_city_sys_admin.csv", index_col="area_name")
    all_jobs_salary = pd.read_csv("result/salary_by_city_all_jobs.csv", header=0, names=["Город", "Средняя зарплата"])
    sys_admin_salary = pd.read_csv("result/salary_by_city_sys_admin.csv", header=0, names=["Город", "Средняя зарплата"])

    all_jobs_salary = all_jobs_salary[all_jobs_salary["Город"].isin(all_job_percents.reset_index()["area_name"][:10])]
    sys_admin_salary = sys_admin_salary[sys_admin_salary["Город"].isin(all_job_percents.reset_index()["area_name"][:10])]

    percent_graphic("result/job_percent_by_city_all_jobs.png", all_job_percents)
    percent_graphic("result/job_percent_by_city_sys_admin.png", sys_admin_percent)
    mean_salary_graphic("result/salary_by_city_all_jobs.png", all_jobs_salary)
    mean_salary_graphic("result/salary_by_city_sys_admin.png", sys_admin_salary)
    plt.show()


if __name__ == "__main__":
    main()
