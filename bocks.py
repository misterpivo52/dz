# Базовий клас Книга
class Book:
    def __init__(self, title, author, isbn, year_published):
        """
        Ініціалізує базові атрибути книги.
        :param title: Назва книги
        :param author: Автор книги
        :param isbn: Унікальний ідентифікатор книги (ISBN)
        :param year_published: Рік публікації
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info(self):
        """
        Повертає інформацію про книгу у вигляді рядка.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year Published: {self.year_published}"


# Клас Художня книга (FictionBook), успадковує Book
class FictionBook(Book):
    def __init__(self, title, author, isbn, year_published, genre):
        """
        Додає жанр для художньої книги.
        :param genre: Жанр книги (наприклад, драма, фантастика)
        """
        super().__init__(title, author, isbn, year_published)
        self.genre = genre

    def get_info(self):
        """
        Повертає інформацію про художню книгу, включаючи жанр.
        """
        return super().get_info() + f", Genre: {self.genre}"


# Клас Науково-популярна книга (NonFictionBook), успадковує Book
class NonFictionBook(Book):
    def __init__(self, title, author, isbn, year_published, topic):
        """
        Додає тему для науково-популярної книги.
        :param topic: Тема книги (наприклад, історія, технології)
        """
        super().__init__(title, author, isbn, year_published)
        self.topic = topic

    def get_info(self):
        """
        Повертає інформацію про науково-популярну книгу, включаючи тему.
        """
        return super().get_info() + f", Topic: {self.topic}"


# Клас Довідкова книга (ReferenceBook), успадковує Book
class ReferenceBook(Book):
    def __init__(self, title, author, isbn, year_published, description):
        """
        Додає опис для довідкової книги.
        :param description: Опис книги (наприклад, коротка анотація)
        """
        super().__init__(title, author, isbn, year_published)
        self.description = description

    def get_info(self):
        """
        Повертає інформацію про довідкову книгу, включаючи опис.
        """
        return super().get_info() + f", Description: {self.description}"


# Клас Бібліотека
class Library:
    def __init__(self):
        """
        Ініціалізує порожній список книг у бібліотеці.
        """
        self.books = []

    def add_book(self, book):
        """
        Додає книгу до бібліотеки.
        :param book: Об'єкт книги
        """
        self.books.append(book)

    def remove_book(self, title):
        """
        Видаляє книгу з бібліотеки за назвою.
        :param title: Назва книги
        :return: True, якщо книгу видалено, інакше False
        """
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def get_books(self):
        """
        Повертає список усіх книг у бібліотеці.
        """
        return self.books

    def get_books_by_category(self, category):
        """
        Повертає книги певної категорії (Fiction, NonFiction, Reference).
        :param category: Категорія книги
        :return: Список книг у зазначеній категорії
        """
        if category == "Fiction":
            return [book for book in self.books if isinstance(book, FictionBook)]
        elif category == "NonFiction":
            return [book for book in self.books if isinstance(book, NonFictionBook)]
        elif category == "Reference":
            return [book for book in self.books if isinstance(book, ReferenceBook)]
        else:
            return []

    def get_books_by_author(self, author):
        """
        Повертає книги певного автора.
        :param author: Автор книги
        :return: Список книг цього автора
        """
        return [book for book in self.books if book.author == author]

    def get_books_by_year(self, year):
        """
        Повертає книги, опубліковані у певному році.
        :param year: Рік публікації
        :return: Список книг, виданих у зазначеному році
        """
        return [book for book in self.books if book.year_published == year]


# Інтерактивне меню для користувача
def main():
    """
    Основне меню для взаємодії з бібліотекою.
    """
    library = Library()  # Створення об'єкта бібліотеки
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")  # Додати книгу
        print("2. Remove Book")  # Видалити книгу
        print("3. View All Books")  # Переглянути всі книги
        print("4. View Books by Category")  # Переглянути книги за категоріями
        print("5. View Books by Author")  # Переглянути книги за автором
        print("6. View Books by Year")  # Переглянути книги за роком
        print("7. Exit")  # Вийти
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # Додавання книги
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            year_published = input("Enter the year published: ")
            category = input("Enter the category (Fiction, NonFiction, Reference): ").strip().capitalize()

            if category == "Fiction":
                genre = input("Enter the genre: ")
                book = FictionBook(title, author, isbn, year_published, genre)
            elif category == "NonFiction":
                topic = input("Enter the topic: ")
                book = NonFictionBook(title, author, isbn, year_published, topic)
            elif category == "Reference":
                description = input("Enter the description: ")
                book = ReferenceBook(title, author, isbn, year_published, description)
            else:
                print("Invalid category!")
                continue

            library.add_book(book)
            print(f"Book '{title}' added successfully!")

        elif choice == "2":
            # Видалення книги
            title = input("Enter the title of the book to remove: ")
            if library.remove_book(title):
                print(f"Book '{title}' removed successfully!")
            else:
                print(f"Book '{title}' not found!")

        elif choice == "3":
            # Відображення всіх книг
            print("All books in the library:")
            books = library.get_books()
            if books:
                for book in books:
                    print(book.get_info())
            else:
                print("No books in the library.")

        elif choice == "4":
            # Книги за категоріями
            category = input("Enter the category (Fiction, NonFiction, Reference): ").strip().capitalize()
            books = library.get_books_by_category(category)
            if books:
                print(f"Books in category '{category}':")
                for book in books:
                    print(book.get_info())
            else:
                print(f"No books found in category '{category}'.")

        elif choice == "5":
            # Книги за автором
            author = input("Enter the author's name: ")
            books = library.get_books_by_author(author)
            if books:
                print(f"Books by '{author}':")
                for book in books:
                    print(book.get_info())
            else:
                print(f"No books found by '{author}'.")

        elif choice == "6":
            # Книги за роком
            year = input("Enter the year of publication: ")
            books = library.get_books_by_year(year)
            if books:
                print(f"Books published in year {year}:")
                for book in books:
                    print(book.get_info())
            else:
                print(f"No books found published in year {year}.")

        elif choice == "7":
            # Вихід
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


# Запуск програми
if __name__ == "__main__":
    main()
