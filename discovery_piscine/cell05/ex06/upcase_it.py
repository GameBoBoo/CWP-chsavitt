#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่ (len เท่ากับ 2 เพราะ index 0 คือชื่อโปรแกรม)
if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")