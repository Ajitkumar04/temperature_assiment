# user input storsge in file
name=input()
file=open("user_file.txt","a")
file.write(f"\n new user added:{name}")
file.close()