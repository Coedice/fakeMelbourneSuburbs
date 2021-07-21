import csv

with open("suburbs.csv") as csvfile:
    reader = csv.reader(csvfile)
    suburbs = []

    for row in reader:
        suburbs += [row]

    parts = [""]*5

    for suburb in suburbs:
        for part_index in range(5):
            if len(suburb[part_index + 1]) > len(parts[part_index]):
                parts[part_index] = suburb[part_index + 1]

longest_fake_suburb = "{} {}{}{} {}".format(parts[0], parts[1], parts[2], parts[3], parts[4]).title()

print(longest_fake_suburb)
