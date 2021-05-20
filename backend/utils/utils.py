import csv


def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrderedDict.
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data
