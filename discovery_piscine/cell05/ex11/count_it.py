#!/usr/bin/env python3
import sys

# ดึงเฉพาะรายการพารามิเตอร์ที่ส่งเข้ามา (ตัด sys.argv[0] ที่เป็นชื่อไฟล์ออก)
args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for param in args:
        print(f"{param}: {len(param)}")