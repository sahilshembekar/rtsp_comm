import cv2

rtsp_url = 'http://server_ip:port_no'  # Replace with the actual RTSP server URL

# Create a VideoCapture object and open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    # Read frame-by-frame from the RTSP stream
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
