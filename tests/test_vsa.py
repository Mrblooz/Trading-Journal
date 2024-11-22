from tools.vsa import VolumeSpreadAnalyzer
import pandas as pd

def test_detect_vsa_signals():
    analyzer = VolumeSpreadAnalyzer()
    test_data = pd.DataFrame({
        "High": [1.25, 1.26],
        "Low": [1.20, 1.25],
        "Volume": [150000, 120000]
    })

    print("Test Data Before Spread Calculation:")
    print(test_data)

    test_data = analyzer.calculate_spread(test_data)
    print("Test Data After Spread Calculation:")
    print(test_data)

    result = analyzer.detect_vsa_signals(test_data)
    print("Test Data After VSA Signal Detection:")
    print(result)

    assert "Volume Signal" in result.columns, "Missing 'Volume Signal' column in output."
    assert result["Volume Signal"].iloc[0] == "High Volume Wide Spread", "Incorrect VSA signal for first row."
    assert result["Volume Signal"].iloc[1] == "Low Volume Narrow Spread", "Incorrect VSA signal for second row."

