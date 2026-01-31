import pandas as pd
from titanic_project.data_preprocessing import save_raw_to_interim

def test_save_raw_to_interim(tmp_path):
    # Création de faux fichiers raw dans un dossier temporaire
    raw_train = tmp_path / "train.csv"
    raw_test = tmp_path / "test.csv"

    df_train = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df_test = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

    df_train.to_csv(raw_train, index=False)
    df_test.to_csv(raw_test, index=False)

    # Chemins de sortie dans le dossier temporaire
    interim_train = tmp_path / "train_clean.csv"
    interim_test = tmp_path / "test_clean.csv"

    # Appel de la fonction
    save_raw_to_interim(
        raw_train_path=raw_train,
        raw_test_path=raw_test,
        interim_train_path=interim_train,
        interim_test_path=interim_test
    )

    # Vérification que les fichiers ont été créés
    assert interim_train.exists()
    assert interim_test.exists()

    # Vérification du contenu
    saved_train = pd.read_csv(interim_train)
    saved_test = pd.read_csv(interim_test)

    pd.testing.assert_frame_equal(saved_train, df_train)
    pd.testing.assert_frame_equal(saved_test, df_test)