import smartpy as sp

class Plant(sp.Contact):

    def __init__(self, _name):
        self.init(player = sp.map(), stat = sp.record(name = _name, attack = sp.int(0), defence = sp.int(0), health = sp.int(100), growth_rate = sp.int(5), is_alive = True, special_move = []))


    @sp.entry_point
    def assignChar(self, params):
        sp.verify(~ self.data.player.contains(sp.sender), "User already have a character")
        self.data.player[sp.sender] = self.data.stat
        self.data.player[sp.sender].name = params.name

    @sp.entry_point
    def attack(self, params):
        self.data.player[sp.sender].attack += params.attack

    @sp.entry_point
    def defence(self, params):
        self.data.player[sp.sender].defence += params.defence

    @sp.entry_point
    def createMove(self, params):
        sp.verify(~ self.data.player.contains(sp.sender), "User already have a character")
        self.data.player[sp.sender].special_move = params.moves

    @sp.entry_point
    def endGame(self, params):
        sp.verify(self.data.player[sp.sender].health == 0, "You are not dead")
        self.data.player[sp.sender].is_alive = False