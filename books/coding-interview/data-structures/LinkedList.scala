abstract class MyList[+A] {
  def head: A
  def tail: MyList[A]
}

case class MyCons[A](head: A, tail: MyList[A]) extends MyList[A]

case object MyNil extends MyList[Nothing] {
  def head = throw new NoSuchElementException("MyNil.head")
  def tail = throw new NoSuchElementException("MyNil.tail")
}

object ListFuncs {

  def getNth[A](l: MyList[A], n: Int): A = {
    n match {
      case 0  => l.head
      case _  => getNth(l.tail, n-1)
    }
  }

  def delete[A](l: MyList[A], e: A): MyList[A] = {
    if (l.head == e) {
      l.tail
    } else if (l.tail == MyNil) {
      throw new NoSuchElementException("Element " + e + " does not exist")
    } else {
      MyCons(l.head, delete(l.tail, e))
    }
  }

  def test = {
    // [1,3,10,11,7]
    val xs = MyCons(1, MyCons(3, MyCons(10, MyCons(11, MyCons(7, MyNil)))))
    getNth(xs, 3)
    delete(xs, 11)
  }
}
