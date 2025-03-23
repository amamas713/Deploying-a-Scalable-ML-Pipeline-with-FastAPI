import pytest
import pandas as pd
import os 
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Read the Census Data file into a Data Frame in Preparation for Unit Tests
@pytest.fixture(scope="session")
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    return df


def test_one(data):
    """
    # Data Validation - https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300
    """

    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42) 
    assert X.shape == (100, 2), "The shape of X should be (100, 2)"
    assert y.shape == (100, ), "The shape of y should be (100,)"
   

def test_two(data):
    """
    # Modeling Function - https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300
    """
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
    model = LogisticRegression(solver="liblinear", random_state=42) # Modified to use the solver in the original model rather than the default
    model.fit(X, y)
    assert hasattr(model, "coef_"), "The model should have attributes after training"


def test_three(data):
    """
    # Model Integration - https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300
    """
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
    model = LogisticRegression(solver="liblinear", random_state=42).fit(X, y) # Modified to use the solver in the original model rather than the default
    predictions = model.predict(X)
    assert set(predictions) <= {0, 1}, "Predictions should be 0 or 1"
    #pass
