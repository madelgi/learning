import Employee
import Control.Monad
import Data.Monoid
import Data.Tree (Tree)
import qualified Data.Tree as T
--------------------------------------------------------------------------------
-- | Exercise 1
glCons :: Employee -> GuestList -> GuestList
glCons e@(Emp nm fn) (GL names score) = GL (e : names) (fn + score)

instance Monoid GuestList where
    mempty = GL [] 0
    mappend (GL l1 s1) (GL l2 s2) = GL (l1 ++ l2) (s1+s2)

moreFun :: GuestList -> GuestList -> GuestList
moreFun g1@(GL _ s1) g2@(GL _ s2) = if s1 > s2 then g1 else g2


--------------------------------------------------------------------------------
-- | Exercise 2
treeFold :: (a -> [b] -> b) -> b -> Tree a -> b
treeFold f i t = if (subForest t == [])
                     then i
                     else f (rootNode t) (map . treeFold f i $ subForest t)
