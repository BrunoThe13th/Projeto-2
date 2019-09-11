# Função responsável por formatar a saída para json
def format_json(people):
    json = '[\n'
    for n_person in range(len(people)):
        i = 0
        json += '\t{\n'
        for k, v in people[n_person].items():
            if i == len(people[n_person]) - 1:
                json += '\t\t' + f'"{k}" : "{v}"\n'
            else:
                json += '\t\t' + f'"{k}" : "{v}",\n'
            i += 1
        if n_person == len(people) - 1:
            json += '\t}\n'
        else:
            json += '\t},\n'
    json += ']'

    return json
