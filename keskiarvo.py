
val1 = int(input('anna 1.luku\n'))
val2 = int(input('anna 2.luku\n'))
val3 = int(input('anna 3.luku\n'))


sum = val1 + val2 +val3
avg = sum / 3

print("lukujen",val1,',',val2, "ja",val3, "keskiarvo on","{:.2f}".format(sum))