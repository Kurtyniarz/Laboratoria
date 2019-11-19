import pickle
import time


class Blog:
    def __init__(self, author):
        if author == '':
            author = 'Default User'
        self.author = author
        file = open('blogdata.txt', 'rb')
        try:
            self.blogData = pickle.load(file)
            self.run()
        except EOFError:
            self.blogData = {
                "entries": []
            }
            self.add()
        file.close()

    def run(self):
        self.load()
        print('Wybierz operacje:')
        print('1.Dodaj wpis')
        print('2.Zakoncz program')
        opt = input('... ')
        self.option(opt)

    def option(self, option):
        if option == 1 or option == '1':
            self.add()
        elif option == 2 or option == '2':
            self.exit()
        else:
            print('Zly wybor...')
            self.run()

    def add(self):
        print('Podaj wpis, ktory chcesz dodac: ')
        text = str(input())
        newDate = time.ctime(time.time())
        self.blogData['entries'].append({
            'author': self.author,
            'text': text,
            'date': str(newDate)
        })
        file = open('blogdata.txt', 'wb')
        pickle.dump(self.blogData, file)
        self.run()

    def load(self):
        for entry in reversed(self.blogData['entries']):
            print(f"Autor: {entry['author']}, Data i czas: {entry['date']} \n Wpis: {entry['text']}")

    def exit(self):
        exit()


def main():
    print('Witaj w aplikacji Blog! Podaj swoje imie')
    author = str(input('Imie: '))
    newBlog = Blog(author)


if __name__ == '__main__':
    main()
