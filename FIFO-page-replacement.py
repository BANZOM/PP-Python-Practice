# Input the sequence
sequence = list(map(int, input("Enter the sequence: ").split()))

# Input the frame number
frame_size = int(input("Enter the frame number: "))
frame = [0] * frame_size

# Initialize variables for page faults
page_faults = 0
frame_index = 0

# Function to check if a page is in the frame
def is_page_in_frame(page, frame):
    return page in frame

# Main loop to check for page faults
for page in sequence:
    if is_page_in_frame(page, frame):
        # Page is already in the frame, no page fault
        continue
    else:
        # Page fault occurred
        frame[frame_index] = page
        frame_index = (frame_index + 1) % frame_size  # Move the frame index in a circular manner
        page_faults += 1
        print("Updated frame:", frame)

# Print the total number of page faults
print("Total page faults: ", page_faults)
print("Frame fault rate: ", page_faults / len(sequence))