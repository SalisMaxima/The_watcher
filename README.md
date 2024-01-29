```markdown
# Weight Tracker Analysis

## Overview
This repository contains a set of Python scripts designed for tracking and analyzing weight data. Developed by Mathias Herløv Lund, these scripts enable users to record their weight, visualize weight trends over time, and perform statistical and regression analysis.

### Scripts
1. `weight_recorder.py` - Records user's weight and the current date.
2. `weight_plotter.py` - Plots the recorded weight data over time.
3. `weight_analyzer.py` - Analyzes the data by performing linear and polynomial regression, and calculates basic statistics.

## Setup
To run these scripts, ensure you have Python installed along with the following libraries:
- numpy
- matplotlib
- scipy
- datetime

You can install these libraries using pip:
```bash
pip install numpy matplotlib scipy
```

## Usage

### Recording Weight Data
Run `weight_recorder.py` to input your weight. The script saves the weight and the corresponding date into `weights.txt` and `dates.txt`.

```bash
python weight_recorder.py
```

### Plotting Weight Data
Execute `weight_plotter.py` to visualize your weight data over time. This script reads the data and generates a plot showing the weight trend.

```bash
python weight_plotter.py
```

### Analyzing Weight Data
Use `weight_analyzer.py` for detailed analysis. It performs linear and polynomial regression on your data and computes statistics such as mean, median, and standard deviation.

```bash
python weight_analyzer.py
```

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or suggestions, feel free to contact [Mathias Herløv Lund](mathiaslundmobil@gmail.com).
```

