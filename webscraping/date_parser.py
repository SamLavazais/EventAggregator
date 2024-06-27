import re
import dateparser


def date_parser(date, source):
    match source:
        case "user":
            return dateparser_user(date)
        case "HAS":
            return dateparser_has(date)
        case "FIRAH":
            pass
        case "CNSA":
            return dateparser_cnsa(date)
        case "Filnemus":
            return dateparser_filnemus(date)


def dateparser_user(date):
    return dateparser.parse(date, settings={'DATE_ORDER': 'YMD'})


def dateparser_has(date):
    # créer le regex permettant de sélectionner la 1ère date indiquée
    pattern = r'\A\w{2}\s(\d{2}/\d{2}/\d{4})'
    match = re.findall(pattern, date)[0]
    # parser la date avec le package de parsing
    parsed_date = dateparser.parse(match, settings={'DATE_ORDER': 'DMY'})

    return parsed_date
    # retourner la date sous un format FRONT ?


# ATTENTION au regex "\n" : vérifier si ça fonctionne en conditions réelles !
def dateparser_cnsa(date):
    # créer le regex permettant de sélectionner la 1ère date indiquée
        # ex : "1er\n                \n                octobre"
    pattern = r'\A(\d{1,2})\w*\n\s+\n\s+(\w{2,})'
    [day, month] = re.findall(pattern, date)[0]
    date_to_parse = "{0} {1} {2}".format(day, month, 2024)
    # parser la date avec le package de parsing
    parsed_date = dateparser.parse(
        date_to_parse
    )
    return parsed_date
    # retourner la date sous un format FRONT ?


def dateparser_filnemus(date):
    # créer le regex permettant de sélectionner la 1ère date indiquée
    # ex : "11Jun." ”02Jul." "05Jul.06Jul." "12Sep.14Sep."
    pattern = r'\A(\d{1,2})(\w{3}).'
    [day, month] = re.findall(pattern, date)[0]
    date_to_parse = "{0} {1} {2}".format(day, month, 2024)
    # parser la date avec le package de parsing
    parsed_date = dateparser.parse(
        date_to_parse,
    )

    return parsed_date
    # retourner la date sous un format FRONT ?
