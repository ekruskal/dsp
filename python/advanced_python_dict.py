# Q6
import csv


def read_data(data):
    row_list = []
    with open(data) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            row_list.append(row)
    return row_list

faculty = read_data('faculty.csv')
faculty_dict = {}

for i in faculty[1:]:                               # Turns name entry in faculty to (first name, last name)
    run_last = True
    run_first = True
    for x in range(0, len(i[0])):
        if run_last and i[0][len(i[0]) - 1 - x] == ' ':
            run_last = False
            pointer1 = len(i[0]) - x
    for y in range(0, len(i[0])):
        if run_first and i[0][y] == ' ':
            run_first = False
            pointer2 = y
    i[0] = (i[0][:pointer2], i[0][pointer1:])
for i in faculty[1:]:
    add = True
    for j in faculty_dict:
        if i[0][1] == j:
            faculty_dict[j] = [i[1:]] + faculty_dict[j]
            add = False
    if add:
        faculty_dict[i[0][1]] = [i[1:]]

print(faculty_dict)

# Q7
professor_dict = {}
for i in faculty[1:]:                   # I did some additions to the code above for this section to make this simpler
    professor_dict[i[0]] = i[1:]
print(professor_dict)
# Q8                                # A little confused by the question since dictionaries are unsorted by their nature
                                    # So I assumed you meant for the print display to be sorted
sorted_names = sorted(professor_dict, key=lambda name: name[1])

for name in sorted_names:
    print('%s : %s' % (name, professor_dict[name]))
