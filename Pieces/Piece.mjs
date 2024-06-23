import Square from "../Game/Square.mjs";

export default class Piece {
  constructor(isWhite) {
    this.isWhite = isWhite;
  }

  pieceSymbol = () => {};

  move = (initialSquare, destinationSquare) => {};
}
