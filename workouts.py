import csv
import pandas as pd

# read csv
def read_csv(file):
    method = int(input('Enter 1 or 2: '))
    if method == 1:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for r in reader:
                print(r)
    elif method == 2:
        dataframe = pd.read_csv(file)
        print(dataframe)
    else:
        return 0
    
    return 1

# Print data from .txt file
def read_txt(file):
    if '.txt' not in file:
        return 0
    with open(file, 'r') as f:
        for line in f:
            print(line)

# Create a list of data from rows in a dataframe      
def csv_to_txt(file='workout.csv'):
    if '.csv' not in file:
        return 0
    
    df = pd.read_csv(file)

    #sets = [col for col in df.columns if 'Set' in col]
    cols = [col for col in df.columns]
    myfile = input('Enter file name, if no file one will be created: ')

    with open(myfile, 'a') as f:
        for set in df[cols].values:
            f.write(str(set))
            f.write('\n')

        print(myfile, 'closed')        


    return 1




