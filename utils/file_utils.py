from typing import List
from pandas import read_excel, read_csv

def read_xls(filename: str) -> List[str]:
    """
    Reads the excel file into a pandas dataframe and returns a list of names.
    """
    names = []
    excel = read_excel(filename)
    print("printing dataframe: ", excel)
    for row in excel.itertuples():
        names.append(row[1]) #Append the name to the names list
    return names

