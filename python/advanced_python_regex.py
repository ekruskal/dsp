import csv


def read_data(data):
    row_list = []
    with open(data) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            row_list.append(row)
    return row_list

faculty = read_data('faculty.csv')
# Q1, Q2, Q3, and Q4
degree_total = []
title_total = []
email_addresses = []

for i in faculty:
    degree_total.append(i[1])
    title_total.append(i[2])
    email_addresses.append(i[3])

degree_total = degree_total[1:]                     # remove title
title_total = title_total[1:]
email_addresses = email_addresses[1:]


new_degree_total = []
for degree in degree_total:                         # remove periods and add spaces in first spot
    new_degree = degree.replace('.', '')
    if new_degree[0] != ' ':
        new_degree = ' ' + new_degree
    new_degree_total.append(new_degree)


newest_degree_total = []
for degree in new_degree_total:                     # split up person's many degrees into individual degrees
    pointers = []
    for i in range(0, len(degree)):
        if degree[i] == ' ':
            pointers.append(i)
    pointers.append(len(degree))
    pointers = sorted(pointers)
    for j in range(0, len(pointers)):
        if pointers[j] != len(degree):
            newest_degree_total.append(degree[pointers[j]+ 1:pointers[j+1]])


print(newest_degree_total)


def frequency(x):
    frequency_dict = {}
    for i in x:
        add = True
        for j in frequency_dict:
            if i.lower() == j.lower():
                frequency_dict[j] += 1
                add = False
        if add and i != '0':
            frequency_dict[i] = 1
    return frequency_dict

print(frequency(newest_degree_total))        # Q1 answer
print(frequency(title_total))                # Q2 answer
print(email_addresses)                       # Q3 answer

domains = []
for email_address in email_addresses:
    counter = 0
    for i in range(0, len(email_address) - 1):
        if email_address[i] == '@':
            counter = i + 1
    domains.append(email_address[counter:])

print(sorted(frequency(domains)))            # Q4 answer

