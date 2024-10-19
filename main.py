import cv2
from deepface import DeepFace
camera = cv2.VideoCapture(0)


while True:
    ret, frame = camera.read()
    try:
        results = DeepFace.analyze(frame, actions=['emotion', 'race', 'gender', 'age'])
        # print(results[0]['dominant_emotion'])
        print(results)
        print(results[0]['region']['x'])
        cv2.rectangle(frame, (results[0]['region']['x'],results[0]['region']['y']), (results[0]['region']['x']+results[0]['region']['w'], results[0]['region']['y']+results[0]['region']['h']), (255,0,0), 3)
        text1 = f"Emotion:{results[0]['dominant_emotion']}"
        text2 = f"Age:{results[0]['age']}"
        text3 = f"Gender:{results[0]['dominant_gender']}"
        text4 = f"Race:{results[0]['dominant_race']}"

        position1 = (results[0]['region']['x'], results[0]['region']['y'] - 70)
        position2 = (results[0]['region']['x'], results[0]['region']['y'] - 40)
        position3 = (results[0]['region']['x'], results[0]['region']['y'] - 10)
        position4 = (results[0]['region']['x'], results[0]['region']['y'] + 20)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255,0,0)
        thickness = 2
        cv2.putText(frame, text1, position1, font, font_scale, color, thickness)
        cv2.putText(frame, text2, position2, font, font_scale, color, thickness)
        cv2.putText(frame, text3, position3, font, font_scale, color, thickness)
        # cv2.putText(frame, text4, position4, font, font_scale, color, thickness)
    except:
        print('[INFO]: No Face detected')

    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()