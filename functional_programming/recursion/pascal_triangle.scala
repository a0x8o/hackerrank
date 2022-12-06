import collection.mutable

object Solution {
  
  def main(args: Array[String]) {
    val n = readLine().trim().toInt
    val matrix = mutable.Map.empty[(Int, Int), Int]

    for (i <- 1 to n) {
      matrix += ((i, 1) -> 1)
      matrix += ((i, i) -> 1)
    }

    if (n >= 3)
      for (i <- 3 to n) 
        for (j <- 2 to (i-1)) {
          val temp: Int = matrix(i-1, j-1) + matrix(i-1, j)
          matrix += ((i, j) -> temp)
        }

    val res = new mutable.StringBuilder()

    for (i <- 1 to n) {
      for (j <- 1 to i) {
        res ++= matrix(i, j).toString
        if (j != i) res ++= " "
      }
      if (i != n) res ++= "\n"
    }

    println(res)
  }
}

