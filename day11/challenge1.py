class Monkey:
    def __init__(self, items: list, operation: str, test: int, true: int, false: int):
        self.items = items
        if operation.startswith("+"):
            if "old" not in operation:
                self.operation = lambda x: (x + int(operation[1:]))//3
            else:
                self.operation = lambda x: (x + x) // 3
        elif operation.startswith("*"):
            if "old" not in operation:
                self.operation = lambda x: (x * int(operation[1:]))//3
            else:
                self.operation = lambda x: (x * x) // 3
        self.test = lambda x: x%test==0
        self.true = true
        self.false = false
        self.checks=0

    def pushItem(self, item: int):
        self.items.append(item)

    def popItem(self):
        return self.items.pop(0)
    
### Parse input

monkeys=[]

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        line=line.lstrip()
        if line.startswith("Starting items:"):
            items = [int(x) for x in line.split(":")[1].split(",")]
        elif line.startswith("Operation: new = old "):
            operation = line.split("old ")[1].strip()
        elif line.startswith("Test: divisible by "):
            test = int(line.split("by ")[1].strip())
        elif line.startswith("If true: throw to monkey "):
            true = int(line.split("monkey ")[1].strip())
        elif line.startswith("If false: throw to monkey "):
            false = int(line.split("monkey ")[1].strip())
        if line.strip()=="":
            monkeys.append(Monkey(items, operation, test, true, false))
    monkeys.append(Monkey(items, operation, test, true, false))

print(monkeys)

### Run the Keep Away game
for iteration in range(20):
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            monkey.checks+=1
            item = monkey.popItem()
            item = monkey.operation(item)
            if monkey.test(item):
                monkeys[monkey.true].pushItem(item)
            else:
                monkeys[monkey.false].pushItem(item)
checks=[monkey.checks for monkey in monkeys]
checks.sort(reverse=True)
print(checks[0]*checks[1])
