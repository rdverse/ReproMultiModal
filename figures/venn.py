import numpy as np
import pandas as pd
import matplotlib_venn as vplt

x = np.random.randint(2, size=(10, 3))
df = pd.DataFrame(x, columns=['A', 'B', 'C'])
print(df)
v = vplt.venn3(subsets=(1, 1, 1, 1, 1, 1, 1))

df = pd.DataFrame([[1, 1], [1, 0], [0, 1], [0, 0]], columns=['A', 'B'])

sets = [set(np.argwhere(v).ravel()) for k, v in df.items()]
venn3(sets, df.columns)
plt.show()
