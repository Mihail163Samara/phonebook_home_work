'''Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Надо это сделать без get_dummieНs'''


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})

df.loc[df['whoAmI']=='robot',['robot']] = '1'
df.loc[df['whoAmI']!='robot',['robot']] = '0'
df.loc[df['whoAmI']=='human',['human']] = '1'
df.loc[df['whoAmI']!='human',['human']] = '0'

print(df)