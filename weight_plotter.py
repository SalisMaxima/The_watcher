"""
Summary:
Date: 29/01/2024
Author: Mathias Herløv Lund
Version: 1.0
Description: This script aims to load data generated by weight_recorder in the form of dates.txt and weights.txt, and plot the data.
Input: dates.txt and weights.txt
Format of dates: date.strftime("%d/%m/%Y")
Format of weights: float
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import os
import sys

def main():
    if not os.path.exists("weights.txt") or not os.path.exists("dates.txt"):
        print("Data files not found.")
        sys.exit()

    # Load data
    try:
        dates = np.loadtxt("dates.txt", dtype=str, ndmin=1)
        weights = np.loadtxt("weights.txt", ndmin=1)
    except:
        print("Error loading data files.")
        sys.exit()

    # Check if data is correctly loaded by printing
    print("Dates loaded:", dates)
    print("Weights loaded:", weights)

    # Convert dates to datetime objects and check for errors
    try:
        dates = [datetime.datetime.strptime(date, "%d/%m/%Y") for date in dates]
    except ValueError as e:
        print(f"Error in date conversion: {e}")
        sys.exit()

    # Convert dates to matplotlib dates
    dates = mdates.date2num(dates)

    # Plot data
    fig, ax = plt.subplots()
    ax.plot_date(dates, weights, linestyle='-', marker='o', color='red', markersize=8)  # Set marker and color

    # Set the x-axis to span a few days before and after the data range
    if len(dates) > 0:  # Check if there are any dates
        first_date = mdates.num2date(min(dates)) - datetime.timedelta(days=3)  # 3 days before the first data point
        last_date = mdates.num2date(max(dates)) + datetime.timedelta(days=3)   # 3 days after the last data point

        # Convert back to matplotlib date format for plotting
        first_date = mdates.date2num(first_date)
        last_date = mdates.date2num(last_date)

        ax.set_xlim(first_date, last_date)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
    ax.xaxis.set_tick_params(rotation=30)
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight [kg]")
    ax.set_title("Weight over time")
    ax.grid(True)
    plt.tight_layout()
    plt.savefig("weight_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
