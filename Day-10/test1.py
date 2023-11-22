import os
folders = input("Provide the folder name: ").split()

for folder in folders :

    #exceptional handling
    try:
        files = os.listdir(folder)
    except PermissionError:
        print("No access for this folder:" + folder)
        continue
    except FileNotFoundError:
        print("please provide valid folder name, look like this folder doesn't exist:")
        break

    print("----- listing files for folder:" + folder)
    
    for file in files:
        print(file)
