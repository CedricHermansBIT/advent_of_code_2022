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

inputs=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        if line == "\n":
            continue
        else:
            inputs.append(eval(line))
inputs.append([[2]])
inputs.append([[6]])
#print(inputs)

for _ in range(len(inputs)):
    for i in range(len(inputs)-1):
        if not evaluate(inputs[i],inputs[i+1]):
            inputs[i],inputs[i+1]=inputs[i+1],inputs[i]
r=1
for i,inp in enumerate(inputs):
    if inp==[[2]] or inp==[[6]]:
        r*=i+1
print(r)
