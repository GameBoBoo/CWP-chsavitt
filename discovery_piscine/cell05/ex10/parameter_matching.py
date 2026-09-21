#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่ (len เท่ากับ 2 เนื่องจาก sys.argv[0] คือชื่อไฟล์)
if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    user_input = input("What was the parameter? ")
    
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")