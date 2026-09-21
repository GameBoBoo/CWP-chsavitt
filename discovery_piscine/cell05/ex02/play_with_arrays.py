#!/usr/bin/env python3

# ลิสต์ตัวเลขตั้งต้นตามโจทย์
original = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างลิสต์ใหม่ โดยเลือกเฉพาะตัวที่มากกว่า 5 แล้วบวกเพิ่ม 2
new_array = []
for x in original:
    if x > 5:
        new_array.append(x + 2)

# แสดงผลตามตัวอย่างโจทย์
print(original)
print(new_array)