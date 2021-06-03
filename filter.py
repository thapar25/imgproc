import cv2

def apply_filter():
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    dog = cv2.imread('dog.png')


    def apply(dog, fc, x, y, w, h):
        face_width = w
        face_height = h

        dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
        for i in range(int(face_height * 1.75)):
            for j in range(int(face_width * 1.5)):
                for k in range(3):
                    if dog[i][j][k] < 235:
                        fc[y + i - int(0.375 * h) - 1][x + j -
                                                    int(0.35 * w)][k] = dog[i][j][k]
        return fc


    webcam = cv2.VideoCapture(0)
    while True:
        
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray, 1.19, 7)

        for (x, y, w, h) in fl:
            im = apply(dog, im, x, y, w, h)

        cv2.imshow('Filter Applied', im)
        key = cv2.waitKey(30) & 0xff
        if key == 27:  # The Esc key
            break


if __name__ == '__main__':
    apply_filter()
