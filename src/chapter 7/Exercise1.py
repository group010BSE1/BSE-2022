fhandle = open("mbox-short.txt")
for line in fhandle:
    print(line.upper().rstrip())