"""
	This file contains most of the constant global variables that can be accessed
	with other programs.
"""

import pandas as pd
import calendar


'''
    After importing and skewing unwanted data,
    rows are dailies
    columns are date, subtotal, ticket discount, and gift sale
'''

# hardcoded file paths for each year summary
files = []
files.append("../reports2020/totalSalesSummary2020.xlsx")
files.append("../reports2021/totalSalesSummary2021.xlsx")
files.append("totalSalesSummary2022.xlsx")

# table is an array of an arrray; 
# yearly array of dates ranging from 1/1/2020 - 1/1/2030
table = []

for i in range(2020,2031):
    start = "1/1/" + str(i)
    end = "12/31/" + str(i)
    t = pd.date_range(start=start, end=end)
    table.append(t)

# this table is used for sharing data from multiple years
# xtable is days of the leap year without actual year. 
# used during plotting to plot multiple years
xDailyTable = []

oddMonths = ["January", "March", "May", "July", "August", "October", "December"]
evenMonths = ["April", "June", "September", "November"]

for month in calendar.month_name[1:]:
    if month in oddMonths:
        for days in range(1,32):
            xDailyTable.append(month + " " + str(days))
    elif month in evenMonths:
        for days in range(1,31):
            xDailyTable.append(month + " " + str(days))
    else:
        for days in range(1,30):
            xDailyTable.append(month + " " + str(days))
                  