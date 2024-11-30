import pandas as pd
import pytest
from solutions.pandas.articles_views import article_views_df


def test_article_views_case1():
    data = {"author_id": [1, 2, 3, 4, 5], "viewer_id": [1, 2, 3, 4, 6]}
    views = pd.DataFrame(data)
    result = article_views_df(views)
    expected_data = {"id": [1, 2, 3, 4]}
    expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)


def test_article_views_case2():
    data = {"author_id": [1, 2, 2, 3, 4, 5], "viewer_id": [1, 2, 2, 3, 4, 6]}
    views = pd.DataFrame(data)
    result = article_views_df(views)
    expected_data = {"id": [1, 2, 3, 4]}
    expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)


def test_article_views_case3():
    data = {"author_id": [1, 2, 3, 4, 5], "viewer_id": [6, 7, 8, 9, 10]}
    views = pd.DataFrame(data)
    result = article_views_df(views)
    expected_data = {"id": []}
    expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
