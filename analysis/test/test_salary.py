from unittest import TestCase

import pandas as pd

from analysis.salary import salary_by_year_dynamic


class Test(TestCase):
    def test_salary_by_year_dynamic_nonempty(self):
        df = pd.read_csv("../w.csv",
                         parse_dates=["published_at"],
                         low_memory=False)
        w = salary_by_year_dynamic(df)
        print(w)
        self.assertFalse(w.empty, "Не должен быть пустым")
