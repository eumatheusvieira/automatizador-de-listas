import pyautogui
from time import sleep

pyautogui.click(687,386, duration=2)
pyautogui.write("Math")
pyautogui.click(680,411, duration=2)
pyautogui.write("123456")
pyautogui.click(587,446, duration=2)

with open("produtos.txt", 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]

        pyautogui.click(430,376, duration=2)
        pyautogui.write(produto)
        pyautogui.click(432,401, duration=2)
        pyautogui.write(quantidade)
        pyautogui.click(434,422, duration=2)
        pyautogui.write(preco)
        pyautogui.click(313,586, duration=2)


