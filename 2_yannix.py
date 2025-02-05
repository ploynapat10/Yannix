input_1 = int(input())
input_2 = input()

input_2 = input_2[1:-1].split(",")
ip2 = list(map(int, input_2))

def cal_water(volume,high):
    sum_high = sum(high)
    water_level = (volume+(sum_high))/len(high)
    return water_level

while True:
    total = 0
    min_high = min(ip2)
    level = cal_water(input_1,ip2)
    for i in ip2:
        total += round(abs(level-i),4)
    if total != input_1:
        mx = max(ip2)
        mx_i = ip2.count(mx)
        for i in range(mx_i):
            ip2.remove(mx)
        if max(ip2)!=mx:
            level = cal_water(input_1,ip2)
            print('%.2f' %(level-min_high))
            break
        elif max(ip2)==mx:
            print('%.2f' %(level-min_high))
            break
                
    else:
        level = cal_water(input_1,ip2)
        print('%.2f' %(level-min_high))
        break