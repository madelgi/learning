{-# LANGUAGE FlexibleInstances #-}
{-# OPTIONS_GHC -fno-warn-missing-methods #-}

fib :: Integer -> Integer
fib n = fibHelp 0 1 n
    where fibHelp n1 n2 n = case n of
            0 -> n1
            _ -> fibHelp n2 (n1 + n2) (n - 1)

fibs1 :: [Integer]
fibs1 = map fib [0..]

fibs2 :: [Integer]
fibs2 = 1 : 1 : zipWith (+) fibs2 (tail fibs2)

data Stream a = Cons a (Stream a)

streamToList :: Stream a -> [a]
streamToList (Cons x s) = x : (streamToList s)

instance Show a => Show (Stream a) where
    show s = show $ take 20 (streamToList s)

streamRepeat :: a -> Stream a
streamRepeat x = Cons x (streamRepeat x)

streamMap :: (a -> b) -> Stream a -> Stream b
streamMap f (Cons x l) = Cons (f x) (streamMap f l)

streamFromSeed :: (a -> a) -> a -> Stream a
streamFromSeed r a = Cons a (streamFromSeed r (r a))

nats :: Stream Integer
nats = streamFromSeed (+1) 0

interleaveStream :: Stream a -> Stream a -> Stream a
interleaveStream (Cons a l1) (Cons b l2) =
        Cons a (Cons b (interleaveStream l1 l2))

ruler :: Stream Int
ruler = streamMap f (streamFromSeed (+1) 1)
    where f x = length . takeWhile (\n -> even n && n /= 0)
                       . iterate (`div` 2) $ x


type Matrix = (Int,Int,Int,Int)

instance Num Matrix where
    (a1,a2,a3,a4) * (b1,b2,b3,b4) = ( a1*b1+a2*b3
                                    , a1*b2+a2*b4
                                    , a3*b1+a4*b3
                                    , a3*b2+a4*b4
                                    )

fib4 :: Int -> Int
fib4 n | n == 0 = 1
fib4 n          = takeFst $ ((1,1,1,0) :: Matrix)^n

takeFst :: Matrix -> Int
takeFst (a,_,_,_) = a
