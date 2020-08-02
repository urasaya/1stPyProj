#นางสาวอุรัสยา นาคเปรม 6109684768
#เขียนPython code รับข้อมูลเข้ามาจำนวนหนึ่ง แล้วแสดงผลค่าสูงสุด ต่ำสุด และ ค่าเฉลี่ย ของข้อมูลชุดดังกล่าว
import math
x = list(map(int, input("Enter a multiple value: ").split()))
#หาค่าสูงสุด
maximum = math.max(x)
#หาค่าต่ำสุด
minimum = min(x)
#หาค่าเฉลี่ย
avg = sum(x)/len(x)
print("The maximum value is {:5.2f} The minimum value is {:5.2f} The average is {:5.2f}.".format(maximum,minimum,avg))