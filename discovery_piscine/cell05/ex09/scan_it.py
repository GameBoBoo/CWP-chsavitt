#!/usr/bin/env python3
import sys
import re

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 2 ตัวพอดีหรือไม่ (len เท่ากับ 3 เพราะ index 0 คือชื่อโปรแกรม)
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # ค้นหาคำที่ตรงกันทั้งหมดในข้อความ
    matches = re.findall(re.escape(keyword), text)
    
    # ถ้าพบคำค้นหา (จำนวนมากกว่า 0) ให้แสดงจำนวนครั้ง ถ้าไม่พบให้แสดง none
    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")