# automatically generated, do not modify

# namespace: MyGame

import flatbuffers

class Monster(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonster(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Monster()
        x.Init(buf, n + offset)
        return x


    # Monster
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Monster
    def Pos(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Vec3 import Vec3
            obj = Vec3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Mana(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 150

    # Monster
    def Hp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 100

    # Monster
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Monster
    def Inventory(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def InventoryLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Color(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 3

def MonsterStart(builder): builder.StartObject(7)
def MonsterAddPos(builder, pos): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pos), 0)
def MonsterAddMana(builder, mana): builder.PrependInt16Slot(1, mana, 150)
def MonsterAddHp(builder, hp): builder.PrependInt16Slot(2, hp, 100)
def MonsterAddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def MonsterAddInventory(builder, inventory): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(inventory), 0)
def MonsterStartInventoryVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterAddColor(builder, color): builder.PrependInt8Slot(6, color, 3)
def MonsterEnd(builder): return builder.EndObject()
