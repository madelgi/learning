{-# LANGUAGE NoImplicitPrelude #-}
{-# LANGUAGE ScopedTypeVariables #-}

module Course.Compose where

import Course.Core
import Course.Functor
import Course.Applicative
import Course.Monad

-- | Exactly one of these exercises will not be possible to achieve.
--   Determine which.
newtype Compose f g a = Compose (f (g a))

-- | Implement a Functor instance for Compose
instance (Functor f, Functor g) => Functor (Compose f g) where
    (<$>) = error "todo: Course.Compose (<$>)#instance (Compose f g)"

-- | Implement the pure and (<*>) function for an Applicative instance
--   for Compose
instance (Applicative f, Applicative g) => Applicative (Compose f g) where
    pure  = error "todo: Course.Compose pure#instance (Compose f g)"
    (<*>) = error "todo: Course.Compose (<*>)#instance (Compose f g)"

-- | Implement the (=<<) function for a Monad instance for Compose
instance (Monad f, Monad g) => Monad (Compose f g) where
    (=<<) = error "todo: Course.Compose (<<=)#instance (Compose f g)"
