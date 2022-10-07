from turtle import width
import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")

print(file_menu)
pyautogui.click(file_menu)



file_icon = pyautogui.locateOnScreen("trash_icon.png")

pyautogui.moveTo(file_icon)


#속도 개선

# 1.GrayScale
# file_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(file_icon)

# 2.범위 지정
# file_icon = pyautogui.locateOnScreen("trash_icon.png",  region=(x, y, width , height )
# pyautogui.moveTo(file_icon)


# 3. 정확도 조정
file_btn = pyautogui.locateOnScreen("run_btn.png" , confidence=0.9)
pyautogui.moveTo(file_btn)

