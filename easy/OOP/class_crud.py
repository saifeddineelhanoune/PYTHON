class CRUDOperations:
    def __init__(self):
        self.my_list = []
        self.my_dict = {}
        self.my_set = set()

    # Create operations
    def create_list(self, value):
        self.my_list.append(value)

    def create_dict(self, key, value):
        self.my_dict[key] = value

    def create_set(self, value):
        self.my_set.add(value)

    # Read operations
    def read_list(self, index):
        return self.my_list[index]

    def read_dict(self, key):
        return self.my_dict.get(key)

    def read_set(self):
        return self.my_set

    # Update operations
    def update_list(self, index, value):
        self.my_list[index] = value

    def update_dict(self, key, value):
        self.my_dict[key] = value

    def update_set(self, old_value, new_value):
        self.my_set.remove(old_value)
        self.my_set.add(new_value)

    # Delete operations
    def delete_list(self, index):
        del self.my_list[index]

    def delete_dict(self, key):
        del self.my_dict[key]

    def delete_set(self, value):
        self.my_set.remove(value)


# Example usage
crud = CRUDOperations()

# Create operations
crud.create_list("apple")
crud.create_dict("fruit", "banana")
crud.create_set("cherry")

# Read operations
print(crud.read_list(0))  # Output: "apple"
print(crud.read_dict("fruit"))  # Output: "banana"
print(crud.read_set())  # Output: {"cherry"}

# Update operations
crud.update_list(0, "orange")
crud.update_dict("fruit", "mango")
crud.update_set("cherry", "strawberry")

# Delete operations
crud.delete_list(0)
crud.delete_dict("fruit")
crud.delete_set("strawberry")
