
import os.path


class File():
    words = []
    path: str

    def __init__(self, path):
        self.path = path
        file_text = open(path, ("r" if os.path.isfile(path) else "w"),
                         encoding='utf-8').read().splitlines()
        for string in file_text:
            self.words += str(string).split(' ')

    def delete_word(self, word):
        for element in self.words:
            if element == word:
                self.words.remove(word)
        pass

    def update_source(self):
        file = open(self.path, "w", encoding='utf-8')
        file.write(' '.join(self.words))
        file.close()
        pass

    def delete_char(self, char):
        words = []
        for i in range(len(self.words)):
            words.append(str(self.words[i]).replace(char, ''))
        self.words = words
        del words
        pass


file_text = File("file.txt")

print(file_text.words)
file_text.delete_char('т')

print(file_text.words)
file_text.delete_word('слово_для_удаления')

print(file_text.words)
file_text.update_source()
