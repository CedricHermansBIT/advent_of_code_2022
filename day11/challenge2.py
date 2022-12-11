class Monkey:
    def __init__(self, items: list, operation: str, test: int, true: int, false: int):
        self.items = items
        if operation.startswith("+"):
            if "old" not in operation:
                self.operation = lambda x: (x + int(operation[1:]))
            else:
                self.operation = lambda x: (x + x)
        elif operation.startswith("*"):
            if "old" not in operation:
                self.operation = lambda x: (x * int(operation[1:]))
            else:
                self.operation = lambda x: (x * x)
        self.operation_type = operation[0]
        self.test = lambda x: x%test==0
        self.test_value=test
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

## By looking at the inputs: the tests are always divide by a prime number, this means we can simplify the item values by dividing by the multiple of the prime numbers
## This is also called the Chinese Remainder Theorem, commonly used in these challenges ;) (and in cryptography)
## Small note: the values don't have to be prime, but they need to be coprime (no common factors)
simplifier=1
for monkey in monkeys:
    simplifier*=monkey.test_value

### Run the Keep Away game
for iteration in range(10000):
    print(iteration)
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            monkey.checks+=1
            item = monkey.popItem()
            item = monkey.operation(item)
            item %= simplifier
            if monkey.test(item):
                monkeys[monkey.true].pushItem(item)
            else:
                monkeys[monkey.false].pushItem(item)
checks=[monkey.checks for monkey in monkeys]
checks.sort(reverse=True)
print(checks)
print(checks[0]*checks[1])
