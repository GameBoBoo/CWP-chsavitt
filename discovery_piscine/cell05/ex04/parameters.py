#!/usr/bin/env python3
import sys

# นับจำนวนพารามิเตอร์ทั้งหมด ลบด้วย 1 (เพื่อไม่นับชื่อไฟล์โปรแกรม)
count = len(sys.argv) - 1

print(f"Number of parameters: {count}.")