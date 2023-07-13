import cv2
from flask import Flask, Response

app = Flask(__name__)

def generate_frames():
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to JPEG format
        ret, encoded_image = cv2.imencode('.jpg', frame)

        # Yield the encoded image as a byte string
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + encoded_image.tobytes() + b'\r\n')

    # Release the video capture
    video_capture.release()

@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
