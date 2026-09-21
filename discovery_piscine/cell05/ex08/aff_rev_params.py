#!/usr/bin/env python3
import sys

# sys.argv มีชื่อโปรแกรมอยู่ที่ index 0 เสมอ
# ดังนั้นถ้าพารามิเตอร์น้อยกว่า 2 ตัว แปลว่า len(sys.argv) < 3
if len(sys.argv) < 3:
    print("none")
else:
    # นำเฉพาะพารามิเตอร์ตั้งแต่ตัวแรกเป็นต้นไปมาวนลูปย้อนหลัง
    for param in reversed(sys.argv[1:]):
        print(param)