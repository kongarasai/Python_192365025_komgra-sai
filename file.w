def write_list_to_file(strings, filename):
    with open(filename, 'w') as file:
        for string in strings:
            file.write(string + '\n')
my_strings = ["Hello", "World", "Python", "Programming"]
y=write_list_to_file(my_strings, "output.txt")
