n_room = int(input())
usingOrder = input()
usingOrder = usingOrder[1:-1].split(",")
order = list(map(int, usingOrder))

room = []
for i in range(n_room):
    room.append(0)

level = []
for i in range(n_room):
    level.append(0)

for i in range(n_room):
    x = order.index(i+1)
    if (x != 0) and (x!=n_room-1):
        if room[x-1] == 0 and room[x+1]==0:
            level[x] = 0
        else:
            for i in range(1,n_room-1):
                if room[i-1] == 0 and room[i] == 0 and room[i+1] == 0:
                    level[x] = 2
                    break
                elif (room[0] == 0 and room[1] == 0) or (room[-1] == 0 and room[-2] == 0):
                    level[x] = 2
                    break
                else:
                    level[x] = 1
    if x==0:
        if room[1] == 1:
            for i in range(1,n_room-1):
                if room[i-1] == 0 and room[i] == 0 and room[i+2] == 0:
                    level[x] = 2
                    break
                elif (room[0] == 0 and room[1] == 0) or (room[-1] == 0 and room[-2] == 0):
                    level[x] = 2        
                    break
                else:
                    level[x] = 1       
        else:
            level[x] = 0
    if x==n_room-1:
        if room[n_room-2] == 1:
            for i in range(1,n_room-1):
                if room[i-1] == 0 and room[i] == 0 and room[i+2] == 0:
                    level[x] = 2        
                    break
                elif (room[0] == 0 and room[1] == 0) or (room[-1] == 0 and room[-2] == 0):
                    level[x] = 2        
                    break
                else:
                    level[x] = 1
        else:
            level[x] = 0
    room[x] = 1
print(level)