lst = []

def add_book():
  name = input("Enter the name of the book : ")
  author = input("Enter the author : ")
  lst.append({'name':name,'Author':author,'read':False})


def list_book():
  print(lst)


def delete_book():
  index = int(input("Enter the index : "))
  del lst[index]


def read_book():
  b = int(input("Enter the index : "))
  l = lst[b]
  for ele in l:
    f=l['read']=True
  with open('file.txt','w') as f:
    f.write(str(l))
