key = ["name","age","major"]
value = ["Ivan","25","Computer science"]

student = {}

for i in range (len(key)):
    student[key[i]] = value[i]
print(student)

my_dict = {"name":"Ivan","age":30,"occupation":"student"}
name = my_dict.get("name")
print(name)