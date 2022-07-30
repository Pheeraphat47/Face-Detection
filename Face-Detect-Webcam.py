import cv2 # import opencv

cap = cv2.VideoCapture(0) # สร้างตัวแปรสำหรับวิดีโอ
haarcascade = cv2.CascadeClassifier('Open-CV-Model.xml') # สร้างตัวแปรสำหรับอ่านโมเดล

while cap.isOpened(): # สร้างลูปเพื่อนอ่านรูปทีละเฟรมจนกว่าจะหมด

    _, img = cap.read() # รับภาพจากวิดีโอทีละเฟรม

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # แปลงภาพที่ได้เป็นสีขาว - ดำ
    faces = haarcascade.detectMultiScale(gray, 1.1, 4) # เอารูปที่ได้เข้าโมเดล

    for (x, y, w, h) in faces: # สร้างลูปสำหรับมารก์ตำแหน่งใบหน้าทั้งหมด
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Output', img) # แสดงผลรูป

    if cv2.waitKey(1) & 0xFF == ord('e'): # waitKey(1)จะแสดงเฟรม 1ms  , ให้กด e เพื่อออกจา่กโปรแกรม
         break
    
cap.release()
cv2.destroyAllWindows()