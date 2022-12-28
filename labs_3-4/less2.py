
class Human():
    def __init__(self, surname, name, second_name, age=0, sex="Ж"):
        self.surname = surname.title()
        self.name = name.title()
        self.second_name = second_name.title()
        self.age = age
        self.sex = sex
        pass

    def get_fio(self):
        print(self.surname + " " +
              self.name[0] + ". " +
              self.second_name[0] + ".")
        pass

    def get_full_info(self):
        tmp = [
            f"Фамилия: {self.surname}",
            f"Имя: {self.name}",
            f"Отчество: {self.second_name}",
            f"Возраст: {self.age}",
            f"Пол: {self.sex}"
        ]
        return "\n".join(tmp)


class Student(Human):
    def __init__(self, surname, name, second_name, age=0, sex="Ж", group=""):
        super().__init__(surname, name, second_name, age, sex)
        self.group = group
        pass

    def get_full_info(self, mode=False):
        orig = super().get_full_info()
        tmp = [
            f"Группа: {self.group}"
        ]

        if mode:
            tmp = orig.split("\n") + tmp
            return ", ".join(tmp)
        else:
            tmp.insert(0, orig)
            return "\n".join(tmp)


if __name__ == "__main__":
    student = Student("Иванов", "Василий",
                      "Петрович", 18, "м", "пгст-11")

    print(student.get_full_info())
    print()
    print(student.get_full_info(True))
