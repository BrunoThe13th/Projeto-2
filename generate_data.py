import random


# Função responsável por gerar valores 0 ate n-1
# Sera utiliza para pegar um elemento aleatório de uma lista
def random_pos(final):
    return random.randint(0, final - 1)


# Função responsável por gerar os registros
def generator(q_people):
    # abertura dos arquivos
    txt_names = open("bases/name.txt", "r")
    txt_surnames = open("bases/surname.txt", "r")
    txt_trees = open("bases/tree.txt", "r")
    txt_phones = open("bases/phone.txt", "r")
    txt_zipcodes = open("bases/zipcode.txt", "r")
    txt_adresses = open("bases/street.txt", "r")
    txt_type = open("bases/type_adress.txt", "r")
    txt_cities = open("bases/city.txt", "r")
    txt_states = open("bases/state.txt", "r")
    txt_countries = open("bases/country.txt", "r")

    # definição das listas
    list_names = []
    list_surnames = []
    list_trees = []
    list_phones = []
    list_zipcodes = []
    list_adresses = []
    list_type = []
    list_cities = []
    list_states = []
    list_countries = []

    # populando as listas
    for name in txt_names:
        list_names.append(name.strip("\n"))

    for surnames in txt_surnames:
        list_surnames.append(surnames.strip("\n"))

    for tree in txt_trees:
        list_trees.append(tree.strip("\n"))

    for phone in txt_phones:
        list_phones.append(phone.strip("\n"))

    for zipcode in txt_zipcodes:
        list_zipcodes.append(zipcode.strip("\n"))

    for ad in txt_adresses:
        list_adresses.append(ad.strip("\n"))

    for type in txt_type:
        list_type.append(type.strip("\n"))

    for cit in txt_cities:
        list_cities.append(cit.strip("\n"))

    for state in txt_states:
        list_states.append(state.strip("\n"))

    for country in txt_countries:
        list_countries.append(country.strip("\n"))

    people = list()
    for _ in range(0, q_people):
        register_people = dict()
        complete_name = list_names[random_pos(len(list_names))] + " "
        complete_name += list_surnames[random_pos(len(list_surnames))]
        complete_name += " " + list_trees[random_pos(len(list_trees))]
        register_people['name'] = complete_name

        phone = "(" + str(random_pos(9)) + str(random_pos(9)) + ") "
        phone += str(random_pos(9)) + str(random_pos(9)) + str(random_pos(9))
        phone += str(random_pos(9)) + str(random_pos(9)) + "-"
        phone += str(random_pos(9)) + str(random_pos(9)) + str(random_pos(9))
        phone += str(random_pos(9))
        register_people['phone'] = phone

        zipcode = str(random_pos(9)) + str(random_pos(9)) + str(random_pos(9))
        zipcode += str(random_pos(9)) + "-" + str(random_pos(9))
        zipcode += str(random_pos(9)) + str(random_pos(9))
        register_people['zipcode'] = zipcode

        adress = list_type[random_pos(len(list_type))] + " "
        adress += list_adresses[random_pos(len(list_adresses))]
        register_people['adress'] = adress

        city = list_cities[random_pos(len(list_cities))]
        register_people['city'] = city

        state = list_states[random_pos(len(list_states))]
        register_people['state'] = state

        country = list_countries[random_pos(len(list_countries))]
        register_people['country'] = country

        people.append(register_people.copy())

    return people
