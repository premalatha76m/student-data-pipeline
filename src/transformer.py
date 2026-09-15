def transform_data(df):

    # Calculate average
    df["average"] = (
        df["python"]
        + df["dbms"]
        + df["web"]
    ) / 3

    # Round average
    df["average"] = df["average"].round(2)

    # Calculate grade
    def calculate_grade(mark):

        if mark >= 90:
            return "A+"

        elif mark >= 80:
            return "A"

        elif mark >= 70:
            return "B"

        elif mark >= 60:
            return "C"

        elif mark >= 50:
            return "D"

        else:
            return "F"

    df["grade"] = df["average"].apply(
        calculate_grade
    )

    return df
