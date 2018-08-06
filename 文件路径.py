import os
def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        #print('ss ',maindir)
        print(file_name_list)
        #print('sssss',max(subdir))
        #exit()
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            #print(apath)
            result.append(apath)
    return result

path_a = 'D:\python\chuhuo'    

all_path(path_a)