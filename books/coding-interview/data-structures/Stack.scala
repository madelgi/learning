import scala.collection.mutable.Stack

object StackProbs {
  // sortStack = (3,1,4)
  def sort(s: Stack[Int]) = {
    val sortedStack = new Stack[Int]
    var x = 0
    while (!s.isEmpty) {
      x = s.pop
      while (!sortedStack.isEmpty && sortedStack.top < x) {
        s.push( sortedStack.pop )
      }
      sortedStack.push(x)
    }
    sortedStack
  }

  // min method for stack - simply iterate through looking for smallest
  // value
  def min(s: Stack[Int]): Int = {
    val sCopy = s.clone
    var minVal = sCopy.pop
    var next = 0
    while (sCopy != Nil) {
      next = sCopy.pop
      if (next < minVal) minVal = next
    }
    minVal
  }
}

class MyQueue {
  private val s1 = new Stack[Int]
  private val s2 = new Stack[Int]

  def enqueue(n: Int) {
    if (s1.isEmpty && s2.isEmpty) s1.push(n)
    else if (!s1.isEmpty) s1.push(n)
    else s2.push(n)
  }

  def dequeue: Int = {
    if (s1.isEmpty) {
      if (s2.isEmpty) {
        0
      } else {
        var x = s2.pop
        while (!s2.isEmpty) {
          s1.push(x)
          x = s2.pop
        }
        x
      }
    } else {
      var x = s1.pop
      while (!s1.isEmpty) {
        s2.push(x)
        x = s1.pop
      }
      x
    }
  }
}
