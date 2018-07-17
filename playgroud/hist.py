import pandas as pd
import matplotlib.pyplot as plt


csv_data = pd.read_csv('sample.csv')
csv_data['database'].plot('hist')
