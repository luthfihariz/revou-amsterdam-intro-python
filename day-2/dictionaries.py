student = {
    "name": "John Doe", 
    "age": 20, 
    "major": "Computer Science",
    "is_graduated": True,
}

# print(student["name"])
# print(student.get("age"))
# print(student.get("lives_in", "Nowhere"))

# print(student.pop("major"))

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, "=", value)

for value in student.values():
    print(value)


student["lives_in"] = "Bekasi"
print(student)