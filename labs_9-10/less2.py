import os.path
from jinja2 import Template
import csv


class Character:
    def __init__(self, name, competition_type, characteristic, competition_data):
        self.name = name
        self.competition_type = competition_type
        self.characteristic = characteristic
        self.competition_data = competition_data


def get_file_content(path):
    if os.path.isfile(path):
        with open(path, "r", encoding='utf-8') as txt_infile:
            file_content = ''.join(txt_infile.read().splitlines())
    else:
        print("File not exists")

    return file_content


def set_csv_data(characters, path):
    with open(path, mode="w", encoding='utf-8') as csv_outfile:
        file_writer = csv.writer(
            csv_outfile, delimiter=";", lineterminator="\r")

        file_writer.writerow(
            ["Имя победителя", "Вид соревнования", "Дата соревнования", "Характеристика"])

        for char in characters:
            file_writer.writerow(
                [char.name, char.competition_type, char.competition_data, char.characteristic])
    pass


# ------------------------------------------------------------------------

char_1 = Character(
    input("Имя: "),
    input("Вид соревнования: "),
    int(input("Характеристика: ")),
    input("Дата соревнования: ")
)

char_2 = Character(
    input("Имя: "),
    input("Вид соревнования: "),
    int(input("Характеристика: ")),
    input("Дата соревнования: ")
)

characters = [char_1, char_2]


msg_template = Template(get_file_content('template2.txt'))

print('\n', msg_template.render(
    c_t=char_1.competition_type, char_1=char_1, char_2=char_2), '\n')


set_csv_data(characters, 'Персонажи.csv')
csv_inline = open('Персонажи.csv', 'r', encoding="utf-8")
print(csv_inline.read())
csv_inline.close()
