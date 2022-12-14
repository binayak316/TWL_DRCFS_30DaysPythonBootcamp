'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''

def read_file(filename):

    # # TODO: Open the file in read-only mode and read its contents. Return the contents of the file.
    # pass
    contents = open('/home/commando/PycharmProjects/python bootcamp/TWL_DRCFS_30DaysPythonBootcamp/Week 2/Assignments/' + filename , 'r')
    contents = contents.read()
    return contents


contents = read_file('my_file.txt')
print(contents)  # Output: "Hello, world!\nI just did my first Assignment of week 2."

