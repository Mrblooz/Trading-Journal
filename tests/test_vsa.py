import pytest
import pandas as pd
from tools.vsa import VolumeSpreadAnalyzer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "High": [1.25, 1.26],
        "Low": [1.20, 1.25],
        "Volume": [150000, 120000]        
    })

def test_calculation_spread(sample_data):
    analyzer = VolumeSpreadAnalyzer()
    result = analyzer.calculate_spread(sample_data)
    assert "Spread" in result.columns, "Missing 'Spread' column in output."
    assert result["Spread"].iloc[0] == pytest.approx(0.05, rel=1e-3), "Incorrect spread calculation for first row."
    assert result["Spread"].iloc[1] == pytest.approx(0.01, rel=1e-3), "Incorrect spread calculation for second row."


def test_detect_vsa_signals(sample_data):
    analyzer = VolumeSpreadAnalyzer()
    sample_data = analyzer.calculate_spread(sample_data)
    result = analyzer.detect_vsa_signals(sample_data)
    assert "Volume Signal" in result.columns, "Missing 'Volume Signal' column in output."
    assert result["Volume Signal"].iloc[0] == "High Volume Wide Spread", "Incorrect VSA signal for first row."
    assert result["Volume Signal"].iloc[1] == "Low Volume Narrow Spread", "Incorrect VSA signal for second row."