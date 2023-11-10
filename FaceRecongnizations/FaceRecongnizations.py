import dlib
import cv2
import face_recognition



# get the image
known_image = face_recognition.load_image_file("image/Arbab_Sabir.jpg")


# encode the image
known_image_encoding = face_recognition.face_encodings(known_image)[0]

# veriables for image
face_locations = []
face_encodings = []
face_names = []

# open the camera
video_capture = cv2.VideoCapture(0)

while True:
    # capture the frame
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    # loop through each face in this frame of video
    for(top, righ, bottm, left), face_encodings in zip(face_locations,face_encodings):
        # see if the face is a match for the known face(s)
        match = face_recognition.compare_faces([known_image_encoding], face_encodings)
        name = "Unknown"
        
        if match[0]:
            name = "Arbab Sabir"
        else:
            name = "Unknown"
        
        # draw a box around the face
        cv2.rectangle(frame, (left, top), (righ, bottm), (0, 0, 255), 2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottm - 6), font, 1.0, (255, 255, 255), 1)
    
    # display the resulting image
    cv2.imshow('Video', frame)
    
    #brake loop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

        
