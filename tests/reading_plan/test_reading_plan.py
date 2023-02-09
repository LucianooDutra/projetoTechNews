from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tests.assets.news import NEWS
import pytest


def get_news():
    return NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch("tech_news.analyzer.reading_plan.find_news", new=get_news)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    result = ReadingPlanService.group_news_for_available_time(4)

    unfilled_content = [1, 0, 1, 3]

    readable_content = [
        [("noticia_0", 2), ("Notícia bacana 2", 1)],
        [("Notícia bacana", 4)],
        [("noticia_3", 1), ("noticia_4", 1), ("noticia_5", 1)],
        [("noticia_6", 1)],
    ]

    unreadable_content = [
        ("noticia_7", 7),
        ("noticia_8", 8),
        ("noticia_9", 5),
    ]

    for index, readable in enumerate(result["readable"]):
        assert readable["unfilled_time"] == unfilled_content[index]
        assert readable["chosen_news"] == readable_content[index]

    assert len(result["unreadable"]) != 0

    for index, unreadable in enumerate(result["unreadable"]):
        assert unreadable == unreadable_content[index]
