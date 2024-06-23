export default class Square {
  constructor(piece, x, y, coveredByWhite, coveredByBlack) {
    this.piece = piece;
    this.x = x;
    this.y = y;
    this.coveredByWhite = coveredByWhite;
    this.coveredByBlack = coveredByBlack;
  }

  getPiece = () => {
    return this.piece;
  };

  setPiece = (piece) => {
    this.piece = piece;
  };

  getX = () => {
    return this.x;
  };

  getY = () => {
    return this.y;
  };

  isCoveredByWhite = () => {
    return this.coveredByWhite;
  };

  setCoveredByWhite = (coveredByWhite) => {
    this.coveredByWhite = coveredByWhite;
  };

  isCoveredByBlack = () => {
    return this.coveredByBlack;
  };

  setCoveredByBlack = (coveredByBlack) => {
    this.coveredByBlack = coveredByBlack;
  };

  getSquare = () => {
    return [this.x, this.y];
  };
}
