# Função responsável por formatar a saída para sql insert
def format_insert(people):
    i = 0
    insert = "INSERT INTO person ("
    for person in people:
        for k in person.keys():
            if i == len(person) - 1:
                insert += k + ")"
            else:
                insert += k + ', '
            i += 1
        break
    insert += "\nVALUES  "
    for n_person in range(len(people)):
        i = 0
        insert += "("
        for v in people[n_person].values():
            if i == len(people[n_person]) - 1 and n_person == len(people)-1:
                insert += "'" + v + "'" + ");\n"
            elif i == len(people[n_person]) - 1:
                insert += "'" + v + "'" + "),\n\t"
            else:
                insert += "'" + v + "'" + ', '
            i += 1

    return insert
