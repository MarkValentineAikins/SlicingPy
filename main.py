# Slicing in python help you to create a sub-string by using he slice function.
from audioop import reverse

name = "Mark Valentine Aikins"
first_name = name[0:4]
print("We have slice the first four letters, " +"we have "+ first_name)
last_name = name[15:22]
#last_name = name[-6:]
print("Slicing the last six letters, "+ "we have "+ last_name)
middle_name = name[5:14]
print("Slicing the middle nine letters, "+"we have " +middle_name)
Step_name = name[0:14:2]
print("Slicing the step ten letters, "+"we have " +Step_name)
reverse_name = name[::-1]
print("Reverse the name, "+"we have " +reverse_name)
# Slicing a URL with slice functionality
google_URL = "https://www.google.com"
palm_URL = "https://www.palm.edu.gh"
#slice = google_URL.split("/")
#print("Slicing slice with slice functionality "+"we have "+ str(slice))
#slice = slice(12,-4)
slice_ed = slice(12,-7)
#print(google_URL[slice])
print(palm_URL[slice_ed])

