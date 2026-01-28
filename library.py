class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print("\nTitle  :", self.title)
        print("Author :", self.author)
        print("Price  :", self.price)
        print("-" * 20)

n = int(input("How many books do you want to enter? "))
books = []

for i in range(n):
    print(f"\nEnter details of Book {i+1}:")
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    books.append(Book(title, author, price))

print("\n--- Book Details ---")
for b in books:
    b.show()
