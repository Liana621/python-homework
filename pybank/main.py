
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

#Net Value of Profit Losses Coloum
budgetfile['profit_losses'].sum()
      
#Mean of the above
budgetfile['profit_losses'].mean()
      
#Changes to the PNL
budgetfile['profit_losses'].sum()
budgetfile['pnl_changes'] = budgetfile['profit_losses']-budgetfile['profit_losses'].shift()
      
coloum = (budgetfile['profit_losses']-budgetfile['profit_losses'].shift())

coloum.mean()
      

      

      

      
      

      

      
