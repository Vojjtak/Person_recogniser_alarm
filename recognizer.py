import cv2
from ultralytics import YOLO
from playsound import playsound


class PersonRecognizer:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.cap = cv2.VideoCapture(0)

    def recognizer(self):
        while True:
            success, frame = self.cap.read()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if success:
                results = self.model.predict(frame, stream=True)
                names = self.model.names
                for result in results:
                    for c in result.boxes.cls:
                        if 'person' in names[int(c)]:
                            print('Person is there!')
                            playsound('alarm.mp3', True)


        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    call = PersonRecognizer()
    call.recognizer()
