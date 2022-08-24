
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def roman_numbers(num):
    if num > 10000:
        print(" Enter number less than 10000!")
        return
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "D", "XD", "L", "XL", "X", "IX", "V", "I"]
    roman = ""
    i = 0
    while num > 0:
        div = num // value[i]
        num = num % value[i]
        while div:
            roman = roman + symbol[i]
            div = div - 1
        i = i + 1
    return roman


num = int(input("Enter arabic number:"))
print("roman_numbers of ", num, "is: ", roman_numbers(num))

