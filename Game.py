

class Game:
    def __init__(self) -> None:
        play = self.init()

    def init(self) -> bool:
        inp = input("Play or Watch (P|W): ").lower()
        if inp.startswith("p"):
            return True
        elif inp.startswith("w"):
            return False
        else:
            return self.init()