# อ่านข้อมูลจากไฟล์ที่แฮกเกอร์ให้
with open('hackers_data.txt', 'r') as file:
    data = file.readlines()

# สร้างตัวแปรสำหรับเก็บรหัสลับ
secret_code = 0

# วนลูปผ่านแต่ละบรรทัดในข้อมูล
for line in data:
    # เริ่มต้นด้วยการแยกส่วนของข้อมูลเพื่อหาหมายเลขแรกและสุดท้าย
    numbers = [int(x) for x in line if x.isdigit()]
    # นำหมายเลขแรกและสุดท้ายมารวมกัน
    code = numbers[0] * 10 + numbers[-1]
    # เพิ่มรหัสลับที่ได้เข้าสู่ผลรวมรวม
    secret_code += code

# แสดงผลลัพธ์
print("รหัสลับคือ:", secret_code)
