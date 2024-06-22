import Square from "../Square.mjs";
import Piece from "./Piece.mjs";

export default class Pawn extends Piece {
  constructor(isWhite) {
    super(isWhite);
    this.madeFirstMove = false;
  }

  pieceSymbol = () => {
    return this.isWhite ? "♟" : "♙";
  };

  move = (initialSquare, destinationSquare) => {
    //TODO
    // 1) hacer que los peones no se puedan mover hacia adelante si hay una pieza en el
    // camino y
    // 2) hacer que puedan comer piezas diagonalmente
    let dx = Math.abs(initialSquare.x - destinationSquare.x);

    if (dx > 2) return false;
    if (dx == 2 && this.madeFirstMove) return false;

    this.madeFirstMove = true;

    switch (this.isWhite) {
      // check if player wants to go backwards
      case true: {
        if (destinationSquare.x < initialSquare.x) return true;
        break;
      }
      case false: {
        if (destinationSquare.x > initialSquare.x) return true;
        break;
      }
    }

    return false;
  };
}
