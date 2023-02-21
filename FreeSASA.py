import glob
import os
import subprocess

file_path = "/home/kaneko/outputdir/*_relaxed_model_3.pdb"
files = sorted(glob.glob(file_path))
#print(files)

file_name_path = "/home/kaneko/outputdir_copy/*_relaxed_model_3.pdb"
file_name = glob.glob(file_name_path)
b = sorted([os.path.basename(f) for f in file_name])
#print(file_names)

for (file, filename) in zip(files, b):
    cmd = ["freesasa" , "--format=rsa" , "--output" , filename , file]
    print(cmd)

    subprocess.run(cmd)

