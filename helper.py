import math
import socket


def createMessage(type, message, debug=False):
    ret = [len(message) + 3, 0, type]
    for i in range(len(message)):
        if message[i] == "byte":
            message[i] = 0
        if message[i] > 255:
            if message[i + 1] != "byte":
                print("Error: Overflow")
                message[i] %= 256
            else:
                message[i + 1] = int(message[i] / 256)
                message[i] %= 256
        ret.append(message[i])
    return ret


def aToD(string):
    ret = []
    for c in string:
        ret.append(ord(c))
    return ret


def strForm(arr):
    ret = [len(arr)] + arr
    return ret


def hexPrint(prefix, data):
    print(prefix)
    s = str(data.hex())
    s_spaces = ""
    index = 0
    for i in range(int(len(s) * 1.5)):
        if i % 3 == 2:
            s_spaces = s_spaces + " "
        else:
            s_spaces = s_spaces + s[index]
            index += 1
    print(s_spaces)


def send(s, message):  # Returns type, data
    s.sendall(bytes(message))
    hexPrint("Sending:", bytes(message))


def request(s):
    received = s.recv(65536)
    msgtype, data = int(received[2]), received[3:]

    if msgtype == 2:
        print("Disconnected, reason: " + repr(data))
    else:
        hexPrint("Received (" + str(msgtype) + "):", data)

    return (msgtype, data)


def joinServer(s, version, player, uuid):
    version_msg = createMessage(1, version)
    send(s, version_msg)
    msgtype, data = request(s)

    pslot = int(data[0])

    player_msg = createMessage(4, player.generateBytes(pslot))
    send(s, player_msg)

    uuid_msg = createMessage(68, uuid)
    send(s, uuid_msg)

    HP_msg = createMessage(16, player.generateHP(pslot))
    send(s, HP_msg)

    mana_msg = createMessage(42, player.generateMana(pslot))
    send(s, mana_msg)

    buffs_msg = createMessage(50, player.generateBuffs(pslot))
    send(s, buffs_msg)

    for slot in player.inventory:
        slot_msg = createMessage(5, slot.genSlotMessage(pslot))
        send(s, slot_msg)

    rwd_msg = createMessage(6, [])
    send(s, rwd_msg)
    msgtype, data = request(s)

    tiles_msg = createMessage(8, player.generateSpawnTiles())
    send(s, tiles_msg)

    msgtype, data = request(s)

    netModuleZeros = 0
    while True:
        msgtype, data = request(s)

        if msgtype == 10:
            pass  # Handle tile input
        elif msgtype == 11:
            pass  # handle section tile frame
        elif msgtype == 21:
            pass  # handle update item drop
        elif msgtype == 22:
            pass  # handle update item owner
        elif msgtype == 23:
            pass  # handle npc update
        elif msgtype == 83:
            pass  # handle update npc kill count
        elif msgtype == 49:
            pass  # handle complete connection and spawn
        elif msgtype == 57:
            pass  # handle update good evil
        elif msgtype == 7:
            pass  # handle world info
        elif msgtype == 101:
            pass  # handle update shield strengths
        elif msgtype == 136:
            pass  # handle sync cavern monster type
        elif msgtype == 82:
            print(int(data[0]))
            if int(data[0]) == 0:
                netModuleZeros += 1
                if netModuleZeros == 3:
                    break
            # handle net modules

    spawn_msg = createMessage(12, player.generateSpawn(pslot))
    send(s, spawn_msg)

    module_msg = createMessage(82, [6, 0, 14, 0, 0, 0, 0, 0, 63])
    send(s, module_msg)

    msgtype, data = request(s)  # 74 - angler quest
    msgtype, data = request(s)  # 139 - set as host
    msgtype, data = request(s)  # 74 - angler quest
    msgtype, data = request(s)  # 129 - finished connecting
