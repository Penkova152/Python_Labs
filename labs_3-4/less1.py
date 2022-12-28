class Cat:
    name = "Барсик"
    friends = []

    def get_sound(self):
        print("мяю")
        pass

    def add_friend(self, obj):
        self.friends.append(obj)
        pass

    def friends_list(self):
        if self.friends.empty():
            print("Список пуст")
        else:
            for friend in self.friends:
                print(friend.name)


class Dog:
    name = "Барбос"
    friends = []

    def get_sound(self):
        print("гав-гав")
        pass

    def add_friend(self, obj):
        self.friends.append(obj)
        pass

    def friends_list(self):
        if not self.friends:
            print("Список пуст")
        else:
            for friend in self.friends:
                print(friend.name)


class Chicken():
    name = "Курица"
    friends = []

    def get_sound(self):
        print("чик-чик")
        pass

    def add_friend(self, obj):
        self.friends.append(obj)
        pass

    def friends_list(self):
        if self.friends.empty():
            print("Список пуст")
        else:
            for friend in self.friends:
                print(friend.name)


cat = Cat()
dog = Dog()
chicken = Chicken()

Animals = [cat, dog, chicken]

for obj in Animals:
    print(obj.name, end=": ")
    obj.get_sound()

dog.add_friend(chicken)
dog.add_friend(cat)
dog.friends_list()
