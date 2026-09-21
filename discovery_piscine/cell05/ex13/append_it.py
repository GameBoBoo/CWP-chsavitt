#!/usr/bin/env python3
import sys

# ดึงเฉพาะพารามิเตอร์ที่ส่งเข้ามา (ตัดชื่อโปรแกรม argv[0] ออก)
args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        # ถ้าไม่ได้ลงท้ายด้วย "ism" ให้บวก "ism" ต่อท้ายแล้วพิมพ์ออกมา
        if not word.endswith("ism"):
            print(word + "ism")