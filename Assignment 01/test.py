N = int(input())
name = []
destination = []
time = []
for j in range(N):
    string = input()
    string = string.split()
    name.append(string[0])
    destination.append(string[4])
    time.append(string[6])


def sort(name, dest, time, N):
    for i in range(N):
        flag = False
        for j in range(0, N-i-1):
            if name[j+1] < name[j]:
                name[j], name[j+1] = name[j+1], name[j]
                dest[j], dest[j+1] = dest[j+1], dest[j]
                time[j], time[j+1] = time[j+1], time[j]
                flag = True
            elif name[j+1] == name[j]:
                if time[j+1] > time[j]:
                    name[j], name[j+1] = name[j+1], name[j]
                    dest[j], dest[j+1] = dest[j+1], dest[j]
                    time[j], time[j+1] = time[j+1], time[j]
                    flag = True
        if flag == False:
            break

    return name, dest, time


n, d, t = sort(name, destination, time, N)

for j in range(N):
    print(f'{n[j]} will departure for {d[j]} at {t[j]}')