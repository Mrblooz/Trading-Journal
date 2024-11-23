import pandas as pd
from tools.phases import PhaseAnalyzer

def test_detect_phases():
    """
    Test the detection of Wyckoff phases based on the example data.
    """
    # Instantiate the phase detector
    detector = PhaseAnalyzer(rolling_window=2)

    # Example data to test
    test_data = pd.DataFrame({
        "Entry Price": [1.20, 1.25, 1.30, 1.15, 1.10],
        "Volume": [100000, 150000, 120000, 140000, 110000]
    })

    # Apply phase detection logic
    result = detector.detect_phases(test_data)

    # Debug: Print resultaat
    print("Testresultaat:")
    print(result)

    # Assertions aangepast aan correcte logica
    assert "Phase" in result.columns, "Phase column not added to the data."
    assert result["Phase"].iloc[0] == "Undefined", "Incorrect phase detected for first row."
    assert result["Phase"].iloc[1] == "Distribution", "Incorrect phase detected for second row."
    assert result["Phase"].iloc[2] == "Distribution", "Incorrect phase detected for third row."
    assert result["Phase"].iloc[3] == "Markup", "Incorrect phase detected for fourth row."
    assert result["Phase"].iloc[4] == "Markup", "Incorrect phase detected for fifth row."
