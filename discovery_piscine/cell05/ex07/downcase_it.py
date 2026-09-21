#!/usr/bin/env python3
import sys

# ตรวจสอบว่าส่งพารามิเตอร์มา 1 ตัวพอดีหรือไม่ (len เท่ากับ 2 เพราะตำแหน่งที่ 0 คือชื่อโปรแกรม)
if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")