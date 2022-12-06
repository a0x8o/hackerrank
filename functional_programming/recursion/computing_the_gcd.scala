object Solution {

  def gcd(x: Int, y: Int): Int = {
    if (x < y)
      gcd(y, x)
    else {
      val r = x % y
      if (r == 0) y
      else gcd(y, r)
    }
  }
  

  /** This part handles the input/output. Do not change or modify it. */
  def acceptInputAndComputeGCD(pair: List[Int]) = {
      println(gcd(pair.head, pair.reverse.head))
  } 


  /** The part relates to the input/output. Do not change or modify it **/
  def main(args: Array[String]) {
    acceptInputAndComputeGCD(readLine().trim().split(" ").map(x => x.toInt).toList)
  }
}
