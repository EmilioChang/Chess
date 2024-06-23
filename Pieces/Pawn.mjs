import Square from "../Game/Square.mjs";
import Piece from "./Piece.mjs";

export default class Pawn extends Piece {
  constructor(isWhite) {
    super(isWhite);
    this.madeFirstMove = false;
  }

  pieceSymbol = () => {
    return this.isWhite ? "♟" : "♙";
  };

  move = (board, initialSquare, destinationSquare) => {
    let dx = Math.abs(initialSquare.x - destinationSquare.x);

    if (dx > 2) return false;
    if (dx === 2) {
      if (
        this.madeFirstMove ||
        this.isDiagonalMove(initialSquare, destinationSquare)
      )
        return false;
    }

    if (this.isForwardMove(initialSquare, destinationSquare)) {
      return this.isValidPath(board, initialSquare, destinationSquare);
    }

    // check if player wants to take a pice
    if (this.isDiagonalMove(initialSquare, destinationSquare)) {
      //taking a piece means going 1 square diagonal. in other words,
      // changing 'x' by -1 (if white) or +1 (if black)
      // 'y' by -1 or +1

      if (Math.abs(initialSquare.y - destinationSquare.y) !== 1) return false;

      if (this.isWhite) {
        if (initialSquare.x - 1 !== destinationSquare.x) return false;
      } else {
        if (initialSquare.x + 1 !== destinationSquare.x) return false;
      }
    } else {
      return true;
    }

    this.madeFirstMove = true;
    return true;
  };

  isValidPath = (board, initialSquare, destinationSquare) => {
    let dx = Math.abs(initialSquare.x - destinationSquare.x);

    if (dx === 2) {
      // If wants to move twice
      // check if square at y+1 has a piece
      let x = initialSquare.x + 1;
      if (board[x][initialSquare.y].piece) return false;
    }

    if (destinationSquare.piece) return false;

    return true;
  };

  isStraightMove = (initialSquare, destinationSquare) => {
    return initialSquare.y === destinationSquare.y;
  };

  isForwardMove = (initialSquare, destinationSquare) => {
    if (this.isWhite) {
      if (destinationSquare.x < initialSquare.x) return true;
    } else {
      if (destinationSquare.x > initialSquare.x) return true;
    }

    return false;
  };

  isDiagonalMove = (initialSquare, destinationSquare) => {
    let dx = Math.abs(initialSquare.x - destinationSquare.x);
    let dy = Math.abs(initialSquare.y - destinationSquare.y);

    return dx === dy;
  };
}
