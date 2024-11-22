import pandas as pd
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data):
        """
        Initialize the Visualizer with data.
        
        Args:
            data (pd.DataFrame): A pandas DataFrame containing trade data.
        """
        self.data = data

    def detect_phases(self):
        """
        Detect Wyckoff phases based on a rolling mean of 'Entry Price'.
        """
        print("Detecting Wyckoff phases...")
        rolling_mean = self.data["Entry Price"].rolling(window=2).mean()
        self.data.loc[self.data["Entry Price"] < rolling_mean, "Phase"] = "Accumulation"
        self.data.loc[self.data["Entry Price"] > rolling_mean, "Phase"] = "Markup"

    def plot_data(self):
        """
        Visualize the trade data with Wyckoff phases.
        """
        print("Plotting data...")
        plt.figure(figsize=(12, 6))

        # Plot Entry Price as a solid line with markers
        plt.plot(self.data["Date"], self.data["Entry Price"], label="Entry Price", marker="o", color="blue")

        # Plot Exit Price as a dashed line
        plt.plot(self.data["Date"], self.data["Exit Price"], label="Exit Price", linestyle="--", color="orange")

        # Annotate each data point with its detected phase
        for i, phase in enumerate(self.data["Phase"]):
            plt.text(self.data["Date"][i], self.data["Entry Price"][i] + 0.005, phase, fontsize=10, ha="center")

        # Add title and axis labels
        plt.title("Wyckoff Analysis: Entry & Exit Prices with Phases", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Price", fontsize=12)

        # Add legend
        plt.legend()

        # Enable grid for better readability
        plt.grid(True)

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Display the plot
        plt.show()


# Sample data for testing
data = {
    "Date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]),
    "Asset": ["EUR/USD"] * 5,
    "Entry Price": [1.2000, 1.2500, 1.2400, 1.1200, 1.1900],
    "Exit Price": [1.2500, 1.2600, 1.2300, 1.2000, 1.1000],
    "Volume": [100000, 120000, 130000, 140000, 150000],
    "Phase": ["Undefined"] * 5,
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a Visualizer instance and execute the workflow
visualizer = Visualizer(df)
visualizer.detect_phases()  # Detect Wyckoff phases
visualizer.plot_data()  # Plot the data
