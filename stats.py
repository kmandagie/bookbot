from typing import Any


def get_word_count(txt: str):
    return len(txt.split())


def num_char(txt: str):
    list_txt = txt.split(" ")
    res = {}
    for w in list_txt:
        for t in w:
            lower = t.lower()
            if lower not in res:
                res[lower] = 0
            res[lower] += 1
    return res


def by_num(data):
    return data["num"]


def sort_by_number(data: list[dict[str, int]]):
    return data.sort(key=by_num, reverse=True)


def transform_sort(data: dict[str, int]):
    result: list[dict[str, Any]] = []
    for k, v in data.items():
        result.append({"char": k, "num": v})
    sort_by_number(result)
    return result
