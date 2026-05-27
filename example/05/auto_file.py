from shutil import copyfile
from os import listdir, makedirs
from os.path import isdir

orig_dir = "C:\\scandata\\"
out_dir  = "C:\\organized\\"

file_list = listdir(orig_dir)

for f_name in file_list:
    f_date = f_name[5:-4]
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year  = f_date[0]
    month = f_date[1]
    day   = f_date[2]

    target_dir = out_dir + year + "\\" + month + "\\" + day
    if not isdir(target_dir):
        makedirs(target_dir)

    copyfile(orig_dir+f_name, target_dir+"\\" + f_name)
    print(orig_dir+f_name + " => " + target_dir+"\\" + f_name)
