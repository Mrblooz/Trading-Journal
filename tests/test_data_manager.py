import pytest
import pandas as pd
from tools.data_manager import DataManager
from unittest.mock import patch

@pytest.fixture
def sample_data():
    """
    Provide sample trade data for tests.
    """
    return pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "Entry Price": [1.20, 1.25],
        "Exit Price": [1.22, 1.28],
        "Volume": [100000, 120000]
    })

def test_load_data(mocker, sample_data):
    """
    Test loading data from a CSV file.
    """
    # Mock file existence and pandas.read_csv
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("pandas.read_csv", return_value=sample_data)

    manager = DataManager()
    data = manager.load_data("dummy_path.csv")

    # Assert that the loaded data matches the sample data
    pd.testing.assert_frame_equal(data, sample_data)

def test_load_data_file_not_found(mocker):
    """
    Test loading data when the file is not found.
    """
    # Mock file not existing
    mocker.patch("os.path.exists", return_value=False)

    manager = DataManager()
    with pytest.raises(FileNotFoundError):
        manager.load_data("dummy_path.csv")

def test_save_data(mocker, sample_data):
    """
    Test saving data to a CSV file.
    """
    # Mock the DataFrame.to_csv method
    mock_to_csv = mocker.patch.object(pd.DataFrame, "to_csv")

    manager = DataManager()
    manager.save_data(sample_data, "data/example_trades.csv")

    # Assert that to_csv was called with the correct arguments
    mock_to_csv.assert_called_once_with("data/example_trades.csv", index=False)

def test_fetch_historical_data(mocker):
    """
    Test fetching historical data using yfinance.
    """
    # Mock yfinance.download to return a sample DataFrame
    mock_download = mocker.patch("yfinance.download", return_value=pd.DataFrame({
        "Open": [150, 155],
        "Close": [152, 157]
    }))

    manager = DataManager()
    data = manager.fetch_historical_data("AAPL", "2023-01-01", "2023-01-31")

    # Assertions
    assert not data.empty, "The returned DataFrame should not be empty."
    assert "Open" in data.columns, "The expected column 'Open' was not found in the returned data."
    mock_download.assert_called_once_with("AAPL", start="2023-01-01", end="2023-01-31")

def test_fetch_historical_data_empty(mocker):
    """
    Test fetching historical data with no results.
    """
    # Mock yfinance.download to return an empty DataFrame
    mock_download = mocker.patch("yfinance.download", return_value=pd.DataFrame())

    manager = DataManager()
    data = manager.fetch_historical_data("AAPL", "2023-01-01", "2023-01-31")

    # Assert that the DataFrame is empty and a warning is logged
    assert data.empty, "The DataFrame should be empty when no data is fetched."
    mock_download.assert_called_once_with("AAPL", start="2023-01-01", end="2023-01-31")

def test_validate_data_success(sample_data):
    """
    Test validating data with all required columns present.
    """
    manager = DataManager()
    # Should not raise any exception
    manager.validate_data(sample_data, ["Date", "Entry Price", "Exit Price", "Volume"])

def test_validate_data_missing_column(sample_data):
    """
    Test validating data with missing required columns.
    """
    manager = DataManager()
    with pytest.raises(ValueError):
        manager.validate_data(sample_data, ["Date", "Entry Price", "Nonexistent Column"])
    