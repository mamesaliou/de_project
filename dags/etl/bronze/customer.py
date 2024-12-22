import duckdb


def create_dataset(table_name="customer", source_database="tpch.db"):
    con = duckdb.connect(source_database)
    pulled_df = con.sql(f"select * from {table_name}").pl()
    return pulled_df.rename(lambda col_name: col_name[2:]).rename(
        {"custkey": "customer_key"}
    )
