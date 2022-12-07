path=""
fs={'':[[],0]}

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if line.startswith('$'):
            if line.startswith('$ ls'):
                continue
            elif line.strip()=="$ cd /":
                path=""
            elif line.startswith("$ cd .."):
                path=path[:path.rfind('/')]

            elif line.startswith("$ cd"):
                path=path+"/"+line[4:].strip()
                if path not in fs:
                    fs[path]=[[],0]
            else:
                assert False, "Unknown command"+line
        elif line.startswith('dir'):
            #print(line)
            if path+"/"+line[4:].strip() not in fs:
                fs[path+"/"+line[5:].strip()]=[[],0]
            fs[path][0].extend(line[4:].strip().split())
        else:
            fs[path][1]+=int(line.split()[0].strip())
print(fs)

def recurse(path):
    if fs[path][0]==[]:
        return fs[path][1]
    else:
        fs[path][1]=fs[path][1]+sum([recurse(path+"/"+x) for x in fs[path][0]])
        return fs[path][1]

recurse("")
print(fs)
total=0
for path in fs:
    if fs[path][1]<100000:
        print(path,fs[path][1])
        total+=fs[path][1]

print(total)
