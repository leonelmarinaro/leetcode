import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left', indicator=True)
    customers_without_orders = merged_df[merged_df['_merge'] == 'left_only'][['name']]
    customers_without_orders = customers_without_orders.rename(columns={"name": "Customers"})
    return customers_without_orders.reset_index(drop=True)

# Caso de prueba para depurar
if __name__ == "__main__":
    customers_data = {"id": [1, 2, 3, 4], "name": ["Alice", "Bob", "Charlie", "David"]}
    orders_data = {"orderId": [101, 102], "customerId": [1, 3]}

    customers_df = pd.DataFrame(customers_data)
    orders_df = pd.DataFrame(orders_data)

    expected_output_data = {"Customers": ["Bob", "David"]}
    expected_output_df = pd.DataFrame(expected_output_data)

    result_df = find_customers(customers_df, orders_df)

    print("Expected Output:")
    print(expected_output_df)
    print("\nResult Output:")
    print(result_df)

    assert result_df.equals(expected_output_df), f"Expected {expected_output_df} but got {result_df}"