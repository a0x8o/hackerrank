object Solution {

  def main(args: Array[String]): Unit = {
    val p = readLine().trim().split("")
    val q = readLine().trim().split("")
    val r = (p zip q).map{case (x, y) => x + y}.mkString("")
    println(r)
  }
}
