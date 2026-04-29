class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start: int, end: int) -> None:
        self.decks = []
        r1, c1 = start
        r2, c2 = end
        if r1 == r2:
            for i in range(min(c1, c2), max(c1, c2) + 1):
                self.decks.append(Deck(r1, i))

        elif c1 == c2:
            for i in range(min(r1, r2), max(r1, r2) + 1):
                self.decks.append(Deck(i, c1))
        self.is_drowned: bool = False

    def get_deck(self, row: int, column: int) -> set[int]:
        for deck in self.decks:
            if row == deck.row and column == deck.column:
                return deck
        return None

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)
        if not deck:
            return None

        if not deck.is_alive:
            return "hit" if not self.is_drowned else "sunk"

        deck.is_alive = False

        for deckk in self.decks:
            if deckk.is_alive:
                self.is_drowned = False
                return "hit"

        self.is_drowned = True
        return "sunk"


class Battleship:
    def __init__(self, ships: list) -> None:
        self.ships = []
        self.field = {}
        for ship_data in ships:
            ship = Ship(ship_data[0], ship_data[1])
            self.ships.append(ship)

            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple) -> str:
        if location not in self.field:
            return "Miss!"

        ship = self.field[location]
        row, column = location

        result = ship.fire(row, column)

        if result == "hit":
            return "Hit!"
        elif result == "sunk":
            return "Sunk!"
