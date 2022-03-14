file_name = input("Enter the file name: ")
try:
    fhandle = open(file_name)
except:
    print("File not found")
    exit()

fhandle = open(file_name)
count = 0
total_floatPoint = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find("0")
        fpoint_number = float(line[index:])
        total_floatPoint = total_floatPoint + fpoint_number
        count += 1

print(f"Average spam confidence: {total_floatPoint/count}")