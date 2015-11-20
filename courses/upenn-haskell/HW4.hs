--------------------------------------------------------------------------------
-- | Exercise 1: Wholemeal programming

-- original fun1
fun1 :: [Integer] -> Integer
fun1 [] = 1
fun1 (x:xs)
    | even x    = (x-2) * fun1 xs
    | otherwise = fun1 xs

-- haskell-fied fun1'
fun1' :: [Integer] -> Integer
fun1' = foldr (*) 1 . map (+(-2)) . filter even

-- original fun2
fun2 :: Integer -> Integer
fun2 1 = 0
fun2 n
    | even n    = n + fun2 (n `div` 2)
    | otherwise = fun2 (3*n + 1)

-- haskell-fied fun2'
fun2' :: Integer -> Integer
fun2' = sum . filter even
          . takeWhile (>1)
          . iterate (\n -> if (even n) then n `div` 2 else (3*n + 1))


-------------------------------------------------------------------------------
-- | Exercise 2: Folding with trees
data Tree a = Leaf
            | Node Integer (Tree a) a (Tree a)
              deriving (Show, Eq)

foldTree :: [a] -> Tree a
foldTree [] = Leaf
foldTree (x:xs) = error "todo"

--------------------------------------------------------------------------------
-- | Exercise 3: More folds!

-- | Part 1: Implement a function `xor` that returns true iff there are
--   an odd number of True values in an input list
xor :: [Bool] -> Bool
xor = even . length . filter (==True)

-- | Part 2: Implement map as a fold.
map' :: (a -> b) -> [a] -> [b]
map' f xs = foldr ((:) . f) [] xs

-- foldr :: (a -> b -> b) -> b -> [a] -> b
-- | Part 3: Implement foldl using foldr.
--myFoldl :: (a -> b -> a) -> a -> [b] -> a
--myFoldl f i l =

--------------------------------------------------------------------------------
-- | Exercise 4
sieveSundaram :: Integer -> [Integer]
sieveSundaram n = marks
    where marks = filter (\x -> x < n `div` 2) array
          array = map (\(x,y) -> x + y + 2*x*y) initArray
          initArray = cartProd [2..n] [2..n]

cartProd :: [a] -> [b] -> [(a,b)]
cartProd xs ys = [(x,y) | x <- xs, y <- ys]
