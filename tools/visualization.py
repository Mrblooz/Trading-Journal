import matplotlib.pyplot as plt
import logging

# Initialize logger for Visualizer
logger = logging.getLogger("Visualizer")

class Visualizer:
    """
    Creates visualizations for trading data, including price trends and phases.
    """

    def plot_data(self, data):
        """
        Generates a plot of entry and exit prices with annotated Wyckoff phases.
        Args:
            data (pd.DataFrame): Trade data with 'Date', 'Entry Price', 'Exit Price', and 'Phase'.
        """
        logger.info("Creating plot...")
        try:
            # Initialize the plot
            plt.figure(figsize=(12, 6))
            
            # Plot entry and exit prices
            plt.plot(data["Date"], data["Entry Price"], label="Entry Price", marker="o", color="blue")
            plt.plot(data["Date"], data["Exit Price"], label="Exit Price", linestyle="--", color="orange")
            
            # Annotate the phases
            for i, phase in enumerate(data["Phase"]):
                plt.text(data["Date"][i], data["Entry Price"][i] + 0.005, phase, fontsize=10, ha="center")
            
            # Add labels, title, and grid
            plt.title("Trading Data Visualization")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            
            # Display the plot
            plt.show()
            logger.info("Plot successfully created.")
        except Exception as e:
            logger.error("Error during plotting.", exc_info=True)
