{-# OPTIONS_GHC -Wall #-}
module LogAnalysis where

import Log
import Data.List.Split (splitOn)
import Data.List       (intercalate)

main :: IO ()
main = do
    f <- readFile "error.log"
    print . whatWentWrong $ parse f

-- | Exercise 1
parse :: String -> [LogMessage]
parse x = map parseMessage (lines x)

parseMessage :: String -> LogMessage
parseMessage x =
    case (head x) of
        'I' -> parseStandard (tail $ tail x) Info
        'W' -> parseStandard (tail $ tail x) Warning
        'E' -> parseError (tail $ tail x)
        _   -> Unknown x

parseError :: String -> LogMessage
parseError s = LogMessage err time msg
    where msg  = intercalate " " (tail $ tail split)
          time = (read $ split !! 1) :: Int
          err = Error ( (read $ split !! 0) :: Int)
          split = splitOn " " s


parseStandard :: String -> MessageType -> LogMessage
parseStandard s mt = LogMessage mt time msg
    where msg = intercalate " " (tail split)
          time = (read $ split !! 0) :: Int
          split = splitOn " " s

-- | Exercise 2
insert :: LogMessage -> MessageTree -> MessageTree
insert msg tree =
    case tree of
        Leaf       -> Node Leaf msg Leaf
        Node l h r -> balancedInsert l h r msg

balancedInsert :: MessageTree -> LogMessage -> MessageTree -> LogMessage -> MessageTree
balancedInsert l h r msg =
        if (getTimeStamp msg > getTimeStamp h)
            then Node l h (insert msg r)
            else Node (insert msg l) h r

-- Utility functions
getType :: LogMessage -> MessageType
getType (LogMessage t _ _) = t

getTimeStamp :: LogMessage -> Int
getTimeStamp (LogMessage _ ts _) = ts

getMsg :: LogMessage -> String
getMsg (LogMessage _ _ msg) = msg

getSeverity :: MessageType -> Int
getSeverity (Error n) = n
getSeverity _         = -1

-- Exercise 3
build :: [LogMessage] -> MessageTree
build [] = Leaf
build (x:xs) = insert x (build xs)

-- Exercise 4
inOrder :: MessageTree -> [LogMessage]
inOrder Leaf = []
inOrder (Node l msg r) = (inOrder l) ++ [msg] ++ (inOrder r)

-- Exercise 5
whatWentWrong :: [LogMessage] -> [String]
whatWentWrong xs = map getMsg . inOrder . build $ filter condition xs
    where condition x = not (getType x == Info || getType x == Warning) &&
                         (getSeverity (getType x) > 49)
