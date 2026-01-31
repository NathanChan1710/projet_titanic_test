import pandas as pd
from sklearn.ensemble import RandomForestClassifier

    
def load_dataset(train_path: str, test_path: str):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df


def preprocess_features(train_df: pd.DataFrame, test_df: pd.DataFrame, feature_columns: list):
    X_train = pd.get_dummies(train_df[feature_columns])
    X_test = pd.get_dummies(test_df[feature_columns])

    # Align columns (important when dummy columns differ)
    X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0)

    return X_train, X_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series):
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=1
    )
    model.fit(X_train, y_train)
    return model


def generate_predictions(model, X_test: pd.DataFrame):
    return model.predict(X_test)


def save_submission(passenger_ids, predictions, output_path: str):
    submission_df = pd.DataFrame({
        "PassengerId": passenger_ids,
        "Survived": predictions
    })
    submission_df.to_csv(output_path, index=False)
    return submission_df