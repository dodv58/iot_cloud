import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#====================================================================
#Generate a DataFrame from an input array
def generate_barchart_input(array, classes, types):
  conv_arr = []
  for i in range(len(classes)):
    for j in range(len(types)):
      row = [classes[i], types[j], array[i][j]]
      conv_arr.append(row)

  return pd.DataFrame(conv_arr, columns = ['class', 'type', 'value'])
#====================================================================

exam_arr = [[1, 2], [3, 4], [5, 6]]
classes = ['a', 'b', 'c']
types = ['col_1', 'col_2']

df = generate_barchart_input(exam_arr, classes, types)

#g = sns.factorplot(x='class', y='value', hue='type', data=df, kind='bar')
g = sns.barplot(x='class', y='value', hue='type', data=df)
plt.show()
