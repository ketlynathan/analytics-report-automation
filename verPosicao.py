# Ver posição do mouse (exibe continuamente)
import pyautogui
import time

print("Posicione o mouse. Pressione Ctrl+C para sair.")
time.sleep(5)
x, y = pyautogui.position()

# imprime em linha única (atualiza com \r)
print(f"Posição: x={x} y={y}", end="\r")
