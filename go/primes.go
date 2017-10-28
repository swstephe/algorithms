package algorithms

import (
	"math/rand"
	"math"
)

type Seed struct {
	limit uint64
	seeds []uint64
}

var MillerSeeds = []Seed{
	{1373653, []uint64{2, 3}},
	{9080191, []uint64{31, 73}},
	{4759123141, []uint64{2, 7, 61}},
	{1122004669633, []uint64{2, 13, 23, 1662803}},
	{2152302898747, []uint64{2, 3, 5, 7, 11}},
	{3474749660383, []uint64{2, 3, 5, 7, 11, 13}},
	{341550071728321, []uint64{2, 3, 5, 7, 11, 13, 17}},
}

func IsPrime0(n uint64) bool {
	if n == 0 || n == 1 {
		return false
	}
	limit := uint64(math.Sqrt(float64(n)))
	for i := uint64(5); i <= limit; i++ {
		if n % i == 0 {
			return false
		}
	}
	return true
}

func IsPrime1(n uint64) bool {
	switch {
	case n == 0 || n == 1:
		return false
	case n % 2 == 0:
		return n == 2
	case n % 3 == 0:
		return n == 3
	}
	limit := uint64(math.Sqrt(float64(n)))
	for i := uint64(5); i <= limit; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func Power(a, n, d uint64) uint64 {
	value := a
	for i := uint64(0); i < n; i++ {
		value = (value*value) % d
	}
	return value
}

func Fermat(n uint64, k int) bool {
    if n <= 4 {
        return n == 2 || n == 3
	}
    for i := 0; i < k; i++ {
		a := (rand.Uint64() % (n - 4)) + 2
		if Power(a, n - 1, n) != 1 {
			return false
		}
	}
	return true
}

func MillerTest(d, n uint64) bool {
    a := (rand.Uint64() % (n - 3)) + 2
    x := Power(a, d, n)
    if x == 1 || x == n - 1 {
		return true
	}
    for d != n - 1 {
		x = (x * x) % n
		d *= 2
		if x == 1 {
			return false
		}
		if x == n - 1 {
			return true
		}
	}
    return false
}

func Witness(n, s, d uint64, a uint64) bool {
	x := Power(a, d, n)
	for i := uint64(0); i < s; i++ {
		y := (x*x) % n
		if y == 1 && x != 1 && x != n-1 {
			return false
		}
		x = y
	}
	return x == 1
}

func Miller(n uint64) bool {
	switch {
	case n == 0 || n == 1:
		return false
	case n % 2 == 0:
		return n == 2
	case n % 3 == 0:
		return n == 3
	}
	d := n >> 1
	s := uint64(1)
    for (d & 1) == 0 {
    	d >>= 1
    	s++
	}
    for _, seed := range MillerSeeds {
		if n < seed.limit {
			for _, sd := range seed.seeds {
				if !Witness(n, s, d, sd) {
					return false
				}
			}
		}
	}
	return true
}

