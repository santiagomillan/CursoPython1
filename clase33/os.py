import os

#directorio actual
# cwd = os.getcwd()
# print("Current Working Directory:", cwd)

#listar los files .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Text files in current directory:", txt_files)

#re nombrar un file
os.rename('1.txt', 'new_name.txt')
print("File renamed successfully.")

#listar los files .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Text files in current directory:", txt_files)