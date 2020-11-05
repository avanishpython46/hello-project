from utils.database import lst,add_book,list_book,read_book,delete
USER_CHOICE = """
R to read a book
q to quit
a to add a Book
l to list all books
d to delete a book : """
def menu():
  user_input = input(USER_CHOICE).lower()
  while user_input!='q':
    if user_input=='a':
      add_book()
    elif user_input=='d':
      delete()
    elif user_input=='l':
      list_book()
    if user_input=='r':
      read_book()
    user_input = input(USER_CHOICE).lower()

menu()
