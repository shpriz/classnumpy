import matplotlib.pyplot as plt
import pandas as pd

all_data = pd.read_csv('creditcard.csv', index_col=0)

counts = all_data['Class'].value_counts()

print(counts)

plt.style.use('fivethirtyeight')

plt.subplot(211)
plt.title('График Class')
counts.plot(kind='barh')

plt.subplot(212)
plt.title('График LOG(Class)')
counts.plot(kind='barh', logx=True)

plt.figure(figsize=[8, 6])

class0 = all_data.loc[all_data['Class'] == 0, ['V1']]
class1 = all_data.loc[all_data['Class'] == 1, ['V1']]

plt.hist(class0['V1'], bins=20, density=True, alpha=0.5, label='Class 0', color='grey')
plt.hist(class1['V1'], bins=20, density=True, alpha=0.5, label='Class 1', color='red')
plt.legend()

plt.show()

