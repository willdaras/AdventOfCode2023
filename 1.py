import data

data = data.get_input(1)

number_strings = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

result = 0

for line in data.split("\n"):
    if line == '':
        continue
    numbers = []
    for i, char in enumerate(line):
        if char.isnumeric():
            numbers.append(char)
        for key in number_strings.keys():
            if line[i:].startswith(key):
                numbers.append(number_strings[key])
    if len(numbers) == 0:
        continue
    result += int(numbers[0] + numbers[len(numbers) - 1])

print(result)