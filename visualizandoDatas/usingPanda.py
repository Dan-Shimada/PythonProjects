import matplotlib.pyplot as plt
import pandas as pd

'''
data = [{'name':'nick',
         'jan_ir':124,
         'feb_ir': 100,
         'march_ir': 165},
        {'name': 'panda',
         'jan_ir':112,
         'feb_ir':143,
         'march_ir':3},
        {'name': 'panda',
         'jan_ir':112,
         'feb_ir':143,
         'march_ir':3},
        {'name': 'panda',
         'jan_ir':112,
         'feb_ir':143,
         'march_ir':3}]
'''

raw_data = {'names':['nick', 'panda', 's', 'Ari', 'Valos'],
            'jan_ir': [13, 122, 101, 106, 365],
            'feb_ir': [122, 132, 144, 98, 62],
            'march_ir': [65, 88, 12, 32, 65]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['march_ir']
color = [(1, .4, .4), (1, .6, 1), (.5, .3, 1), (.3, 1, .5), (.7, .7, .2)]
plt.pie(df['total_ir'], labels=df['names'], colors=color, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
print(df)