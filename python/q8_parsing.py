#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv


def read_data(data):
    row_list = []
    with open(data) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            row_list.append(row)
            print(row)
    return row_list


def get_min_score_difference(parsed_data):
    total = []
    del parsed_data[0]
    for i in parsed_data:
        total.append((abs(int(i[5]) - int(i[6]))))
    return min(total)


def get_team(index_value, parsed_data):
    teams = []
    del parsed_data[0]
    for i in parsed_data:
        if abs(int(i[5]) - int(i[6])) == index_value:
            teams.append(i[0])
    return teams

