apples = 10
var_2 = 10000
print(id(apples))
print(id(var_2))

a = 'hElLo'
b = "HellO"
c = '''Hello 
 World'''
d = """hellO
  worlD"""
print(a.upper())
print(b.lower())
print(c)
print(d)
print(len(c))
a, b = 2, 5
print(a+b, a-b, a*b, a**b, a/b, a//b, a % b)
a = -a
print(a, abs(a))

x, y, c = True, False, None
print(bool(x), bool(y), bool(1), bool(0), bool(-10), bool(c))
print(5 == 2, 4 == 4, 5 > 3, 5 > 9, 4 != 4, 4 != 45)
a = 4 == 5
print(a)
