import cv2
import os
import numpy as np
from keras.models import load_model
import webbrowser


model = load_model('/home/jjespper/Escritorio/modelo_generator_final_7cats_nothing.h5')

marcas = {0:'Budweiser',
          1:'Coronita',
          2:'Heineken',
          3:'Mahou',
          4:'Nothing',
          5:'Pilsner_urquell',
          6:'San_miguel'}


# IMAGES_FOLDER = os.path.join('/home/jjespper/masterIronhack/capturas_beers')
video = cv2.VideoCapture(0)
roi_start = 50
roi_size = 200
cnt = 0


budweiser_web = "https://en.wikipedia.org/wiki/Budweiser"
mahou_web = "https://es.wikipedia.org/wiki/Mahou"
pilsner_urquell_web = "https://es.wikipedia.org/wiki/Pilsner_Urquell"
san_miguel_web = "https://es.wikipedia.org/wiki/Cerveza_San_Miguel"
coronita_web = 'https://es.wikipedia.org/wiki/Corona_Extra'
heineken_web = 'https://es.wikipedia.org/wiki/Heineken'

while True:

    ret, frame = video.read()

    w = frame.shape[1]
    h = frame.shape[0]
    hcenter = w // 2
    vcenter = h // 2

    roi = frame[roi_start:roi_start + roi_size,
          roi_start:roi_start + roi_size]

    new_array = cv2.resize(roi, (300, 300))
    new_array_recolor = cv2.cvtColor(new_array, cv2.COLOR_BGR2RGB)
    asd = np.expand_dims(new_array_recolor, axis=1)
    asd = np.array(asd).reshape(-1, 300, 300, 3)
    asd = asd / 255.
    classes = model.predict(asd)

    color = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    color_cropped = color[:, (hcenter - h // 2):(hcenter + h // 2)]

    cv2.rectangle(frame, (roi_start, roi_start), (roi_start + roi_size, roi_start + roi_size), (0, 255, 0), 0)

    total_probs = classes

    confidence = np.amax(total_probs)

    predict_marca = marcas[np.argmax(total_probs)]

    # k = cv2.waitKey(1) & 0xff
    # if k == ord('s'):  # S to web

    if predict_marca == 'Budweiser' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(budweiser_web)
            cnt = 0

    elif predict_marca == 'Mahou' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(mahou_web)
            cnt = 0

    elif predict_marca == 'Pilsner_urquell' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(pilsner_urquell_web)
            cnt = 0

    elif predict_marca == 'San_miguel' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(san_miguel_web)
            cnt = 0

    elif predict_marca == 'Coronita' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(coronita_web)
            cnt = 0

    elif predict_marca == 'Heineken' and confidence > 0.95:
        cnt += 1
        if cnt == 180:
            webbrowser.open_new(heineken_web)
            cnt = 0

    cv2.putText(frame,
                predict_marca + ' ' + str(confidence) if confidence > 0.5 else 'Cerveza no identificada!',
                (int(roi_start),
                 int(roi_start + .09 * roi_size)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255))

    cv2.imshow('my_webcam_frame', frame)
    cv2.imshow('roi', new_array)

    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):  # escape pressed
        break

cv2.destroyAllWindows()
video.release()
# return IMAGES_FOLDER


