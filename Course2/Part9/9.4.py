""" 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer. """


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Creates an empty dictionary
x = dict()

# Loops thru each line within the doc
for line in handle:
    #Skips every line that does not start with "From"
    if not line.startswith("From:"):
        continue

    # Creates a list of the line within the text doc
    line = line.split()
    line = line[1]
    x[line] = x.get(line, 0) + 1

    bigemail = None
    bigcount = None

    for k, v in x.items():
        if bigemail == None or v > bigemail:
            bigcount = k
            bigemail = v
print(bigcount, bigemail)
