N = int(input())
words = []
for _ in range(N):
    words.append(input())

def ancient_order(words):
    adj_lst = []
    for _ in range(26):
        adj_lst.append([])

    indeg = [0]*26
    hst = [False]*26  

    for w in words:
        for c in w:
            hst[ord(c)-ord('a')] = True

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        found = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                u = ord(w1[j])-ord('a')
                v = ord(w2[j]) - ord('a')
                adj_lst[u].append(v)
                indeg[v] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            print(-1)
            return

    out = []
    queue = [0] * 26
    next = 0
    prev = 0

    for i in range(26):
        if indeg[i] == 0 and hst[i]:
            queue[prev] = i
            prev += 1

    while next < prev:
        best = -1
        for i in range(next, prev):
            if best == -1 or queue[i] < queue[best]:
                best = i
        queue[next], queue[best] = queue[best], queue[next]

        u = queue[next]
        next += 1
        out.append(chr(u + ord('a')))
        for v in adj_lst[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue[prev] = v
                prev += 1

    if len(out) != sum(hst):
        print(-1)
    else:
        print(''.join(out))

ancient_order(words)
