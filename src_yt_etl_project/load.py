def load_table(df, table_name, engine):
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )
