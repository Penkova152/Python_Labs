from jinja2 import Template
import os.path
import json


def get_file_content(path):
    if os.path.isfile(path):
        with open(path, "r", encoding='utf-8') as txt_infile:
            file_content = txt_infile.read()
    else:
        print("Файла нет")

    return file_content


def get_final_msg(json_answers_path, msg_template):

    if os.path.isfile(json_answers_path):
        with open('Ответы.json', "r", encoding='utf-8') as json_infile:
            answers = json.load(json_infile)
            for answer in answers['data']:
                user_name = answer["Имя"]
                time = answer["Время"]
                item = answer["Предмет"]
                place = answer["Место"]
    else:
        user_name = input("Имя: ")
        time = input("Время: ")
        item = input("Предмет: ")
        place = input("Место: ")

    return msg_template.render(u_n=user_name, t=time, i=item, p=place)


# ------------------------------------
tm = Template(get_file_content('template1.txt'))

print(get_final_msg('Ответы.json', tm))
