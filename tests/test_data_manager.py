import os
import pandas as pd
import pytest
from tools.data_manager import DataManager

def test_load_data():
    manager = DataManager()
    filepath = "data/example_trades.csv"

    # Ensure file exists before testing
    assert os.path.exists(filepath), "Test file does not exist."

    data = manager.load_data(filepath)
    assert not data.empty, "Loaded data is empty."
    assert "Date" in data.columns, "Missing 'Date' column in data."

def test_save_data():
    manager = DataManager()
    test_data = pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "Asset": ["EUR/USD", "EUR/USD"],
        "High": [1.25, 1.26],
        "Low": [1.20, 1.25],
        "Entry Price": [1.2000, 1.2500],
        "Exit Price": [1.2500, 1.2600],
        "Volume": [100000, 120000]
    })

    filepath = "data/test_save_data.csv"
    manager.save_data(test_data, filepath)

    # Check if file is saved
    assert os.path.exists(filepath), "Saved file does not exist."

    # Cleanup after test
    os.remove(filepath)
