
import cv2
import numpy as np
import pyautogui
import HandTrackingModule as htm


pyautogui.FAILSAFE = False #instrução para pyautogui não encerrar quando mouse sair da área da tela

detector=htm.HandDetector(detectionCon=0.8, maxHands=1)

larguraVideo, alturaVideo = 640, 480  #Medidas câmera video

video=cv2.VideoCapture(0)
video.set(3, larguraVideo)
video.set(4, alturaVideo)

screen_w, screen_h = pyautogui.size()

frameR = 100
ativar_click = 0

while True:
    ret,frame=video.read()
    frame = cv2.flip(frame, 1)
    maos,img=detector.findHands(frame)
    if maos:
        lmList=maos[0]
        dedos=detector.fingersUp(lmList)
        ponto_9 = lmList['lmList'][9] #ponto 9 conforme pontos de identificação da mão
        x, y, z = ponto_9

        cv2.rectangle(frame, (frameR+80, frameR+80), (larguraVideo-frameR, alturaVideo-frameR), (102, 255, 102), 2)
        cv2.circle(frame, (x,y), 6, (102, 255, 102), -1)

        index_x = np.interp(x, (frameR+80, larguraVideo-frameR), (0, screen_w))
        index_y = np.interp(y, (frameR+80, alturaVideo-frameR), (0, screen_h)) 
        pyautogui.moveTo(index_x, index_y)
        if dedos == [1, 1, 0, 0, 1]:
            if ativar_click == 0:
                ativar_click = 1
            else:
                ativar_click = 0
        if ativar_click == 1:
            cv2.rectangle(img, (0, 450), (150, 480),(0, 0, 0), -2)
            cv2.putText(frame, 'Click Ativado', (8,470), cv2.FONT_HERSHEY_COMPLEX, 0.5, (102, 255, 51), 1, cv2.LINE_AA) 
            if dedos == [1, 0, 1, 1, 1]:
                pyautogui.click()
            if dedos == [0, 0, 0, 0, 0]:
                pyautogui.mouseDown()
            if dedos == [1, 1, 1, 1, 1]:
                pyautogui.mouseUp()
            if dedos == [1, 1, 0, 1, 1]:
                pyautogui.click(button='right')

    cv2.imshow("Tela",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

