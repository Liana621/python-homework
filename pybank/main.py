
# Import the pathlib and csv library
from pathlib import Path
import csv

#Set Path
csvpath = Path('.../Resources/budget_data.csv')
C:\Users\Owner\Desktop\Trilogy\CU-NYC-FIN-PT-08-2019-U-C\02-Homework\02-Python\Instructions\PyBank\Resources
    
# variable to hold coloums
info_given = []


# Initialize line_num variable
line_num = 0



print(f"Current Working Directory: {Path.cwd()}"
  
with open(csvpath, 'r') as csvfile:

    # Print the datatype of the file object
    print(type(csvfile))

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader))      
      
      
###All other info uploaded pushed before this last one were trial &errors. I added alllll lines of notebook here that worked and now below information has correct codes/answers to HW!      
      
#This works to print info in csv      
import pandas as pd

df = pd.read_csv (r'C:\Users\Owner\Desktop\Trilogy\CU-NYC-FIN-PT-08-2019-U-C\02-Homework\02-Python\Instructions\PyBank\Resources\budget_data.csv')
print (df)
      
      
#NOW WE ARE GETTING SOMEWHERE***************************************************
import pandas as pd
from pathlib import Path

#set path
csvpath = Path('budget_data.csv')
      

#Read & see
budgetfile = pd.read_csv(csvpath)
budgetfile.head()      
      
#Rename 2 make easier to type& View
budgetfile = budgetfile.rename(columns={
   "Date":"date",
   "Profit/Losses":"profit_losses"})
budgetfile.head()

#Make Calculations on CSV!!!!!
budgetfile['profit_losses'].max()

#The total number of months included in the dataset
budgetfile['date'].count()

TotalMonths = budgetfile['date'].count()

#Net Value of Profit Losses Coloum
budgetfile['profit_losses'].sum()

NetPnL = budgetfile['profit_losses'].sum()
      
#Mean of the above
budgetfile['profit_losses'].mean()
      
#Changes to the PNL
budgetfile['profit_losses'].sum()
budgetfile['pnl_changes'] = budgetfile['profit_losses']-budgetfile['profit_losses'].shift()
      
coloum = (budgetfile['profit_losses']-budgetfile['profit_losses'].shift())

coloum.mean()
      
AvgPnL = coloum.mean()

      
max_change = budgetfile['pnl_changes'].max()
print(max_change)

budgetfile.loc[budgetfile["pnl_changes"] == budgetfile["pnl_changes"].max(),'date']

min_change = budgetfile['pnl_changes'].min()

budgetfile.loc[budgetfile["pnl_changes"] == budgetfile["pnl_changes"].min(),'date']

#Print Answers
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetPnL}")
print(f"Average Change: ${AvgPnL}")
print(f"Greatest incraese in profits Feb: 2012  $({max_change})")
print(f"Greatest Decrease in Loss: Sep-2013 $({min_change})")
      
      
#All ACTUAL NEW CodeS That WORK

import pandas as pd
from pathlib import Path
      
csvpath = Path('budget_data.csv')

budgetfile = pd.read_csv(csvpath)
budgetfile.head()

budgetfile = budgetfile.rename(columns={
   "Date":"date",
   "Profit/Losses":"profit_losses"})
budgetfile.head()

budgetfile['profit_losses'].max()

budgetfile['date'].count()
      
TotalMonths = budgetfile['date'].count()

TotalMonths = budgetfile['date'].count()

budgetfile['profit_losses'].sum()
      
NetPnL = budgetfile['profit_losses'].sum()
      
budgetfile['profit_losses'].mean()

budgetfile['profit_losses'].sum()
budgetfile['pnl_changes'] = budgetfile['profit_losses']-budgetfile['profit_losses'].shift()
      
budgetfile

#Add new coloum
coloum = (budgetfile['profit_losses']-budgetfile['profit_losses'].shift())

#Average of new
coloum.mean()

#Set Above as a variable
AvgPnL = coloum.mean()
      
#4
max_change = budgetfile['pnl_changes'].max()
print(max_change)

#Find the location of the Max
budgetfile.loc[budgetfile["pnl_changes"] == budgetfile["pnl_changes"].max(),'date']

#5
min_change = budgetfile['pnl_changes'].min()
print(min_change)

#Find location of the Min
budgetfile.loc[budgetfile["pnl_changes"] == budgetfile["pnl_changes"].min(),'date']
      
#HW Final answer!!!!!!!!!!!!!!!
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetPnL}")
print(f"Average Change: ${AvgPnL}")
print(f"Greatest incraese in profits Feb: 2012  $({max_change})")
print(f"Greatest Decrease in Loss: Sep-2013 $({min_change})")    

      

      

      

      
      

      

      
