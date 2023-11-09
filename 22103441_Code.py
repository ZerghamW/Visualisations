"""
Author: Muhammad Zergham
Date: 05/11/2023

Title: Pakistan Intellectual Capital

Description: This is the code generation for visualisations for our academic assignment

This is for different matplotlib graphs, bar, box, histogram and pie chart

"""
# Importing the necessery libraries

import numpy as np # For arthemetic operations.
import pandas as pd # For Data analysis, wrangling, and Exploration
import matplotlib.pyplot as plt # For Data Visualisations

# Reading the Csv file
def read_dataset(data_file):
    """
    Reading Pakistan intellectual Capital Dataset from internal storage.
    Parem: data_file
    Return: Data File as loaded file
    """
    return pd.read_csv(data_file, encoding="latin1")

# Renaming the columns as these are not in usefull name formate
def rename_columns(data1):
    """
    Rename columns in the DataFrame.
    """
    renamed_col = {
        "Teacher Name": "Teacher_Name",
        "University Currently Teaching": "University_Currently_Teaching",
        "Province University Located": "Province_of_University",
        "Terminal Degree": "Terminal_Degree",
        "Graduated from": "Graduated_from",
        "Area of Specialization/Research Interests": "Specialization",
        "Other Information": "Other_Information"
    }
    data1.rename(columns=renamed_col, inplace=True)


# As our main focus is on specialisations so we focus on cleaning this.
def clean_specialization(data1):
    """
    Clean the 'Specialization' column by capitalizing and stripping whitespace.
    """
    data1["Specialization"] = data1["Specialization"].str.capitalize()
    data1["Specialization"] = data1["Specialization"].str.strip()

def plot_top_specializations(data1):
    """
    Plot a bar chart and a pie chart for the top 10 specializations in Pakistan.
    """
    specialization = data1["Specialization"].value_counts()
    plotting = specialization.head(10)

    # Bar Plot
    plt.figure(figsize=(10, 6))
    plotting.plot(kind='bar')
    plt.title("Top 10 Specializations in Pakistan")
    plt.xlabel("Specialization")
    plt.ylabel("Number of Teachers")
    plt.xticks(rotation=45)
    plt.show()

    # Pie Chart
    plt.figure(figsize=(8, 8))
    plotting.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Top 10 Specializations in Pakistan")
    plt.ylabel("")
    plt.show()

# Ploting Histogram
def plot_histogram_specialization(data1):
    """
    Plot a histogram of specialization counts.
    """
    specialization = data1["Specialization"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.hist(specialization, bins=10, edgecolor='k')
    plt.title("Histogram of Specialization Counts")
    plt.xlabel("Count")
    plt.ylabel("Frequency")
    plt.show()

def plot_boxplot_specialization(data1):
    """
    Plot a box plot of specialization counts.
    """
    specialization = data1["Specialization"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.boxplot(specialization, vert=False)
    plt.title("Box Plot of Specialization Counts")
    plt.xlabel("Count")
    plt.show()

def plot_scatter_specialization(data1):
    """
    Plot a scatter plot of the top 10 specializations.
    """
    specialization = data1["Specialization"].value_counts()
    plotting = specialization.head(10)

    plt.figure(figsize=(10, 6))
    plt.scatter(plotting.index, plotting.values)
    plt.title("Scatter Plot of Top 10 Specializations")
    plt.xlabel("Specialization")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

def main():
    data_file = "Pakistan Intellectual Capital - Computer Science - Ver 1.csv"
    data1 = read_dataset(data_file)
    rename_columns(data1)
    clean_specialization(data1)
    
    plot_top_specializations(data1)
    plot_histogram_specialization(data1)
    plot_boxplot_specialization(data1)
    plot_scatter_specialization(data1)

if __name__ == "__main__":
    main()
