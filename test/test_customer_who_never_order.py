import pytest
import pandas as pd
from solutions.customer_who_never_order import find_customers

def test_find_customers_case1():
    customers_data = {"id": [1, 2, 3, 4], "name": ["Alice", "Bob", "Charlie", "David"]}
    orders_data = {"orderId": [101, 102], "customerId": [1, 3]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Bob", "David"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case2():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [101], "customerId": [1]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Bob", "Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case3():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [], "customerId": []}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Alice", "Bob", "Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case4():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [101, 102, 103], "customerId": [1, 2, 3]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": []}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case5():
    customers_data = {"id": [1, 2, 3, 4, 5], "name": ["Alice", "Bob", "Charlie", "David", "Eve"]}
    orders_data = {"orderId": [101, 102, 103, 104], "customerId": [1, 2, 3, 5]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["David"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case6():
    customers_data = {"id": [1, 2, 3, 4], "name": ["Alice", "Bob", "Charlie", "David"]}
    orders_data = {"orderId": [101, 102, 103], "customerId": [1, 2, 4]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case7():
    customers_data = {"id": [1, 2], "name": ["Alice", "Bob"]}
    orders_data = {"orderId": [101], "customerId": [1]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Bob"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case8():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [101, 102], "customerId": [1, 2]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.reset_index(drop=True).equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case2():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [101], "customerId": [1]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Bob", "Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case3():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [], "customerId": []}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Alice", "Bob", "Charlie"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"


def test_find_customers_case4():
    customers_data = {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    orders_data = {"orderId": [101, 102, 103], "customerId": [1, 2, 3]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": []}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    assert result_df.equals(
        expected_output_df
    ), f"Expected {expected_output_df} but got {result_df}"
