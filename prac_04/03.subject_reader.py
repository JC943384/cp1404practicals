"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()


main()

def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                data.append(parts)
    return data
print()
print("This is task 2")
# Example usage
filename = 'subject_data.txt'
data_list = get_data(filename)
print(data_list)


print()
print("This is task3:")
def display_subject_details():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        major = parts[0]
        instructor = parts[1]
        num_student = parts[2]

        print(f"{major} is taught by {instructor} and has {num_student} students")


display_subject_details()











