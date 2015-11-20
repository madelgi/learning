import Data.Map.Strict      (Map, insertWith, empty, fromList, union)

-- | Exercise 1: Write a function "skips", that skips over a list to
--   produce a list of lists, e.g:
--
--   > skips "ABCD"
--   ["ABCD", "BD", "C", "D"]
skips :: [a] -> [[a]]
skips xs = reverse $ skipsHelp (length xs) xs

skipsHelp :: Int -> [a] -> [[a]]
skipsHelp 0 xs = []
skipsHelp n xs = skipped : skipsHelp (n-1) xs
    where skipped = map snd . filter (\x -> (fst x) `mod` n == 0) $ enummed
          enummed = zip [1..] xs

-- | Exercise 2: Write a function `localMaxima` that finds the local maxima
--   in a list of integers,
--
--   > localMaxima [1,4,2,3,4,5,6,7,0]
--   [4,7]
--
--   TODO this is terrible, make less bad
localMaxima :: [Integer] -> [Integer]
localMaxima xs =  concatMap max3 (lists xs)
    where max3 [x,y,z] = if (x < y && y > z) then [y] else []
          lists [x,y,z] = [[x,y,z]]
          lists xs = take 3 xs : (lists $ tail xs)

histogram :: [(Int, Int)] -> String
histogram [] = ""
histogram (x:xs) =
        show (fst x) ++ " | " ++ (replicate (snd x) '*') ++ "\n" ++ histogram xs


buildHash :: [Int] -> Map Int Int
buildHash xs = union (go xs empty) nullMap
    where go [] m = m
          go (x:xs) m = go xs (insertWith (+) x 1 m)
          nullMap = fromList $ zip [1..(maximum xs)] (repeat 0)
