# PyChess

![Chess Board](Images/SS.png?raw=true "Title")

A chess Bot made in python with the help of PyGame. This chess bot uses Min-Max search algorithm with alpha beta pruning and iterative deepening to find the best move to play against its opponent.

It also uses a large data set of 1,30,000+ games played by GMs so that it can make the optimal opening moves.

The chess board supports moves like pawn-promotion, double pawn push, castling on king and queen side, and en passant from black's side.


## Installation

```
git clone https://github.com/DivyanshMittal-exe/PyChess.git
cd PyChess
pip install -r requirements.txt
```

## Usage

```
python -m ChessBoard
```

## Instructions:
- You play as white, while the bot plays as black
- Clicking on any white piece will show the possible legal moves and captures available.
- Selecting on any of the legal moves square will move the piece to the desired location
<hr>
<sup>During the initial phase, when a lot moves are possible, the bot might take some time to process (upto 10 sec) during which your move might not render yet</sup>