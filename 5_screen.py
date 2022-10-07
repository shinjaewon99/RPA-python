import pyautogui

# 스크린  샷 찍기
# img = pyautogui.screenshot()

# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 360,52 46,162,241 #2EA2F1

pixel = pyautogui.pixel(360, 52)

print(pixel)
