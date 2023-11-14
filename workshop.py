import os

print("ป้อนตัวเลขเพื่อเริ่มต้นการทำงาน \n1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล \n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4. เลือกวิชาและลบไฟล์ \n0. จบการทํางาน")

try:
    select = input("โปรดเลือกคำสั่งที่คุณต้องการใช้งาน: ")
    if select not in ["0","1","2","3","4"] :
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")

    if select == "1" :
        subjectName = input("โปรดใส่ชื่อรายวิชาของคุณ (.txt): ")

        if ".txt" not in subjectName :
            print("สกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")

        else :
            subjectDetail = open(f"{subjectName}.txt", "w", encoding="utf-8")
            stuName = input("กรุณาป้อนชื้อ - นามสกุล: ")
            midScore = int(input("กรุณาป้อนคะแนนกลางภาค: "))
            finalScore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
            accuScore = int(input("กรุณาป้อนคะแนนก็บ: "))
            totalScore = midScore + finalScore + accuScore

            if totalScore >= 50 :
                result = "ผ่าน"
                subjectDetail.write(f"นักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                subjectDetail.close()

            else : 
                result = "ไม่ผ่าน"
                subjectDetail.write(f"นักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                subjectDetail.close()

    if select == "2" :

        subjectFileName = os.listdir()
        if not subjectFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for i in subjectFileName :
                print(i)
            fileSelect = input("คุณต้องการเปิดไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")
            if fileSelect not in subjectFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif fileSelect in subjectFileName :
                subjectMod = open(f"{fileSelect}", "a+", encoding="utf-8")
                stuName = input("กรุณาป้อนชื้อ - นามสกุล: ")
                midScore = int(input("กรุณาป้อนคะแนนกลางภาค: "))
                finalScore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
                accuScore = int(input("กรุณาป้อนคะแนนก็บ: "))
                totalScore = midScore + finalScore + accuScore

                if totalScore >= 50 :
                    result = "ผ่าน"
                    subjectMod.write(f"นักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                    print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                    subjectMod.close()
                
                else : 
                    result = "ไม่ผ่าน"
                    subjectMod.write(f"นักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                    print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                    subjectMod.close

    if select == "3" :
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for i in subjectFileName :
                print(i)
            fileSelect = input("คุณต้องการเปิดไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSelect not in subjectFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif fileSelect in subjectFileName :
                subjectRead = open(f"{fileSelect}", "r", encoding="utf-8")
                sRead = subjectRead.read()
                print(sRead)

    if select == "4" :
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for i in subjectFileName :
                print(i)
            fileSelect = input("คุณต้องการเปิดไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSelect not in subjectFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif fileSelect in subjectFileName :
                os.remove(f"{fileSelect}")
                print("ลบไฟล์เรียบร้อย")

    if select == "0" :
        exit

except Exception :
    print("เกิดข้อผิดพลาด กรุณาตรวจสอบข้อมูลที่ป้อนให้ถูกต้อง")