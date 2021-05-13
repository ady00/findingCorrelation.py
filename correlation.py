
import plotly.express as px

import numpy as np
import csv



def plotMaker(data_path):
    
    with open(data_path) as csv_file:
        
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def DataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    
    return {"x" : marks_in_percentage, "y": days_present}




def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])








def create():
    data_path  = "./data/studentMarksDaysPresent.csv"    #this is the data file, you can change this value depending on what you named your csv file as 

    datasource = DataSource(data_path)
    findCorrelation(datasource)
    
    (data_path)

create()
