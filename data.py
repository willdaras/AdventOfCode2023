def get_input(day: int) -> str:
    raw_data = open('data.txt', 'r').read()
    for data in raw_data.split('[day'):
        if data == '':
            continue
        if data.startswith(f'{day}]'):
            return data.removeprefix(f'{day}]')
