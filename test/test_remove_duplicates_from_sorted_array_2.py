import pytest
from solutions.remove_duplicates_from_sorted_array_2 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case1(solution):
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = solution.removeDuplicates(nums)
    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]


def test_case2(solution):
    nums = [1, 1, 1, 2, 2, 3]
    k = solution.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]
