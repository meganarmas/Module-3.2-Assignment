# Task 1: Library System Enhancement 
# Sharpen your skills in managing and modifying data within tuples and lists.

#Problem Statement: You are maintaining a 
# library system where each book is stored as a 
# tuple within a list. Your task is to update this system by adding 
# new books and ensuring no duplicates.

#Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into 
# `library`. Ensure that adding a duplicate book is handled appropriately.

def adding_new_book():
    title_of_book = input("Include the title of the book: ")
    author = input("Include the author's name: ")
    new_book = ((title_of_book, author))
    if new_book not in library:
        library.append(new_book)
        print(f"New book {title_of_book} by {author} added to library")
    else:
        print(f"Book is already in library. Add a different one.")

adding_new_book()