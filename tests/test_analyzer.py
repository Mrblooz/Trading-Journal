import pytest
import pandas as pd
from tools.analyzer import Analyzer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Entry Price"
    })