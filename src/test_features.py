import pandas as pd

from src.features import split_features_target


def test_split_features_target():
    df = pd.DataFrame(
        {
            "feature_1": [1, 2, 3],
            "feature_2": [4, 5, 6],
            "target": [10, 20, 30],
        }
    )

    X, y = split_features_target(df, "target")

    assert "target" not in X.columns
    assert list(X.columns) == ["feature_1", "feature_2"]
    assert list(y) == [10, 20, 30]

