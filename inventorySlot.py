class InventorySlot:
    def __init__(self, slotID, itemID, stack, modifier):
        self.slotID = slotID
        self.itemID = itemID
        self.stack = stack
        self.modifier = modifier

    def genSlotMessage(self, playerID):
        return [
            playerID,
            self.slotID,
            "byte",
            self.stack,
            "byte",
            self.modifier,
            self.itemID,
            "byte",
        ]
