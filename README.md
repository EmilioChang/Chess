# Chess Game

Simple chess game with a GUI made with Python and auxiliary backend with Javascript.

# Installation

## Install dependencies

For **Debian-based** systems:

```bash
sudo apt intall python3-pip -y
pip install pygame
```

Then execute the `run_linux.sh` script.

For **Windows**:

```bat
pip install pygame
```

Then execute the `run_windows.bat` script.

# How to play

***Drag*** the piece you want to move to the desired location. Clicking (and releasing) the piece, and then clicking the destination square **will not** work. 

# How moves are calculated

## Rook

![](./imgs/rook_move.png)

## Knight

![](./imgs/knight_move.png)

## Bishop

![](./imgs/bishop_move.png)

## Queen

![](./imgs/queen_move.png)

## King and Pawns

No logic required. Just move one square at a time.