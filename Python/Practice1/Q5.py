class Book:
    def __init__(self, author , title, pages):
        self.author=author
        self.title=title
        self.pages=pages

    def display_info(self):
        print("author name is ",self.author)
        print("title is ", self.title)
        print("no of pages are", self.pages)
B1=Book("Ana ", "abc",200)
B1.display_info()