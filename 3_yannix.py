wall_high = input()

wall_high = wall_high[1:-1].split(",")
high = list(map(int, wall_high))

water_high1 = [high[0]]
water_high2 = [high[-1]]

mx1=high[0]
for i in range(len(high)-2):
    if high[i+1]>mx1:
        mx1 = high[i+1]
        water_high1.append(mx1)
    else:
        water_high1.append(mx1)
mx2=high[-1]   
for i in range(len(high)-2):
    if mx2<high[-i-2]:
        mx2 = high[-i-2]
        water_high2.append(mx2)
    else:
        water_high2.append(mx2)
water_high2.reverse()

water_high_final = []
for i in range(len(water_high1)):
    if water_high1[i]<water_high2[i]:
        water_high_final.append(water_high1[i])
    else:
        water_high_final.append(water_high2[i])

print(water_high_final)