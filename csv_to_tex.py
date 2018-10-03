#!python3

import pandas as pd
import sys

def import_file(csv_file):
	return pd.read_csv(csv_file)

def write_table(pd_file):
	headers = " & ".join(pd_file.columns) + "\\\\\n"
	data = ""
	for i in range(len(pd_file)):
		data += " & ".join(pd_file.columns) + "\\\\\n \\hline \\\\"
	return "\\begin\{tabular\}\[" + "\|c\|"*len(pd_file.columns) + "\] \n\n \\hline" + headers + data + "\\\\ \n  \end\{tabular\}"

def export_file(string):
	with fhand as open("table.txt",'w'):
		fhand.write(string)

export_file(write_table(import_file(sys.argv[1])))