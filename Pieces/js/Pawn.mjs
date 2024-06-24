import Piece from "./Piece.mjs";

export default class Pawn extends Piece {
  constructor(isWhite) {
    super(isWhite);
    this.madeFirstMove = false;
  }

  move(board, initialSquare, destinationSquare) {
    if (
      destinationSquare.piece &&
      destinationSquare.piece.isWhite === this.isWhite
    ) {
      return false;
    }

    const dx = Math.abs(initialSquare.x - destinationSquare.x);

    if (dx > 2) {
      return false;
    }

    if (dx === 2) {
      if (this.validDoubleMove(board, initialSquare, destinationSquare)) {
        this.madeFirstMove = true;
        return true;
      } else {
        return false;
      }
    }

    if (this.validForwardMove(initialSquare, destinationSquare)) {
      this.madeFirstMove = true;
      return true;
    } else {
      return false;
    }
  }

  validDoubleMove(board, initialSquare, destinationSquare) {
    if (this.madeFirstMove) {
      return false;
    }

    if (initialSquare.y !== destinationSquare.y) {
      return false;
    }

    let direction = this.isWhite ? -1 : 1;

    if (board[initialSquare.x + direction][initialSquare.y].piece) {
      return false;
    }
    if (destinationSquare.piece) {
      return false;
    }

    return true;
  }

  validForwardMove(initialSquare, destinationSquare) {
    if (initialSquare.y !== destinationSquare.y) {
      return false;
    }

    if (Math.abs(initialSquare.x - destinationSquare.x) !== 1) {
      return false;
    }

    return true;
  }

  take = () => {
    // TODO
  };

  enPassant = () => {
    // TODO
  };
}
