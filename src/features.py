import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create basic model features."""
    df = df.copy()
    return df


def split_features_target(df: pd.DataFrame, target_col: str):
    """Split a DataFrame into features X and target y."""
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y