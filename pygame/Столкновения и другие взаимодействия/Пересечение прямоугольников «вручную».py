def linecross(x11, x12, x21, x22):
    return x21 <= x11 <= x22 or x11 <= x21 <= x12


l1, t1, w1, h1 = map(int, input().split())
l2, t2, w2, h2 = map(int, input().split())

if linecross(l1, l2 + w1, l2, l2 + w2) and linecross(t1, t1 + h1, t2, t2 + h2):
    print("YES")
else:
    print("NO")