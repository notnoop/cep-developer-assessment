#!/usr/bin/env python

import pandas as pd
import os
import json

base_dir = os.path.join(os.path.dirname(__file__), "..")

mean = pd.read_csv(os.path.join(base_dir, 'input', 'mean.csv'), index_col='fdntext')
stats = pd.read_csv(os.path.join(base_dir, 'input', 'stats.csv'), index_col=0)
pct = pd.read_csv(os.path.join(base_dir, 'input', 'pct.csv'), index_col='fdntext')

def percentile_chart(client, metric):
    return {'type': 'percentileChart',
            'absolutes': stats[metric][['min', '25%', '50%', '75%', 'max']].tolist(),
            'current': {
                'name': '2014',
                'value': mean[metric][client],
                'percentile': pct[metric][client]},
            'cohorts': [],
            'past_results': [],
            'segmentations': []}

def report(client):
    return {'name': '%s Report' % client,
            'title': '%s Report' % client,
            'cohorts': [],
            'segmentations': [],
            'elements': {v: percentile_chart(client, v) for v in mean.columns}}

def reports(clients):
    return {'version': '1.0',
            'reports': [report(c) for c in clients]}

r = reports(['Tremont 14S'])
with open(os.path.join(base_dir, 'output', 'output.json'), 'w') as fout:
    json.dump(r, fout, indent=4)
