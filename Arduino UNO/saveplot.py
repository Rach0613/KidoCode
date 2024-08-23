import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#convert txt file to csv file
import csv
import itertools

with open('UNO dat.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = zip(*[lines] * 3)  # Use zip instead of itertools.izip
    with open('log.csv', 'w', newline='') as out_file:  # Add newline='' to avoid extra newlines in the output CSV
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro', 'content'))  # Ensure the header matches the number of columns
        writer.writerows(grouped)

print("converted.")

