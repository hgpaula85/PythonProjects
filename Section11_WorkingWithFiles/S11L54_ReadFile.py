"""
File I/O
Reading a file -> .read()
Reading line by line -> .readline()
"""

my_file = open("secondfile.txt", "r")

print("---", "Entire file", "-"*10)
print(str(my_file.read()))
my_file.close()

print("\n", "---", "Line by line", "-"*10)
my_file_line = open("secondfile.txt", "r")
print(str(my_file_line.readline()))
my_file_line.close()