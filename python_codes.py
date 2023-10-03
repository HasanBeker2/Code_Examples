

my_list = []

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)



# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")


# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)


# Print the current list
print("Current list:", my_list)


# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list


# Print the updated list
print("Updated list:", my_list)