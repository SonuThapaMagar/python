import cv2
import time
import os

#Creating folder
save_folder = "dataset"
os.makedirs(save_folder, exist_ok=True)

#Opens the webcamera(0 is usally the default laptop camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Starting photo capture...")
time.sleep(3) # Gives you time to hold your hand up

#Take 10 pictures
for i in range(1, 11):
    ret, frame = cap.read()
    
    if ret:
        filename = os.path.join(save_folder, f"A1{i:02d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Captured photo {i}/20 → {filename}")
    else:
        print(f"Failed to capture photo {i}")
    
    # Wait 2 seconds before the next photo
    if i < 10:
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()
print("Dataset collection complete!")