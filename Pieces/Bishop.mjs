// import Square from "../Square.mjs";
import Piece from "./Piece.mjs";

export default class Bishop extends Piece {
  constructor(isWhite) {
    super(isWhite);
  }

  pieceSymbol = () => {
    return this.isWhite ? "♝" : "♗";
  };

  move = (board, initialSquare, destinationSquare) => {
    if (destinationSquare.piece?.isWhite === this.isWhite) return false;
    if (!this.isDiagonalMove(initialSquare, destinationSquare)) return false;

    return this.isValidPath(board, initialSquare, destinationSquare);
  };

  isValidPath = (initialSquare, destinationSquare) => {
    let stepX = destinationSquare.x > initialSquare.x ? 1 : -1;
    let stepY = destinationSquare.y > initialSquare.y ? 1 : -1;

    let x = initialSquare.x + stepX;
    let y = initialSquare.y + stepY;

    while (x !== destinationSquare.x && y !== destinationSquare.y) {
      if (board[x][y].piece) {
        return false; // There is a piece blocking the path
      }
      x += stepX;
      y += stepY;
    }

    return true;
  };

  isDiagonalMove = (initialSquare, destinationSquare) => {
    let dx = Math.abs(initialSquare.x - destinationSquare.x);
    let dy = Math.abs(initialSquare.y - destinationSquare.y);

    return dx === dy;
  };
}
