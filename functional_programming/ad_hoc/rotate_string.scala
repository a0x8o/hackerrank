import collection.mutable

object Solution {

  def main(args: Array[String]): Unit = {
    val n = readLine().trim().toInt
    val strings = new mutable.ListBuffer[String]()

    for (i <- 1 to n) {
      val string = readLine().trim()
      strings += string
    }

    val res = strings.map{string =>
      val baseList = List.fill(string.size)(string)
      val rotatedList = baseList.zipWithIndex.map{case (s, i) => rotate(s, i+1)}
      rotatedList.mkString(" ")
    }

    println(res.mkString("\n"))
  }

  def rotate(s: String, n: Int): String = {
    var temp = s
    for (i <- 1 to n)
      temp = rotate(temp)
    temp
  }

  def rotate(s: String): String = {
    s.tail ++ s.head.toString
  }
}
