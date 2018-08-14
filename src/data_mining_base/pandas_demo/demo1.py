
import pandas as pd

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print("data::\n", data)

print('loc::\n', data.loc[1:3])


area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})

data = pd.DataFrame({'area':area, 'pop':pop})
print(data)

print(data.values)
print(type(data.values))
print(data.values[0])
print(data.iloc[:3, :2])
print(data.iloc[0, 1])
