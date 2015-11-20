{-# LANGUAGE TypeSynonymInstances #-}

import Parser
import StackVM
import Control.Monad (liftM)

data ExprT = Lit Integer
           | Add ExprT ExprT
           | Mul ExprT ExprT
             deriving (Show, Eq)

--------------------------------------------------------------------------------
-- | Exercise 1: Write an evaluator for ExprT,
--
--   eval :: ExprT -> Integer
eval :: ExprT -> Integer
eval e = case e of
    Lit n     -> n
    Mul e1 e2 -> (eval e1) * (eval e2)
    Add e1 e2 -> (eval e1) + (eval e2)


--------------------------------------------------------------------------------
-- | Exercise 2: Implement the function evalStr,
--
--   evalStr :: String -> Maybe Integer
evalStr :: String -> Maybe Integer
evalStr = liftM eval . parseExp Lit Add Mul


--------------------------------------------------------------------------------
-- | Exercise 3: Abstract the ExprT type into a type class
class Expr a where
    lit :: Integer -> a
    add :: a -> a -> a
    mul :: a -> a -> a

instance Expr ExprT where
    lit x = Lit x
    mul x y = Mul x y
    add x y = Add x y


--------------------------------------------------------------------------------
-- | Exercise 4: Create instances of Expr for Integers, Bool, MinMax, and
--   Mod7
newtype MinMax = MinMax Integer deriving (Eq, Show)
newtype Mod7 = Mod7 Integer deriving (Eq, Show)

instance Expr Integer where
    lit x = x
    mul x y = x * y
    add x y = x + y

instance Expr Bool where
    lit x = if x > 0 then True else False
    mul x y = x || y
    add x y = x && y

instance Expr MinMax where
    lit x = MinMax x
    add (MinMax x) (MinMax y) = MinMax (max x y)
    mul (MinMax x) (MinMax y) = MinMax (min x y)

instance Expr Mod7 where
    lit x = Mod7 (x `mod` 7)
    add (Mod7 x) (Mod7 y) = Mod7 $ (x + y) `mod` 7
    mul (Mod7 x) (Mod7 y) = Mod7 $ (x * y) `mod` 7

testExp :: Expr a => Maybe a
testExp = parseExp lit add mul "(3 * -4) + 5"

testInteger = testExp :: Maybe Integer
testBool = testExp :: Maybe Bool
testMM = testExp :: Maybe MinMax
testSat = testExp :: Maybe Mod7

--------------------------------------------------------------------------------
-- | Exercise 5: Create instances of Expr for Integers, Bool, MinMax, and
--   Mod7
instance Expr Program where
    lit x = [PushI x]
    add x y = x ++ y ++ [SAdd]
    mul x y = x ++ y ++ [SMul]
