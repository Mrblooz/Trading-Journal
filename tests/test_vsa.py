import pandas as pd
from tools.vsa import VolumeSpreadAnalyzer
import pytest

def test_calculate_spread():
    analyzer = VolumeSpreadAnalyzer()
    test_data = pd.DataFrame({
        "High": [1.25, 1.26],
        "Low": [1.20, 1.25]
    })

    result = analyzer.calculate_spread(test_data)
    assert "Spread" in result.columns, "Missing 'Spread' column in output."
    assert result["Spread"].iloc[0] == pytest.approx(0.05), "Incorrect spread calculation for first row."


def test_detect_vsa_signals():
    analyzer = VolumeSpreadAnalyzer()
    test_data = pd.DataFrame({
        "High": [1.25, 1.26],
        "Low": [1.20, 1.25],
        "Volume": [150000, 120000]
    })

    test_data = analyzer.calculate_spread(test_data)
    result = analyzer.detect_vsa_signals(test_data)

    assert "Volume Signal" in result.columns, "Missing 'Volume Signal' column in output."
    assert result["Volume Signal"].iloc[0] == "High Volume Wide Spread", "Incorrect VSA signal for first row."
    assert result["Volume Signal"].iloc[1] == "Neutral", "Incorrect VSA signal for second row."
