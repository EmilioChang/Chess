import Square from "./Square.mjs";
import Rook from "./Pieces/Rook.mjs";
import Knight from "./Pieces/Knight.mjs";
import Bishop from "./Pieces/Bishop.mjs";
import Queen from "./Pieces/Queen.mjs";
import King from "./Pieces/King.mjs";
import Pawn from "./Pieces/Pawn.mjs";

export class Board {
  constructor() {
    this.board = [];
    this.createBoard();
  }

  createBoard = () => {
    for (let i = 0; i < 8; i++) {
      let row = [];
      for (let j = 0; j < 8; j++) {
        row.push(new Square(null, i, j));
      }
      this.board.push(row);
    }

    this.board[7][0] = new Square(new Rook(true), 7, 0);
    this.board[7][1] = new Square(new Knight(true), 7, 0);
    this.board[7][2] = new Square(new Bishop(true), 7, 0);
    this.board[7][3] = new Square(new Queen(true), 7, 0);
    this.board[7][4] = new Square(new King(true), 7, 0);
    this.board[7][5] = new Square(new Bishop(true), 7, 0);
    this.board[7][6] = new Square(new Knight(true), 7, 0);
    this.board[7][7] = new Square(new Rook(true), 7, 0);

    for (let i = 0; i < 8; i++) {
      this.board[6][i] = new Square(new Pawn(true), i, 1);
    }

    this.board[0][0] = new Square(new Rook(false), 0, 0);
    this.board[0][1] = new Square(new Knight(false), 0, 1);
    this.board[0][2] = new Square(new Bishop(false), 0, 2);
    this.board[0][3] = new Square(new Queen(false), 0, 3);
    this.board[0][4] = new Square(new King(false), 0, 4);
    this.board[0][5] = new Square(new Bishop(false), 0, 5);
    this.board[0][6] = new Square(new Knight(false), 0, 6);
    this.board[0][7] = new Square(new Rook(false), 0, 7);

    for (let i = 0; i < 8; i++) {
      this.board[1][i] = new Square(new Pawn(false), 0, i);
    }
  };

  getBoard = () => {
    return this.board;
  };

  getSquare = (x, y) => {
    return this.board[x][y];
  };

  setSquare = (x, y, piece) => {
    this.board[x][y] = piece;
  };

  printBoard = () => {
    for (let i = 0; i < 8; i++) {
      let rowString = `${i + 1}`;

      for (let j = 0; j < 8; j++) {
        let pieceSymbol;
        try {
          pieceSymbol = this.board[i][j].getPiece().pieceSymbol();
        } catch (e) {
          pieceSymbol = "-";
        }
        rowString += ` ${pieceSymbol}`;
      }

      console.log(rowString);
    }
    console.log("  A B C D E F G H");
  };
}

let board = new Board();
board.printBoard();
