import helper as h
from character import Character
from inventorySlot import InventorySlot
from itemID import itemID
import time
import socket

HOST = "localhost"
PORT = 7777
VERSION = h.strForm(h.aToD("Terraria230"))
PLAYER = Character()
PLAYER.name = "Terrarian"
PLAYER.inventory[59] = InventorySlot(59, itemID["Solar Flare Helmet"], 1, 0)
PLAYER.inventory[60] = InventorySlot(60, itemID["Solar Flare Breastplate"], 1, 0)
PLAYER.inventory[61] = InventorySlot(61, itemID["Solar Flare Leggings"], 1, 0)
UUID = h.strForm(h.aToD("ac857bff-9b56-4d26-9b17-ef1accb6dc8f"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    h.joinServer(s, VERSION, PLAYER, UUID)
    time.sleep(30)