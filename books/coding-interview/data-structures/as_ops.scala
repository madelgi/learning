object ASOps {

  // check if a string is all unique characters.
  //
  //  * distinct: remove duplicates from a list (a string is a list of Chars)
  def isUnique(s: String): Boolean = {
    s.distinct == s
  }

  // reverse a string
  def reverse(s: String): String = {
    s match {
      case "" => ""
      case _  => reverse(s.tail) + s.head
    }
  }

  // are two strings anagrams?
  def anagram(s1: String, s2: String): Boolean = {
    s1.sorted == s2.sorted
  }

  def sillyMap(s: String): String = {
    s.flatMap(c => if (c == ' ') "%20" else c.toString)
  }
}
