import pandas as pd
import os
from titanic_project.model_training import (
    preprocess_features,
    train_model,
    generate_predictions,
    save_submission
)


def test_preprocess_features():
    train_df = pd.DataFrame({
        "Pclass": [1, 3],
        "Sex": ["male", "female"],
        "SibSp": [0, 1],
        "Parch": [0, 2]
    })

    test_df = pd.DataFrame({
        "Pclass": [2],
        "Sex": ["female"],
        "SibSp": [1],
        "Parch": [0]
    })

    feature_columns = ["Pclass", "Sex", "SibSp, Parch"]

    X_train, X_test = preprocess_features(train_df, test_df, ["Pclass", "Sex", "SibSp", "Parch"])

    assert X_train.shape[1] == X_test.shape[1]
    assert not X_train.isnull().any().any()
    assert not X_test.isnull().any().any()


def test_train_model():
    X_train = pd.DataFrame({
        "Pclass": [1, 3],
        "Sex_female": [0, 1],
        "Sex_male": [1, 0]
    })
    y_train = pd.Series([0, 1])

    model = train_model(X_train, y_train)

    assert hasattr(model, "predict")


def test_generate_predictions():
    X_train = pd.DataFrame({
        "Pclass": [1, 3],
        "Sex_female": [0, 1],
        "Sex_male": [1, 0]
    })
    y_train = pd.Series([0, 1])

    model = train_model(X_train, y_train)

    X_test = pd.DataFrame({
        "Pclass": [2],
        "Sex_female": [1],
        "Sex_male": [0]
    })

    predictions = generate_predictions(model, X_test)

    assert len(predictions) == 1
    assert predictions[0] in [0, 1]


def test_save_submission(tmp_path):
    passenger_ids = pd.Series([1, 2])
    predictions = [0, 1]

    output_file = tmp_path / "submission.csv"

    df = save_submission(passenger_ids, predictions, output_file)

    assert output_file.exists()
    assert len(df) == 2
    assert list(df.columns) == ["PassengerId", "Survived"]