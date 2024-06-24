// import Square from "../Square.mjs";
import Piece from "./Piece.mjs";

export default class King extends Piece {
  constructor(isWhite) {
    super(isWhite);
    this.canCastle = true;
  }

  pieceSymbol = () => {
    return this.isWhite ? "♚" : "♔";
  };

  move = (initialSquare, destinationSquare) => {
    // TODO: Implement castling
    if (destinationSquare.piece?.isWhite === this.isWhite) return false;

    let dx = Math.abs(destinationSquare.x - initialSquare.x);
    let dy = Math.abs(destinationSquare.y - initialSquare.y);
    if (dx > 1 && dy > 1) return false;

    if (this.isWhite) {
      if (destinationSquare.isCoveredByBlack()) return false;
    } else {
      if (destinationSquare.isCoveredByWhite()) return false;
    }

    return true;
  };

  castle = () => {
    this.canCastle = false;
  };
}
