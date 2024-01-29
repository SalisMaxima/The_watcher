"""
Summary:
    Date: 29/01/2024
    By: Mathias Herløv Lund
    Version: 1.0
    Description: This program's functions are:
    - Prompting the user to record their weight and automatically recording the date and time of the entry.
    - Saving this data in two separate .txt files (weights.txt and dates.txt).
    - If previous data (in weights.txt and dates.txt) is present, then the script appends the new results to these files.
"""

# Importing necessary modulesy
import datetime
import os
import numpy as np

# Checking if the .txt files exist and creating them if they don't
if not os.path.exists("weights.txt"):
    open("weights.txt", "w+").close()

if not os.path.exists("dates.txt"):
    open("dates.txt", "w+").close()

# Check if dates.txt is not empty and load data
if os.stat("dates.txt").st_size > 0:
    with open("dates.txt", "r") as file:
        dates = file.readlines()
        dates = [date.strip() for date in dates]  # Stripping newline characters

    # Displaying the last entry if available
    if dates:
        print("Last entry: " + dates[-1])
    else:
        print("No entries found in dates.txt")

    # Asking user for consent to proceed
    while True:
        proceed = input("Do you want to proceed? (y/n): ")
        if proceed.lower() == "y":
            break
        elif proceed.lower() == "n":
            exit()
        else:
            print("Please enter y or n")

# Preparing to record new data
date = datetime.datetime.now().strftime("%d/%m/%Y")  # Current date in dd/mm/yyyy format
weight = 0  # Initializing weight

# Loading existing data from files
weights = np.loadtxt("weights.txt", dtype=float)
dates = np.loadtxt("dates.txt", dtype=str)

# Prompting user to enter their weight
while True:
    try:
        weight = float(input("Please enter your weight: "))
        break
    except ValueError:
        print("Please enter a number")

# Appending new data to arrays
weights = np.append(weights, weight)
dates = np.append(dates, date)

# Saving updated arrays to .txt files
np.savetxt("weights.txt", weights, fmt="%s")
np.savetxt("dates.txt", dates, fmt="%s")
