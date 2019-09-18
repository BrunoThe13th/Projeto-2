# Foi validado em https://validator.w3.org/ (sem erros)
# Função responsável por formatar a saída para html


def format_html(people):
    html = '<!DOCTYPE html>\n'
    html += '<html lang="pt-br">\n'
    html += '\t<head>\n'
    html += '\t\t<title>HTML Format</title>\n'
    html += '\t\t<meta charset="utf-8">\n'
    html += '\t</head>\n'
    html += '\t<body>\n'
    html += '\t<table style="width:100%">\n'
    for person in people:
        html += '\t\t<tr>\n'
        i = 0
        for k in person.keys():
            html += '\t\t\t<th>'
            html += k + '</th>\n'
            i += 1
        break
    html += '\t\t</tr>\n'

    for person in people:
        i = 0
        html += '\t\t<tr>\n'
        for v in person.values():
            html += '\t\t\t<th>'
            html += v + '</th>\n'
            i += 1
        html += '\t\t</tr>\n'

    html += '\t</table>\n'
    html += '\t</body>\n'
    html += '</html>\n'

    return html
