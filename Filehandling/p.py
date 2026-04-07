import pandas as pd# 
marks={
    'aman':66,
    'gita':21,
    'haru':90,
     'aman1':66,
    'gita1':21,
    'haru1':90,
     'aman2':66,
    'gita2':21,
    'haru2':90,
}
data=pd.Series(marks)
print(data['aman'])