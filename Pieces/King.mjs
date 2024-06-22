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
    let dx = Math.abs(destinationSquare.x - initialSquare.x);
    let dy = Math.abs(destinationSquare.y - initialSquare.y);
    if (dx !== 1 && dy !== 1) return false;

    switch (isWhite) {
      case true: {
        if (destinationSquare.piece?.isWhite) return false;
        if (destinationSquare.isCoveredByBlack()) return false;
        break;
      }

      case false: {
        if (!destinationSquare.piece?.isWhite) return false;
        if (destinationSquare.isCoveredByWhite()) return false;
        break;
      }
    }

    return true;
  };

  castle = () => {
    this.canCastle = false;
  };

  isCastlingDone = () => {
    return this.canCastle;
  };
}
