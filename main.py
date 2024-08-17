# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# by using with keyword
with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)
    # file.write("\n my roll no is 81")

# I moved to my desktop and tried by accessing in this way the file to open
# C:\Users\avina\PycharmProjects\day24\day24
# ../../../OneDrive./Desktop/my_file.txt
# another way of accessing
# /Users/avina/OneDrive/Desktop/my_file.txt
# this is the way we can access from various relative paths
# C:\Users\avina\OneDrive\Desktop
