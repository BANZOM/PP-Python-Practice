# Input the sequence
n = list(map(int, input("Enter the sequence: ").split()))

# Input the frame numbers
f = int(input("Enter the frame number: "))
frame = [0 for i in range(f)]

# Checking of Page Faults
target = -1
page_faults = 0
for item in n:
    if item in frame:
        continue
    else:
        target = (target + 1)%f
        frame[target] = item
        page_faults += 1
        print(frame)
print(page_faults)
