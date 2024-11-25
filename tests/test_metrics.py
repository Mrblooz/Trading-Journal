import pytest
import pandas as pd
from tools.performance_metrics import Metrics

@pytest.fixture
def sample_data():
    """
    Provide sample trade data for testing.
    """
    return pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]),
        "Entry Price": [1.20, 1.25, 1.15],
        "Exit Price": [1.22, 1.20, 1.18]
    })

@pytest.fixture
def empty_data():
    """
    Provide an empty DataFrame for edge case testing.
    """
    return pd.DataFrame(columns=["Date", "Entry Price", "Exit Price"]).astype({"Date": "datetime64[ns]"})

def test_calculate_metrics_success(sample_data):
    """
    Test that metrics are calculated correctly.
    """
    metrics = Metrics()
    result = metrics.calculate_metrics(sample_data)

    # Assertions
    assert result["Total Trades"] == 3, "Total trades should be 3."
    assert result["Profitable Trades"] == 2, "There should be 2 profitable trades."
    assert result["Losing Trades"] == 1, "There should be one Losing Trades."
    assert result["Win Rate (%)"] == 66.67, "Win Rate should be 66.67%."
    assert result["Profit/Loss Ratio"] != "N/A", "Profit/Loss Ratio should be calculated."
    assert result["Average Trade Duration (days)"] == 1.0, "Average Trade Duration should be 1 day."

def test_calculate_metrics_empty_data(empty_data):
    """
    Test that metrics calculation handles empty data correctly.
    """
    metrics = Metrics()
    result = metrics.calculate_metrics(empty_data)

    # Assertions
    assert result["Total Trades"] == 0, "Total trades should be 0 for empty data."
    assert result["Profitable Trades"] == 0, "Profitable trades should be 0 for empty data."
    assert result["Losing Trades"] == 0, "Losing trades should be 0 for empty data."
    assert result["Win Rate (%)"] == 0, "Win Rate should be 0% for empty data."
    assert result["Profit/Loss Ratio"] == "N/A", "Profit/Loss Ratio should be 'N/A' for empty data."
    assert result["Average Trade Duration (days)"] == "N/A", "Average Trade Duration should be 'N/A' for empty data."
