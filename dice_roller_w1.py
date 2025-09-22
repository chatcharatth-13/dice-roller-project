import random # [สำหรับสุ่มตัวเลขลูกเต๋า]

def run_dice_roller():
    """
    โปรแกรม Dice Roller ที่ทำงานใน Terminal
    อนุญาตให้ผู้ใช้ 'roll' ลูกเต๋าหรือ 'quit' ออกจากโปรแกรม
    """
    print("ยินดีต้อนรับสู่โปรแกรม Dice Roller!")
    print("คุณสามารถพิมพ์ 'roll' เพื่อทอยลูกเต๋า หรือ 'quit' เพื่อออกจากโปรแกรม")

    while True:
        command = input("\nกรุณาพิมพ์คำสั่ง (roll/quit): ").lower().strip() # [รับคำสั่งจากผู้ใช้, แปลงเป็นตัวพิมพ์เล็กและลบช่องว่างหัวท้าย]

        if command == 'quit':
            print("ลาก่อน! ขอบคุณที่ใช้บริการ")
            break # [ออกจาก loop และจบโปรแกรม]
        elif command == 'roll':
            dice_roll = random.randint(1, 6) # [สุ่มตัวเลขระหว่าง 1 ถึง 6]
            print(f"คุณทอยลูกเต๋าได้: {dice_roll} 🎲") # [แสดงผลการทอย]
        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่") # [จัดการคำสั่งที่ไม่ถูกต้อง]

# เรียกใช้ฟังก์ชันหลักของโปรแกรม
if __name__ == "__main__":
    run_dice_roller()
