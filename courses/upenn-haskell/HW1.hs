toDigits :: Integer -> [Integer]
toDigits n | n < 1 = []
toDigits n = (toDigits $ n `div` 10) ++ [(n `mod` 10)]

double :: [Integer] -> [Integer

doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther (x:y:zs) = x : 2*y : (doubleEveryOther zs)
doubleEveryOther x = x

validate :: Integer -> Bool
validate x = (sum . doubleEveryOther . toDigits $ x) `mod` 10 == 0
