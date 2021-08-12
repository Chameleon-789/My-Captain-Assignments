x = ["a", "b", "c"]


print(type(x))

x.append("e")
x.insert(3, "d")
x.append("J")
x.append("M")

print(x)
x.remove("J")
x.pop(-1)

print(x)

myList1 = ["f", "g"]

x.extend(myList1)

y = x.copy()

x.clear()
print(y)

print(y.count("d"))
print(y.index("f"))

y.sort()
y.reverse()

print(y)
