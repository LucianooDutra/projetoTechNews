from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    list_news = find_news()

    if list_news is None:
        return []

    result_categories = []

    for new in list_news:
        categories = new["category"]
        result_categories.append(categories)

    dict_categories = Counter(sorted(result_categories))

    sort_categories = sorted(
        dict_categories, key=dict_categories.get, reverse=True
    )

    return sort_categories[:5]


# print(top_5_categories())
