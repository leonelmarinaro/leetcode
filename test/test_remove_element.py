import pytest
from solutions.remove_element import Solution


@pytest.fixture
def solution():
    return Solution()


def test_remove_element_case1(solution):
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_remove_element_case2(solution):
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]