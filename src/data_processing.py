from pathlib import Path

import pandas as pd

def load_data(path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic data cleaning."""
    df = df.copy()
    df = df.drop_duplicates()
    return df