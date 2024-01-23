def safe_print_list(my_list=[], x=0):
# Initialize a counter for the number of printed elements
 count = 0
# Use a try/except block to handle possible errors
 try:
# Loop through the list from index 0 to x-1
  for i in range(x):
# Print the element at index i, followed by a space
   print(my_list[i], end=" ")
# Increment the counter by 1
   count += 1
# Print a new line after the loop
  print()
# If an IndexError occurs, it means x is bigger than the length of the list
 except IndexError:
# Print a message indicating the error
   print("x is out of range")
# Return the number of printed elements
 return count
