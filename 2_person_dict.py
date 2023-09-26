person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
child = person["children"][1]
print(child)

# print out the name of the cat
cat = person["pets"]['cat']
print(cat)

# use a loop to print out the names of each child
for rec in person['children']:
    print(rec)

# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
for k, y in person['pets'].items():
    print(f"The type of pet is: {k} and the name of the pet is: {y}")

