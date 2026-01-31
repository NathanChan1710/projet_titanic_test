# titanic_project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Objectif du projet
Le projet à pour principe de nous faire appliquer les bonnes pratiques d’ingénierie logicielle vues pendant ce cours à un projet Data existant fourni sous forme de notebook python.

⇒Vous devez travailler en équipe (min 2, max 4) et utiliser l’outil collaboratif GIT ainsi qu’un répertoire projet sur github  

⇒Pour la partie CI/CD, il est recommandé d’utiliser Github Actions comme votre projet sera déjà sur Github  

⇒Vous êtes libres d’utiliser l’IDE python de votre choix  

⇒Deadline du projet : Dimanche 8 Février 2026  

⇒Restitution : URL de votre projet github à partager avec un rapport détaillé (pdf ou doc) à déposer dans un drive dédié à votre groupe qui vous sera partagé.

## Les instructions d’installation et d’utilisation.
Il faut faire Git Pull dans votre terminal avec le lien du repository, ensuite faire **pip install -r requirements.txt** pour charger les packages nécessaire à l'utilisation du projet

## Les contributions des membres de l’équipe.
- Nathan =
- Camille = 
- Manohy = 
- Assisa = 

first tianic project

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         titanic_project and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── titanic_project   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes titanic_project a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

