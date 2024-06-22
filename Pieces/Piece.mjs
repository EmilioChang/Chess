import Square from "../Square.mjs";

export default class Piece {
  constructor(isWhite) {
    this.isWhite = isWhite;
  }

  pieceSymbol = () => {};

  move = (initialSquare, destinationSquare) => {};
}
