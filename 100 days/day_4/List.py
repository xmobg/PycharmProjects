states_of_america = ["Delaware", "Pennsylvania", "New York", "San Fransisco", "New Jersey", "Georgia"]

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[5])
for state in states_of_america:
    print(state)

states_of_america[0] = "Washington"
print(states_of_america[0])

states_of_america.append("Arizona")
print(states_of_america)

states_of_america.extend(["California", "New York"])
print(states_of_america)