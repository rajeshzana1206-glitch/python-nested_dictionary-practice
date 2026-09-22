student = {
    "student1" : {
        "name" : "Rajesh",
        "course" : "python",
        "mark" : 90
        },

    "student2" : {
        "name" : "Arun",
        "course" : "python",
        "mark" : 75
        }
    }

for key, value in student.items():
    print(key)

    for inner_key, inner_value in value.items():
        print(inner_key, ":", inner_value)

    
'''print(student["student1"]["name"]
print(student["student1"]["course"])
print(student["student1"]["mark"])

print(student["student2"]["name"])
print(student["student2"]["course"])
print(student["student2"]["mark"])'''


