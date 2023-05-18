thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

# Convert the list to a set and add it to the existing set
thisset.update(set(mylist))

# Print the modified set
print(thisset)
