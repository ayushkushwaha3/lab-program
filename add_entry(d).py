
def add_entry(d):
    d["age"] = 20


def reassign_dict(d):
    d = {"name": "Rahul", "age": 25}
    print("Inside function:", d)


student = {"name": "Ayush"}

print("Before function calls:", student)


add_entry(student)
print("After add_entry():", student)


reassign_dict(student)
print("After reassign_dict():", student)