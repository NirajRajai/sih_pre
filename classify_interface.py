f = open('new_tweet25.txt', 'r')
tweet = f.read()
lines = tweet.split('\n')
f1 = open('dataset/booking_n.txt', 'a')
f2 = open('dataset/cleanliness_n.txt', 'a')
f3 = open('dataset/nowater.txt', 'a')
f4 = open('final/electricity_n.txt', 'a')
f5 = open('dataset/irctcstaff_n.txt', 'a')
f6 = open('dataset/late_n.txt', 'a')
f7 = open('dataset/medical_n.txt', 'a')
f8 = open('final/irctc_care.txt', 'a')
f9 = open('final/staff_n.txt', 'a')
f10 = open('final/security_n.txt', 'a')
# f11=open('final/irctc_staff_n.txt','a')
for line in lines:
    print(
        "1.Booking 2.Cleanliness 3)NoWater  4.electricity 5.irctc staff 6.late 7. medical 8. irctc_care 9.staff 10.security ")
    print(line)
    x = int(input())
    if x == 1:
        f1.write(line + '\n')
    elif x == 2:
        f2.write(line + '\n')
    elif x == 3:
        f3.write(line + '\n')
    elif x == 4:
        f4.write(line + '\n')
    elif x == 5:
        f5.write(line + '\n')
    elif x == 6:
        f6.write(line + '\n')
    elif x == 7:
        f7.write(line + '\n')
    elif x == 8:
        f8.write(line + '\n')
    elif x == 9:
        f9.write(line + '\n')
    elif x == 10:
        f10.write(line + '\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
# f11.close()