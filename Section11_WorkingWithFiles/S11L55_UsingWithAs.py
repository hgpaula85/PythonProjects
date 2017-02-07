"""
With / As keywords
"""

#print("Normal Write Start")
#my_write = open("thirdfile.txt", "w")
#my_write.write("Trying to write to the file")
#my_write.close()

#print("Normal Read Start")
#my_read = open("thirdfile.txt", "r")
# print(str(my_read()))

print("With As write start")
with open("thirdfile.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read")

print("\n", "With As read start")
with open("thirdfile.txt", "r") as with_as_read:
    print(str(with_as_read.read()))