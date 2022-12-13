def evaluate(left, right):
    for l,r in zip(left,right):
        if type(l) == int and type(r) == int:
            if l<r:
                return True
            elif l>r:
                return False
            else:
                continue
        else:
            if type(l) == int and type(r) == list:
                res=evaluate([l],r)
            elif type(l) == list and type(r) == int:
                res=evaluate(l,[r])
            elif type(l) == list and type(r) == list:
                res=evaluate(l,r)
            if res is not None:
                return res
    else:
        if len(left)<len(right):
            return True
        elif len(left)>len(right):
            return False
        else:
            return None


inputs=[[]]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if line == "\n":
            inputs.append([])
        else:
            inputs[-1].append(eval(line))

#print(inputs)

sum=0
for n, (left, right) in enumerate(inputs):
    if evaluate(left,right):
        #print(n+1)
        sum+=n+1
print(sum)
