name = input("Enter filename: ")
if len(name) < 1:
    name = "para.txt"

fhand = open(name)
di = dict()

for line in fhand:
    line.rstrip()
    words = line.split()

    for w in words:
        di[w] = di.get(w, 0) + 1

        largestwrd = None
        count = None

        for k, v in di.items():
            if largestwrd == None or v > count:
                count = (k)
                largestwrd = v




    print(largestwrd, count)
