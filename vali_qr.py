import cv2
import qrcode
from pyzbar.pyzbar import decode

# Function to validate the QR code
def is_valid_qr_code(data):
    # Implement your validation logic here
    # For example, you could check if the QR code data is in a valid format
    # or if the data matches a list of approved QR codes/tickets
    approved_qr_codes = ["qr_code_1", "qr_code_2", "qr_code_3"]
    return data in approved_qr_codes

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Decode QR codes from the frame
    decoded_objects = decode(frame)
    
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        if is_valid_qr_code(data):
            print("Approved:", data)
            # Implement further actions for approved QR codes
            # For example, you can display a message, save attendance, etc.
        else:
            print("Rejected:", data)
            # Implement actions for rejected QR codes
        
        # Draw a bounding box around the QR code
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(frame, [hull], True, (0, 255, 0), 2)
        else:
            cv2.polylines(frame, [points], True, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)
    
    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
