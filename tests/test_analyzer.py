import pytest
import pandas as pd
from tools.analyzer import Analyzer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Entry Price":[1.2000, 1.2500, 1.2400],
        "Phase":["Undefined", "Undefined", "Undefined"]
    })

def test_detect_phases(sample_data):
    analyzer = Analyzer()
    result = analyzer.detect_phases(sample_data)

    assert "Phase" in result.columns, "Missing 'Phase' column in output."
    assert result["Phase"].iloc[0] == "Accumulation", "Incorrect phase detected for the first row"
    assert result["Phase"].iloc[1] == "Markup", "Incorrect phase detected for second row."

    