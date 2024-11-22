import pandas as pd
from tools.vsa import VolumeSpreadAnalyzer
from tools.analyzer import Analyzer

def test_detect_phases():
    analyzer = Analyzer()
    test_data = pd.DataFrame({
        "Entry Price": [1.2000, 1.2500, 1.2400],
        "Phase": ["Undefined", "Undefined", "Undefined"]
    })

    result = analyzer.detect_phases(test_data)
    assert "Phase" in result.columns, "Missing 'Phase' column in output."
    assert result["Phase"].iloc[0] == "Accumulation", "Incorrect phase detected for first row."
    assert result["Phase"].iloc[1] == "Markup", "Incorrect phase detected for second row."
