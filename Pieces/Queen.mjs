import Square from "../Game/Square.mjs";
import Piece from "./Piece.mjs";

export default class Queen extends Piece {
  constructor(isWhite) {
    super(isWhite);
  }

  move = (board, initialSquare, destinationSquare) => {
    if (destinationSquare.piece?.isWhite === this.isWhite) return false;
    return this.isValidPath(board, initialSquare, destinationSquare);
  };

  pieceSymbol = () => {
    return this.isWhite ? "♛" : "♕";
  };

  isValidPath = (board, initialSquare, destinationSquare) => {
    let stepX = destinationSquare.x > initialSquare.x ? 1 : -1;
    let stepY = destinationSquare.y > initialSquare.y ? 1 : -1;

    let x = initialSquare.x + stepX;
    let y = initialSquare.y + stepY;

    if (this.isHorizontalMove(initialSquare, destinationSquare)) {
      let row = initialSquare.x;

      while (y != destinationSquare.y) {
        if (board[row][y].piece) return false; // There is a piece blocking the path
        y += stepY;
      }

      return true;
    }

    if (this.isStraightMove(initialSquare, destinationSquare)) {
      let col = initialSquare.y;

      while (x != destinationSquare.x) {
        if (board[x][col].piece) return false; // There is a piece blocking the path
        x += stepX;
      }

      return true;
    }

    if (this.isDiagonalMove(initialSquare, destinationSquare)) {
      while (x !== destinationSquare.x && y !== destinationSquare.y) {
        if (board[x][y].piece) {
          return false; // There is a piece blocking the path
        }
        x += stepX;
        y += stepY;
      }

      return true;
    }

    return false;
  };

  isDiagonalMove = (initialSquare, destinationSquare) => {
    let dx = Math.abs(initialSquare.x - destinationSquare.x);
    let dy = Math.abs(initialSquare.y - destinationSquare.y);

    return dx === dy;
  };

  isHorizontalMove = (initialSquare, destinationSquare) => {
    return initialSquare.x === destinationSquare.x;
  };

  isStraightMove = (initialSquare, destinationSquare) => {
    return initialSquare.y === destinationSquare.y;
  };
}
