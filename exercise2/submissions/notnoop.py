#!/usr/bin/env python

import pandas as pd
from scipy.stats import percentileofscore
import os

base_dir = os.path.join(os.path.dirname(__file__), "..")

mean = pd.read_csv(os.path.join(base_dir, 'input', 'mean.csv'), index_col='fdntext')

def percentile(items):
    return [percentileofscore(items, i, kind='mean') for i in items]

pct = mean.apply(percentile, axis=0)  # axis=0 i.e. across column
pct.to_csv(os.path.join(base_dir, 'output', 'pct.csv'))
