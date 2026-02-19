# with command
''' with open("temp.txt","w") as file:
  file.write("test data\n")
  file.write("more data\n")'''


with open("files_and_json/temp.txt","r") as file:
  for line in file:
    print(line)

''' with open("files_and_json/temp.txt","w") as file:
  for i in range(5):
    name=input()
    file.write(name+"\n")'''
