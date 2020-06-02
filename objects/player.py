class Player:
    def prompt(self, text):
        pass

class LocalPlayer(Player):
    def prompt(self, text):
        return input(text)

class RemotePlayer(Player):
    def prompt(self, text):
        pass


class AiPlayer(Player):
    def prompt(self, text):
        pass
