# Função responsável por formatar a saída para sql insert
# Foi validado em http://sqllint.com/ (sem erros)

# O https://www.eversql.com/sql-syntax-check-validator/ não aceita um
# INSERT INTO para cada registro, aceitando apenas da seguinte forma:
# Ex.: INSERT INTO tabela(a,b,c) VALUES(1, 2, 3), (4,5,6), (7,8,9);


def format_insert(people):
    insert = ""
    for n_person in range(len(people)):
        i = 0
        insert += "INSERT INTO person("
        for k in people[n_person].keys():
            if i == len(people[n_person]) - 1:
                insert += k + ") "
            else:
                insert += k + ', '
            i += 1

        i = 0
        insert += "VALUES("
        for v in people[n_person].values():
            if i == len(people[n_person]) - 1:
                insert += "'" + v + "'" + ");\n"
            else:
                insert += "'" + v + "'" + ', '
            i += 1

    return insert
