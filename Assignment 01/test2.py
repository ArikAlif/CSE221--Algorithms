N = int(input())
name = []
destination = []
time = []
for i in range(N):
    string = input()
    string = string.split()
    name.append(string[0])
    destination.append(string[4])
    time.append(string[6])


def sort(name, dest, time, N):
    for i in range(N-1):
        min_ind = i
        for j in range(i+1,N):
            if name[min_ind] > name[j]:
                min_ind = j
            elif name[min_ind] == name[j]:
                if time[min_ind] < time[j]:
                    min_ind = j


        name[i], name[min_ind] = name[min_ind], name[i]
        dest[i], dest[min_ind] = dest[min_ind], dest[i]
        time[i], time[min_ind] = time[min_ind], time[i]

    return name, dest, time

n, d, t = sort(name, destination, time, N)

for i in range(N):
    print(f'{n[i]} will departure for {d[i]} at {t[i]}')


