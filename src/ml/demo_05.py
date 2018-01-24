
import pandas as pd
df = pd.read_csv(r'C:\Users\daijitao\Downloads\smsspamcollection\SMSSpamCollection.csv',
                 delimiter='\t', header=None)

print(df.head())
print('含spam短信数量：', df[df[0] == 'spam'][0].count())
print('含ham短信数量：', df[df[0] == 'ham'][0].count())