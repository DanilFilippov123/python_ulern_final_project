import datetime
import json
from dateutil import parser
import requests


def salary(salary_dict: dict | None) -> dict | None:
    if salary_dict is None:
        return None
    res = {}
    _from = salary_dict["from"]
    to = salary_dict["to"]
    if to is None and _from is None:
        return None
    if to is None or _from is None:
        res["value"] = to or _from
    else:
        res["value"] = f"{(_from + to) / 2:.3f}"
    res["currency"] = salary_dict["currency"] if salary_dict["currency"] is not None else "RUR"
    return res


def hh_json_prepare(json_obj: dict) -> dict:
    job = {
        "name": json_obj["name"],
        "employer": json_obj["employer"]["name"],
        "salary": salary(json_obj["salary"]),
        "area_name": json_obj["area"]["name"],
        "published_at": parser.parse(json_obj["published_at"])
    }
    url = f'https://api.hh.ru/vacancies/{json_obj["id"]}'
    req = requests.get(url)
    additional_info = json.loads(req.content.decode())
    req.close()
    job["description"] = additional_info["description"]
    job["key_skills"] = ", ".join([skill["name"] for skill in additional_info["key_skills"]])
    return job
