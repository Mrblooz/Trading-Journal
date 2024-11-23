import pytest
import pandas as pd
from tools.data_manager import DataManager

@pytest.fixture

def sample_data():
    return pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "Entry Price": [1.2, 1.25],
        "Exit Price": [1.22, 1.28],
        "Volume": [100000, 120000]
    })

def test_load_data(mocker, sample_data):
    mocker.patch("pandas.read_csv", return_value=sample_data)
    manager = DataManager()
    data = manager.load_data("dummy_path.csv")
    pd.testing.assert_frame_equal(data, sample_data)

def test_save_data(mocker, sample_data):
    mock_to_csv = mocker.patch.object(pd.DataFrame, "to_csv")
    manager = DataManager()
    manager.save_data(sample_data, "dummy_path.csv")
    mock_to_csv.assert_called_once_with("dummy_path.csv", index=False)

def test_fetch_historical_data(mocker):
    mock_download = mocker.patch("yfinance.download", return_value=pd.DataFrame({"Mock": [1, 2, 3]}))
    manager = DataManager()
    data = manager.fetch_historical_data()
    assert not data.empty
    mock_download.assert_called_once()
    