import pandas as pd

arr = []
columns = ['사은품명','가격', 'URL']
arr.append(['rtx 3080', '100000', 'asdf'])
df = pd.DataFrame(arr, column=columns)
print(df)