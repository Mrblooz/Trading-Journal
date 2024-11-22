import pandas as pd
from tools.visualization import Visualizer

def test_plot_data(mocker):
    visualizer = Visualizer()
    test_data = pd.DataFrame({
        "Date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "Entry Price": [1.2000, 1.2500],
        "Exit Price": [1.2500, 1.2600],
        "Phase": ["Accumulation", "Markup"]
    })

    # Mock the plt.show() method to prevent rendering during tests
    mocker.patch("matplotlib.pyplot.show")

    # Run the plot method
    visualizer.plot_data(test_data)

    # If no exceptions are raised, the test passes
