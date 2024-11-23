import pytest
import pandas as pd
from unittest.mock import MagicMock
from app import TradingJournalApp

def test_app_run():
    # Mocking dependencies
    app = TradingJournalApp()
    
    # Mock data including necessary columns
    mock_data = pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "Entry Price": [1.20, 1.25],
        "Exit Price": [1.22, 1.28],
        "High": [1.30, 1.35],
        "Low": [1.15, 1.20],
        "Volume": [100000, 120000]
    })   

    app.data_manager.load_data = MagicMock(return_value=mock_data)
    app.analyzer.detect_phases = MagicMock(return_value=mock_data)
    app.vsa_analyzer.calculate_spread = MagicMock(return_value=mock_data)
    app.vsa_analyzer.detect_vsa_signals = MagicMock(return_value=mock_data)
    app.visualizer.plot_data = MagicMock()

    # Run the app
    app.run()

    # Verify that methods were called with the correct arguments
    app.data_manager.load_data.assert_called_once_with("data/example_trades.csv")
    app.analyzer.detect_phases.assert_called_once_with(mock_data)
    app.vsa_analyzer.calculate_spread.assert_called_once_with(mock_data)
    app.vsa_analyzer.detect_vsa_signals.assert_called_once_with(mock_data)
    app.visualizer.plot_data.assert_called_once_with(mock_data)
