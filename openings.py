# I may switch this to use a more robust opening book, like the one in the python-chess package.
OPENING_NAMES = {
    ('e4', 'c5'): 'Sicilian Defense',
    ('e4', 'c5', 'Nf3', 'd6', 'd4', 'cxd4', 'Nxd4', 'Nf6', 'Nc3', 'a6'): 'Sicilian Defense,'
                                                                         ' Najdorf Variation',
    ('e4', 'c5', 'Nf3', 'd6', 'd4', 'cxd4', 'Nxd4', 'Nf6', 'Nc3', 'g6'): 'Sicilian Dragon',
    ('e4', 'c5', 'Nf3', 'd6', 'd4', 'cxd4', 'Nxd4', 'g6'): 'Sicilian Defense, Accelerated Dragon',
    ('e4', 'c5', 'Nf3', 'Nc6'): 'Old Sicilian',
    ('e4', 'c6'): 'Caro-Kann Defense',
    ('e4', 'e6'): 'French Defense',
    ('e4', 'd5'): 'Scandinavian Defense',
    ('e4', 'Nf6'): "Alekhine's Defense",
    ('e4', 'Nc6'): 'Nimzowitsch Defense',
    ('e4', 'g6'): 'Modern Defense',
    ('e4', 'e5'): "King's Pawn Game",
    ('e4', 'e5', 'Nc3'): 'Vienna Game',
    ('e4', 'e5', 'd4'): 'Center Game',
    ('e4', 'e5', 'f4'): "King's Gambit",
    ('e4', 'e5', 'Nf3', 'Nf6'): "Petrov's Defense",
    ('e4', 'e5', 'Nf3', 'f5'): 'Latvian Gambit',
    ('e4', 'e5', 'Nf3', 'd6'): 'Philidor Defense',
    ('e4', 'e5', 'Nf3', 'd5'): 'Elephant Gambit',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bb5'): 'Ruy Lopez',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'a6'): 'Ruy Lopez, Morphy Defense',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'd6'): 'Ruy Lopez, Steinitz Defense',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'Nf6'): 'Ruy Lopez, Berlin Defense',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bc4'): 'Italian Game',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'Bc5'): 'Giuco Piano',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'Bc5', 'b4'): 'Italian Game, Evans Gambit',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'Nf6', 'Ng5'): 'Fried Liver Attack',
    ('e4', 'e5', 'Nf3', 'Nc6', 'Nc3'): "Three Knight's Game",
    ('e4', 'e5', 'Nf3', 'Nc6', 'Nc3', 'Nf6'): "Four Knight's Game",
    ('e4', 'e5', 'Nf3', 'Nc6', 'd4'): 'Scotch Game',
    ('e4', 'e5', 'Nf3', 'Nc6', 'c3'): 'Ponziani Opening',
    ('d4', 'Nf6'): 'Indian Defense',
    ('d4', 'Nf6', 'c4', 'g6'): "King's Indian Defense",
    ('d4', 'Nf6', 'c4', 'g6', 'Nc3', 'd5'): 'Grünfeld Defense',
    ('d4', 'Nf6', 'c4', 'e6', 'Nc3', 'Bb4'): 'Nimzo-Indian Defense',
    ('d4', 'Nf6', 'c4', 'e6', 'Nf3', 'Bb4+'): 'Bogo-Indian Defense',
    ('d4', 'Nf6', 'c4', 'c5', 'd5'): 'Benoni Defense',
    ('d4', 'Nf6', 'c4', 'c5', 'd5', 'b5'): 'Benko Gambit',
    ('d4', 'd5'): "Queen's Pawn Game",
    ('d4', 'd5', 'c4'): "Queen's Gambit",
    ('d4', 'd5', 'c4', 'e6'): "Queen's Gambit Declined",
    ('d4', 'd5', 'c4', 'c6'): 'Slav Defense',
    ('d4', 'f5'): 'Dutch Defense',
    ('c4',): 'English Opening',
    ('Nf3',): 'Reti Opening',
    ('a3',): 'Anderssen Opening',
    ('a4',): 'Ware Opening',
    ('b3',): 'Nimzo-Larsen Attack',
    ('b4',): 'Polish Opening',
    ('c3',): 'Saragossa Opening',
    ('d3',): 'Mieses Opening',
    ('e3',): "Van't Krujis Opening",
    ('f3',): "Gedult's Opening",
    ('f4',): 'Bird Opening',
    ('g3',): 'Hungarian Opening',
    ('g4',): 'Grob Opening',
    ('h3',): 'Clemenz Opening',
    ('h4',): 'Kadas Opening',
}
