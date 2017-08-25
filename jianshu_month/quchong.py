import pandas as pd


csvfile='Month.csv'
file=pd.read_csv(csvfile,header=0,encoding='utf-8',)
dateList=file.drop_duplicates()
dateList.to_csv(csvfile)