#DataFrames

import numpy as np
import pandas as pd

data = {
    'ciudad' : ['Caracas', 'Guadalajara', 'La Habana', 'Cancun'],
    'poblacion' : [1000000, 2000000, 400000, 11000000],
    'infectado' : [6000, 4000, 7000, 120000]
}

df = pd.DataFrame(data)
print(f"\n{df}")
print(f"\n{df.columns}")
print(f"\n{df['ciudad']}")
print(f"\n{df.dtypes}")
