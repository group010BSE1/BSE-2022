file_name = input("Enter the file name: ")
if file_name == "na na boo boo":
        print("na na boo boo to you".upper(), "- You have been punk'd!")
        quit()
try:
    fhandle = open(file_name)
except:
    print(f"File cannot be opened: {file_name}")
    exit()
    
fhandle = open(file_name)
count = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence"):
        count += 1
print(f"There were {count} subject lines in {file_name}")