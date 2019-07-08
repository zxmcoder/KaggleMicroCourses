# https://pintia.cn/problem-sets/14/problems/800
# 左右对齐的方式
# 左 :0<4 左补0长度为4
# 右 :*>8 右补*长度为8
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print('{}*{}={:<4}'.format(j, i, i * j), end = '')
    print()
# https://pintia.cn/problem-sets/14/problems/801
n = int(input())
f = False
for y in range(1, 106):
    for x in range(1, y + 1):
        if x ** 2 + y ** 2 == n:
            f = True
            print('{} {}'.format(x, y))
if not f:
    print('No Solution')
# for循环不可以改变i的值，我TM……
# https://pintia.cn/problem-sets/14/problems/802
t = int(input())
a = [0] * (t + 1)
for i in range(1, t + 1):
    a[i] = a[i - 1] + 3
b = [0] * (t + 1)
x = 0
while x < t + 1:
    if b[x] <= a[x]:
        for j in range(x + 1, min(x + 11, t + 1)):
            b[j] = b[j - 1] + 9
        x += 10
    else:
        for j in range(x + 1, min(x + 31, t + 1)):
            b[j] = b[j -1]
        x += 30
if a[t] == b [t]:
    print('-_- {}'.format(a[t]))
elif a[t] > b[t]:
    print('@_@ {}'.format(a[t]))
else:
    print('^_^ {}'.format(b[t]))