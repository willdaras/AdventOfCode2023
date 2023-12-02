import data

data = data.get_input(2)

cube_colour_count = {'red': 12, 'green': 13, 'blue': 14}

result = 0

for game_id, dataset in enumerate(data.split('Game ')[1:]):
    game_data = dataset.removeprefix(f'{game_id + 1}: ')
    game_data = game_data.replace('; ', ', ').replace('\n', '')
    cube_sets = game_data.split(', ')
    min_per_colour = {'red': 0, 'green': 0, 'blue': 0}
    for cube_set in cube_sets:
        pair = cube_set.split(' ')
        if int(min_per_colour[pair[1]]) < int(pair[0]):
            min_per_colour[pair[1]] = int(pair[0])
    power = 1
    for count in min_per_colour.values():
        power *= count
    result += power

print(result)