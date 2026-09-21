#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่
if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = text.count('z')
    
    # ถ้าพบตัวอักษร z อย่างน้อย 1 ตัว ให้พิมพ์ 'z' ตามจำนวนที่พบ
    if count > 0:
        print("z" * count)
    else:
        print("none")