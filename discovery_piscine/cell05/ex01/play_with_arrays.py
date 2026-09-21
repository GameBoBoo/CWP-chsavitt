#!/usr/bin/env python3

# 1. สร้างลิสต์ตัวเลขตั้งต้นตามตัวอย่างในโจทย์
original = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. วนลูปบวกเพิ่มตัวละ 2 ไปใส่ใน new_array
new_array = []
for x in original:
    new_array.append(x + 2)

# 3. แสดงผลทั้งสองลิสต์
print(f"Original array: {original}")
print(f"New array: {new_array}")