import helper as h
from character import Character
from inventorySlot import InventorySlot
from itemID import itemID
import function as r
import time
import socket
import socks

# 设置代理
# socks.set_default_proxy(socks.HTTP, addr='42.6.114.140', port=4176)
# socket.socket = socks.socksocket


HOST = "121.62.18.209"
PORT = 7777
VERSION = h.strForm(h.aToD("Terraria248"))
PLAYER = Character()
# PLAYER.name = r.random_str(8)  # 暂时取随机的名字
PLAYER.name = "菜b"
PLAYER.inventory[59] = InventorySlot(59, 0, 1, 0)
PLAYER.inventory[60] = InventorySlot(60, 0, 1, 0)
PLAYER.inventory[61] = InventorySlot(61, 0, 1, 0)
UUID = h.strForm(h.aToD(
    r.random_str(8) + "-" + r.random_str(4) + "-" + r.random_str(4) + "-" + r.random_str(4) + "-" + r.random_str(
        12)))  # 生成随机的UUID

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    h.joinServer(s, VERSION, PLAYER, UUID)
    a = 0
    while True:
        h.sendMsg(s, f"{a}")
        a += 1
        time.sleep(0.5)
    time.sleep(30)
