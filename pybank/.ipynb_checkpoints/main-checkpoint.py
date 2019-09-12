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
      
      