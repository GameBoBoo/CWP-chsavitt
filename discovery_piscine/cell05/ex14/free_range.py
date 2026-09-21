#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 2 ตัวพอดีหรือไม่ (len เท่ากับ 3 เพราะ argv[0] คือชื่อโปรแกรม)
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # range(start, end + 1) เพื่อให้รวมตัวเลขตัวสุดท้ายด้วย
    result = list(range(start, end + 1))
    print(result)