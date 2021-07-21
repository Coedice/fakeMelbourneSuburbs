import csv
import random

real_suburbs = []
fake_suburbs_displayed = int(input("How many fake suburbs would you like to see?: "))

with open("suburbs.csv") as csvfile:
    reader = csv.reader(csvfile)
    suburbs = []

    for row in reader:
        suburbs += [row]

    for suburb in suburbs:
        # TODO: Make sure the spaces are removed before assessment of sameness
        real_suburbs += ["{} {}{}{} {}".format(suburb[1], suburb[2], suburb[3], suburb[5], suburb[5])]

def new_suburb():
    def aux_new_suburb():
        # Get random suburb indices for each of the 5 fields
        indices = []

        for _ in range(6):
            indices += [random.randrange(0, len(suburbs))]

        # Construct new suburb name
        pre_word = suburbs[indices[0]][1]
        prefix = suburbs[indices[1]][2]
        stem = suburbs[indices[2]][3]
        suffix = suburbs[indices[3]][4]
        after_word = suburbs[indices[4]][5]

        # Check if stem is not empty
        if stem == "":
            return aux_new_suburb()

        # Check if one of pre_word, prefix, suffix, and after_word are not empty
        if pre_word + prefix + suffix + after_word == "":
            return aux_new_suburb()

        generated_suburb = "{} {}{}{} {}".format(pre_word, prefix, stem, suffix, after_word)

        # Check if new suburb is a real suburb
        for real_suburb in real_suburbs:
            if generated_suburb == real_suburb:
                return aux_new_suburb()

        return generated_suburb, indices

    # Make output
    new_sub = aux_new_suburb()
    output = new_sub[0].strip().title() + "\n\tFrom: "
    indices = new_sub[1]

    for i in range(5):
        if suburbs[indices[i]][i + 1] != "":
            output += suburbs[indices[i]][0].title() + ", "

    return output[:-2]


for i in range(1, fake_suburbs_displayed + 1):
    print("{}) {}".format(i, new_suburb()))
