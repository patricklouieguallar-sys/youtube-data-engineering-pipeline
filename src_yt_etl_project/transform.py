import pandas as pd


def transform_csv(dframe):
    dframe["trending_date"] = pd.to_datetime(
        dframe["trending_date"], format="%y,%d.%m")
    dframe["publish_time"] = pd.to_datetime(["publish_time"])
    dframe["description"] = dframe["description"].fillna("")

    bool_cols = [
        "comments_disabled",
        "ratings_disabled",
        "video_error_or_removed",
    ]

    for colmuns in bool_cols:
        dframe[colmuns] = dframe[colmuns].astype(bool)

    return dframe
