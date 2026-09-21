#!/usr/bin/env python3
import sys

# ถ้ามีพารามิเตอร์ส่งเข้ามา (len มากกว่า 1 เพราะตัวที่ 0 คือชื่อไฟล์)
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")