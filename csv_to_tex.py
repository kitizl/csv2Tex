#!python3

import pandas as pd
import sys

def import_file(csv_file):
    # this function imports a .csv file as a pandas dataframe
    return pd.read_csv(csv_file,dtype=str)

def convert_file(pd_file):
    # this function converts a pandas dataframe to a latex table
    # adding headers separately
    headers = pd_file.columns
    # this is how the tabular object is made in LaTeX
    begin_str = "\\begin{table} \n \\centering \n\\begin{tabular}{|"+ "c|"*len(pd_file.columns) +"}\n"
    # and this is how the tabular object is terminated
    end_str = "\\end{table}\n \\caption{"+sys.argv[1]+"} \n\\end{tabular}"
    # the headers are the first row of the 'body' of the main table
    main_str = " & ".join(headers) + " \\\\ \n\\hline  \n"
    # the following loop will go through the individual rows of the dataframe and
    # connects the individual elements using '&' (because of LaTeX syntax) and
    # then moves ahead with a \\\\ (making a LaTeX newline) and \n (a newline for
    # ease of reading)
    for line in range(len(pd_file)):
        main_str += " & ".join(pd_file.iloc[line]) + "\\\\ \n\\hline \\\\ \n"
    # the final result is returned as a single string
    return (begin_str + main_str + end_str)

def export_file(string):
    # this function exports a string into a file
    choice = input("Would like this to be saved as a file or just as standard output? (F/O): ")
    if choice=="F":
        fhand = open("table.txt","w")
        fhand.write(string)
    elif choice=="O":
        print(string)
    else:
        print("You have entered an incorrect choice. Please try again.")
        export_file(string)

export_file(convert_file(import_file(sys.argv[1])))
