size = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1
cord = [(x-1, y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

count = 0
possible_cord = []
for a, b in cord:
    if a<0 or a>size-1 or b<0 or b>size-1:
        continue
    count += 1
    possible_cord.append((a+1,b+1))
print(count)
for x, y in possible_cord:
    print(x, y)