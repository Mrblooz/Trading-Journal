import pandas as pd
import logging

# initialize logger for PerformanceMetrics
logger = logging.getLogger()

class PerformanceMetrics:
    """
    A class to calculate and analyze performance metrics for trading data.    
    """

    def __init__(self, data):
        """
        Initialize with the trading data.
        Args:
            data(pd.DataFrame): The trading data DataFrame.
        """
        self.data = data

    def calculate_pnl(self):
        """
        Calculate profit/loss (PnL) for each trade
        Adds a new 'PnL' column to the DataFrame        
        """
        logger.info("Calculate Profit/Loss (PnL) for each trade...")
        try:
            # Assuming 'Size' column exists; default to 1 if not 
            self.data["Size"] = self.data.get("Size", 1)
            self.data["PnL"] = (self.data["Exit Price"] - self.data["Entry Price"]) * self.data["Size"]            
            logger.info("PnL calculation  Completed.")
            return self.data
        except Exception as e:
            logger.error("Error calculating PnL.", exc_info=True)
            raise

    def categorize_trades(self):
        """
        Categorize each trade as a 'Win' or 'Loss'.
        Adds a new 'Trade Result' column to the DataFrame
        """
        logger.info("Categorizing trades as 'Win' or 'Loss'...")
        try:
            self.data["Trade Result"] = self.data["PnL"].apply(lambda x: "Win" if x > 0 else "Loss")
            logger.info("Trade categorization Completed.")
            return self.data
        except Exception as e:
            logger.error("Error categorizing trades.", exc_info=True)
            raise

    def calculate_total_pnl(self):
        """
        Calculate the total profit/loss across all trades.
        Returns:
            float: Total PnL.
        """
        logger.info(f"Total PnL...")
        try:
            total_pnl = self.data["PnL"].sum()
            logger.info(f"Total PnL": {total_pnl})
            return total_pnl
        except Exception as e:
            logger.error("Error Calculating total PnL.", exc_info = True)
            raise

    def calculate_win_rate(self):
        """
        Calculate the win rate as a percentage.
        Returns:
            float: Win rate percentage.
        """
        logger.info("Calculating win rate...")
        try:
            total_trades = len(self.data)
            wins = len(self.data[self.data["Trade Result"] == "Win"])
            win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0
            logger.info(f"Win Rate: {win_rate:.2f}%")
            return win_rate
        except Exception as e:
            logger.error("Error Calculating win rate.", exc_info=True)
            raise

    def calculate_risk_reward(self):
        """
        Calculate the risk/reward ration
        Returns
            float: Risk/reward ratio.         
        """
        logger.info("Calculating risk/reward ratio...")
        try:
            avg_profit = self.data[self.data["PnL"] > 0]["PnL"].mean()
            avg_loss = abs(self.data[self.data["PnL"] > 0]["PnL"].mean())
            risk_reward = avg_profit / avg_loss if avg_loss else float("Inf")
            logger.info(f"Risk/Reward Ratio: {risk_reward:.2f}")
            return risk_reward
        except Exception as e:
            logger.error("Error calculating risk/reward ratio.", exc_info = True)
            raise

    def calculate_cumulative_pnl(self):
        """
        Calculate the cumulative PnL over time.
        Adds a 'Cumulative PnL' column to the DataFrame
        """
        logger.info("Calculating cumulative PnL...")
        try:
            self.data["Cumulative PnL"] = self.data["PnL"].cumsum()
            logger.info("Cumulative PnL calculation complete")
            return self.data
        except Exception as e:
            logger.error("Error calculating cumulative PnL.", exc_info=True)
            raise

        

                                   








