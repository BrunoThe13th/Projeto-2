# Foi validado em https://csvlint.com/online-validator (sem erros)
# Função responsável por formatar a saída para csv


def format_csv(people):
    csv = ''
    for person in people:
        i = 0
        for k in person.keys():
            if i == len(person) - 1:
                csv += k + '\n'
            else:
                csv += k + ','
            i += 1
        break

    for person in people:
        i = 0
        for v in person.values():
            if i == len(person) - 1:
                csv += v + '\n'
            else:
                csv += v + ","
            i += 1

    return csv
