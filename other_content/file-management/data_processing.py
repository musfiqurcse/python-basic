import os


#input_paths = ["Back_1","Back_2","Back_3"]
#output_path = "Back"

folders = []
counter = 1
input_paths = str(input()).split(" ")
output_path = str(input())
for input_path in input_paths:
    folders = []
    print(input_path)
    for r, d, f in os.walk(input_path):
        for folder in d:
            folders.append(os.path.join(r, folder))
        folders.append(f)
        print(f)
    folders[0].sort()
    print(folders[0])
    for k in range(0,len(folders[0])):
        os.system("scp "+input_path+"/"+folders[0][k]+f" {output_path}/{counter}.ply")
        counter+=1
