data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
        187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_value = 100
max_value = 200

for index, value in enumerate(data):
    if (value < min_value) or (value > max_value):
        del data[index]
print(data)
