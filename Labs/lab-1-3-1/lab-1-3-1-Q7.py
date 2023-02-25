# Lab 1-3-1 Q6
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Write a program to ask the user to enter the current time and duration of a meeting
# and then display the end time of the meeting.

print('Meeting time calculator')

# get the start time
start_hour = int(input('Please enter the start time (hours): '))
start_minute = int(input('Please enter the start time (minutes): '))

# get the duration of the meeting
duration_minutes = int(input('Please enter the duration (minutes): '))

# calculate the end time
end_hour = start_hour + (start_minute + duration_minutes) // 60
end_minute = (start_minute + duration_minutes) % 60

# display the end time
print()
print(f'The meeting will start at {start_hour:0>2d}:{start_minute:0>2d}')
print(f'The meeting will end at {end_hour:0>2d}:{end_minute:0>2d}')