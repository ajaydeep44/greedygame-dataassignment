import pandas as pd
import datetime
df = pd.read_csv('session1.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
st_time=[]
en_time=[]
game=[]
count=1
b=0
c=0

for i in range(len(df)-1):
    row1, row2 = df.iloc[i], df.iloc[i+1]
    if (row1['event'] == 'ggstart' and row2['event']== 'ggstop'):
                 if row2['timestamp']- row1['timestamp'] >datetime.timedelta(seconds=30) and i%2 !=0: 
                    st_time.append(row2['timestamp']- row1['timestamp'])               
                    
                 elif row2['timestamp']- row1['timestamp'] <= datetime.timedelta(seconds=30) and i%2 ==0:
                    en_time.append(row2['timestamp']- row1['timestamp'])
                    
                 elif row2['timestamp']-row1['timestamp'] > datetime.timedelta(seconds=30) and i%2 ==0:
                    b = sum(st_time)
                    c = sum(en_time)
                    game.append(b-c)
                    count += 1
    else:
	    break
		
print('Total number of Sessions')          
print count
print('Per session time spent ')
print game


