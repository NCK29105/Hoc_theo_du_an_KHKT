class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Năm xuất bản: {self.year}")
        print("-" * 30)


if __name__ == "__main__":
    book1 = Book("Dế Mèn Phiêu Lưu Ký", "Lê văn C", 1941)
    book2 = Book("Tư tưởng HCM", "Nguyễn Văn A", 2022)

    book1.display_info()
    book2.display_info()