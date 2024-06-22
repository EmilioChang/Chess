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
    let dx = Math.abs(destinationSquare.x - initialSquare.x);
    let dy = Math.abs(destinationSquare.y - initialSquare.y);
    if (dx * dy !== 2) return false;

    switch (this.isWhite) {
      case true: {
        if (destinationSquare.piece?.isWhite) return false;

        break;
      }

      case false: {
        if (!destinationSquare.piece?.isWhite) return false;

        break;
      }
    }

    return true;
  };
}
