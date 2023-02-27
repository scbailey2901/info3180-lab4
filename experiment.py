import os
filelist=[]
for subdir, dirs, files in os.walk("C:/Users/shane/Downloads/info3180-labs/info3180-lab4/uploads/"):
    for file in files:
        f=(os.path.join(subdir, file))
        print(f)
        if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpg"):
            filelist.append(f)
    print(filelist)

