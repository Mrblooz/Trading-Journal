import os
from app import DataManager

def test_load_data():
    manager = DataManager()
    filepath = "data/example_trades.csv"
    assert os.path.exists(filepath), "File does not exist!"
    data = manager.load_data(filepath)
    assert not data.empty, "Data failed to load!"