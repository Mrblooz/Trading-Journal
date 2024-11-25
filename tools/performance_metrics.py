import pandas as pd
import logging

# Initialize logger for Metrics
logger = logging.getLogger("Metrics")

class Metrics:
    """
    Calculates performance metrics for trading data.
    """

    def calculate_metrics(self, data):
        """
        Calculate various performance metrics from the trade data.
        Args:
            data (pd.DataFrame): DataFrame containing trade data with 'Entry Price' and 'Exit Price'.
        Returns:
            dict: Dictionary containing calculated metrics.
        """
        logger.info("Starting metrics calculation...")
        try:
            # Ensure required columns are present
            required_columns = ["Entry Price", "Exit Price"]
            if not all(col in data.columns for col in required_columns):
                raise ValueError(f"Missing required columns for metrics calculation: {required_columns}")

            # Calculate metrics
            total_trades = len(data)
            profitable_trades = len(data[data["Exit Price"] > data["Entry Price"]])
            losing_trades = len(data[data["Exit Price"] <= data["Entry Price"]])
            win_rate = (profitable_trades / total_trades) * 100 if total_trades > 0 else 0

            avg_profit = data.loc[data["Exit Price"] > data["Entry Price"], "Exit Price"].mean()
            avg_loss = data.loc[data["Exit Price"] <= data["Entry Price"], "Exit Price"].mean()
            
            # Handle edge cases for Profit/Loss Ratio
            if pd.notna(avg_profit) and pd.notna(avg_loss) and avg_loss != 0:
                profit_loss_ratio = avg_profit / abs(avg_loss)
            else:
                profit_loss_ratio = "N/A"

            # Handle Trade Duration if Date exists
            if "Date" in data.columns and not data["Date"].empty:
                try:
                    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
                    data["Trade Duration"] = data["Date"].diff().dt.days
                    avg_duration = data["Trade Duration"].mean()
                except Exception as e:
                    logger.warning("Trade Duration calculation failed. Defaulting to 'N/A'.", exc_info=True)
                    avg_duration = "N/A"
            else:
                avg_duration = "N/A"

            # Compile metrics into a dictionary
            metrics = {
                "Total Trades": total_trades,
                "Profitable Trades": profitable_trades,
                "Losing Trades": losing_trades,
                "Win Rate (%)": round(win_rate, 2),
                "Profit/Loss Ratio": round(profit_loss_ratio, 2) if profit_loss_ratio != "N/A" else "N/A",
                "Average Trade Duration (days)": round(avg_duration, 2) if avg_duration != "N/A" else "N/A"
            }

            logger.info("Metrics calculation completed.")
            return metrics
        except Exception as e:
            logger.error("Error during metrics calculation.", exc_info=True)
            raise
