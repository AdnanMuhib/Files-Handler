import os
def file_handling():
	print("\n1- List Files")
	print("2- Open a file")
	print("3- Create New file")
	print("4- Delete a file")
	print("5- Exit\n\n***********: \n")
	choice = input(":")
	if (choice == 1):
		for filename in os.listdir("D:\UNIVERSITY DOCUMENTS\SEMESTER NUMBER 6\Operating System"):
			print filename
		file_handling()

	elif(choice == 2):
		filename = raw_input("Enter a filename to open: ")
		if (os.path.isfile(filename)):
			myfile = open(filename)
			if (myfile):
				print("File " + filename + " opened Successfully....\n\nFile has following content")
				text = myfile.read()
				print(text)
		else:
			print("file doesn't exist in the current directory...")
		file_handling()

	elif(choice == 3):
		filename = raw_input("type the File name to Create: ")
		file_text = raw_input("type the Content to write in the file: ")
		count = 1
		while (os.path.isfile(filename)):
			filename = filename + "(" + str(count) + ")"
		with open(filename,'w+') as myfile:
			myfile.write(file_text)
			myfile.close()
		file_handling()

	elif(choice == 4):
		filename = raw_input("Type the name of the file to delete: ")
		if (os.path.isfile(filename)):
			os.remove(filename)
			print("file deleted Successfully...")
		else:
			print(filename + " doesn't exist in the current directory...")
		file_handling()
	elif(choice == 5):
		pass
	else:
		print("wrong input")
		file_handling()

def main():
	file_handling()
if __name__ == '__main__':
	main()

