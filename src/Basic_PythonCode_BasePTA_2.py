# https://pintia.cn/problem-sets/14/problems/804
import math
a, b = input().split('/')
a = int(a)
b = int(b)
c = math.gcd(a, b)
print('{}/{}'.format(a // c, b // c))
# https://pintia.cn/problem-sets/994805260223102976/problems/994805325918486528
n = eval(input())
t = 0
while n != 1:
    if n % 2:
        n = (3 * n + 1) / 2
    else:
        n /= 2
    t += 1
print(t)
# https://pintia.cn/problem-sets/994805260223102976/problems/994805324509200384
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# eval()和int()的区别
n = input()
s = 0
for c in n:
    s += int(c)
change = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
words = []
while s:
    words.append(change[s % 10])
    s //= 10
print(words[len(words) - 1], end = '')
for i in range(len(words) - 2, -1, -1):
    print(' {}'.format(words[i]), end = '')
# https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
n = eval(input())
# for i in range(0, n):
for i in range(n):
    s = input()
    # p = t = a = 0
    for c in s:
        if c == 'P':
            p += 1
            posp = s.index(c)
        if c == 'A':
            a += 1
        if c == 'T':
            t += 1
            post = s.index(c)
        # p = s.count('P')
        # a = s.count('A')
        # t = s.count('T')
    # print(posp,post)
    if p != 1 or t != 1 or a < 1 or p + t + a != len(s) or posp >= post:
        print("NO")
        continue
    # print('1111')
    res = 'YES' if posp * (post - posp - 1) == (len(s) - post - 1) else 'NO'
    print(res) 