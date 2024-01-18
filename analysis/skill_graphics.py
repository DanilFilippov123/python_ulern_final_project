import wordcloud
import numpy as np
import pandas as pd
import ast
import seaborn as sns


def main(csv_file: str, result_file: str):
    df = pd.read_csv(csv_file, index_col="year")
    df["key_skills"] = df["key_skills"].apply(lambda x: ast.literal_eval(x))

    all_skills_freq: dict[int, list[tuple[str, int]]] = df.to_dict()["key_skills"]
    last_five_year_skills: list[tuple[str, str]] = np.concatenate([all_skills_freq[year] for year in all_skills_freq.keys()])
    last_five_year_most_common_skill = dict()

    for (skill, count) in last_five_year_skills:
        if skill not in last_five_year_most_common_skill.keys():
            last_five_year_most_common_skill[skill] = int(count)
        else:
            last_five_year_most_common_skill[skill] += int(count)
    words_graphic = wordcloud.WordCloud(font_step=12, min_font_size=10, max_font_size=400,
                                        width=1000, height=400,
                                        background_color="#BFD9C5",
                                        colormap="tab10")
    cloud: wordcloud.WordCloud = words_graphic.fit_words(last_five_year_most_common_skill)
    cloud.to_file(result_file)


if __name__ == "__main__":
    main("result/skill_by_year_sys_admin.csv", "result/skill_by_year_sys_admin.png")
    main("result/skill_by_year_all_jobs.csv", "result/skill_by_year_all_jobs.png")
