import Square from "../Square.mjs";
import Piece from "./Piece.mjs";

export default class Rook extends Piece {
  constructor(isWhite) {
    super(isWhite);
  }

  pieceSymbol = () => {
    return this.isWhite ? "♜" : "♖";
  };

  move = (board, initialSquare, destinationSquare) => {
    if (destinationSquare.piece?.isWhite === this.isWhite) return false;
    return this.isValidPath(board, initialSquare, destinationSquare);
  };

  isValidPath = (board, initialSquare, destinationSquare) => {
    let min;
    let max;

    if (this.isHorizontalMove(initialSquare, destinationSquare)) {
      let row = initialSquare.x;
      min = Math.min(initialSquare.y, destinationSquare.y) + 1;
      max = Math.max(initialSquare.y, destinationSquare.y);

      for (; min < max; min++) {
        if (board[row][min].piece != null) return false;
      }

      return true;
    }

    if (this.isStraightMove(initialSquare, destinationSquare)) {
      let col = initialSquare.y;
      min = Math.min(initialSquare.x, destinationSquare.x) + 1;
      max = Math.max(initialSquare.x, destinationSquare.x);

      for (; min < max; min++) {
        if (board[min][col].piece != null) return false;
      }

      return true;
    }

    return false;
  };

  isHorizontalMove = (initialSquare, destinationSquare) => {
    return initialSquare.x === destinationSquare.x;
  };

  isStraightMove = (initialSquare, destinationSquare) => {
    return initialSquare.y === destinationSquare.y;
  };
}
