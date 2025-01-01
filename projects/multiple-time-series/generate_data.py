from pathlib import Path
import numpy as np
import pandas as pd


for i in range(10):
    np.random.seed(i)
    data = np.random.randn(365 * 24)
    
    path = Path(__file__).parent / f'data/data_{i}.csv'

    times = pd.date_range(start='2020-01-01', periods=365 * 24, freq='h')
    df = pd.DataFrame(data, index=times, columns=['value'])
    df.index.name = 'time'

    df.to_csv(path)


with open(Path(__file__).parent / 'data/files.txt', 'w') as f:
    for i in range(10):
        f.write(f'data_{i}.csv\n')