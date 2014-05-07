#!/usr/bin/env python

import pandas as pd
import os

COLUMNS = [
    'fdntext',
    'fldimp',
    'undrfld',
    'advknow',
    'pubpol',
    'comimp',
    'undrwr',
    'undrsoc',
    'orgimp',
    'undrorg']

base_dir = os.path.join(os.path.dirname(__file__), "..")

df = pd.read_csv(os.path.join(base_dir, 'input', 'xl.csv'), usecols=COLUMNS,
                 na_values=['77', '88'])

mean = df.groupby('fdntext').mean()

# Task 1: Output mean
mean.to_csv(os.path.join(base_dir, 'output', 'mean.csv'))

# Task 2: Output stats
mean.describe().to_csv(os.path.join(base_dir, 'output', 'stats.csv'))
