// import Square from "../Square.mjs";
import Piece from "./Piece.mjs";

export default class Knight extends Piece {
  constructor(isWhite) {
    super(isWhite);
  }

  pieceSymbol = () => {
    return this.isWhite ? "♞" : "♘";
  };

  move = (initialSquare, destinationSquare) => {
    if (destinationSquare.piece?.isWhite === this.isWhite) return false;
    let dx = Math.abs(destinationSquare.x - initialSquare.x);
    let dy = Math.abs(destinationSquare.y - initialSquare.y);
    if (dx * dy !== 2) return false;

    return true;
  };
}
