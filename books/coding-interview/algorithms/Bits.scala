object Bits {
  // 5.3) Given an integer, print the next smallest and next largest number that
  // have the same number of 1 bits in their binary representation.

  // 5.5) Write a function that computes the number of bits required to convert
  // integer A to integer B.
  def BitNumber(a: Int, b: Int): Int = {
    var aBinary = a.toBinaryString
    var bBinary = b.toBinaryString
    var newval = ""
    val l = aBinary.length - bBinary.length
    if (l > 0) {
      bBinary = "0" * l + bBinary
    }
    if (l < 0) {
      val newval = ("0" * l) + aBinary
    }
    println(l)
    println(aBinary)
    println(newval)
    println(bBinary)
    stringDiff(aBinary, bBinary)
  }

  private def stringDiff(a: String, b: String): Int = {
    (a zip b).filter(n => n._1 == n._2).length
  }

  // 5.6) Write a function to swap odd and even numbered bits
  def Swap(n: Int): Int = {
    val nBin = n.toBinaryString
    var binHead = ""
    var binTail = nBin
    if (nBin.length % 2 == 1) {
      binHead = nBin.head.toString
      binTail = nBin.tail
    }
    val fin = binHead + binTail.reverse.grouped(2).toList.map(n => (n(0), n(1)))
                          .reverse.map(n => n._1.toString + n._2.toString).mkString
    Integer.parseInt(fin, 2)
  }
}
