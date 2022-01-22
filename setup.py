import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_files:
        df = csv.DictReader(csv_files)
        fig = px.scatter(df, x="Days Present", y = "Marks In Percentage" )
        fig.show()

def getSourceObject(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x":marks_in_percentage,"y":days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("The Correlation between Marks In Percentage and Days Present is :- \n--->",correlation[0,1])

def setup():
    data_path: r'C:\Users\HP\Downloads\finding-correlation-master\Project 106\Student Marks vs Days Present.csv'

    getSourceObject(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()