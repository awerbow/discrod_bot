import os
import time
import pyautogui as pc

end = 0


def clear():
    global end
    coord = pc.locateOnScreen('src/target.png', confidence=0.95)
    if coord:
            end = 0
            pc.rightClick(coord[0:2])
            with pc.hold('shift'):
                return pc.click(pc.locateCenterOnScreen('src/delete.png', grayscale=True))
    pc.press('pageup')
    end += 1


os.startfile(r"C:\Users\Artyo\OneDrive\Рабочий стол\Discord")

while end < 10:
    time.sleep(1)
    clear()
else:
    print('•> СООБЩЕНИЯ ОЧИЩЕНЫ ✅')