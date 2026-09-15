import pandas as pd


def clean_data(df, minimum_mark=0, maximum_mark=100):

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Clean names
    if "name" in df.columns:
        df["name"] = (
            df["name"]
            .astype("string")
            .str.strip()
        )

    # Convert numeric columns
    numeric_columns = [
        "age",
        "python",
        "dbms",
        "web"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # Remove rows where name is missing
    df = df.dropna(subset=["name"])

    # Fill missing age
    if "age" in df.columns:
        df["age"] = df["age"].fillna(
            df["age"].median()
        )

    # Handle marks
    mark_columns = [
        "python",
        "dbms",
        "web"
    ]

    for column in mark_columns:

        if column in df.columns:

            df[column] = df[column].fillna(0)

            df[column] = df[column].clip(
                minimum_mark,
                maximum_mark
            )

    return df
