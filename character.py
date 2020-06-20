import helper as h
from inventorySlot import InventorySlot


class Character:
    def __init__(self):
        self.style = 0
        self.hairStyle = 0
        self.name = "Terrarian"
        self.hairDye = 0
        self.hideVisuals = 0
        self.hideVisuals2 = 0
        self.hideMisc = 0
        self.hairColor = [215, 90, 55]
        self.skinColor = [255, 125, 90]
        self.eyeColor = [105, 90, 75]
        self.shirtColor = [175, 165, 140]
        self.undershirtColor = [160, 180, 215]
        self.pantsColor = [255, 230, 175]
        self.shoeColor = [160, 105, 60]
        self.mediumcore = False
        self.hardcore = False
        self.extraAccessory = False
        self.creative = False
        self.biomeTorches = False
        self.torchGod = False
        self.currHP = 100
        self.maxHP = 100
        self.currMana = 20
        self.maxMana = 20
        self.inventory = [InventorySlot(slotID, 0, 0, 0) for slotID in range(260)]
        self.startX = 2 ** 32 - 1
        self.startY = 2 ** 32 - 1
        self.spawnX = 65535
        self.spawnY = 65535

    def generateBytes(self, playerID):
        ret = (
            [playerID, self.style, self.hairStyle]
            + h.strForm(h.aToD(self.name))
            + [self.hairDye, self.hideVisuals, self.hideVisuals2, self.hideMisc]
        )
        ret = (
            ret
            + self.hairColor
            + self.skinColor
            + self.eyeColor
            + self.shirtColor
            + self.undershirtColor
            + self.pantsColor
            + self.shoeColor
        )
        dflag = 0
        if self.mediumcore:
            dflag += 1
        if self.hardcore:
            dflag += 2
        if self.extraAccessory:
            dflag += 4
        if self.creative:
            dflag += 8
        ret.append(dflag)
        tflag = 0
        if self.biomeTorches:
            tflag += 1
        if self.torchGod:
            tflag += 2
        ret.append(tflag)
        return ret

    def generateHP(self, playerID):
        return [playerID, self.currHP, "byte", self.maxHP, "byte"]

    def generateMana(self, playerID):
        return [playerID, self.currMana, "byte", self.maxMana, "byte"]

    def generateBuffs(self, playerID):
        return [playerID] + [0 for i in range(44)]

    def generateSpawnTiles(self):
        return [
            self.startX,
            "byte",
            "byte",
            "byte",
            self.startY,
            "byte",
            "byte",
            "byte",
        ]

    def generateSpawn(self, playerID):
        return [
            playerID,
            self.spawnX,
            "byte",
            self.spawnY,
            "byte",
            0,
            "byte",
            "byte",
            "byte",
            1,
        ]
