class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        
        if n < 2:
            return 0
        
        # Generating primes up to n^(2/3)
        n_2_3 = int(n ** (2/3) + 1e-8)
        h_n_2_3 = (n_2_3 + 1) >> 1
        
        primes = [2]
        isPrime = [True] * h_n_2_3
        isPrime[0] = False
        
        for i in range(1, h_n_2_3):
            if isPrime[i]:
                primes.append(p := (i << 1) + 1)
                for j in range((p * p) >> 1, h_n_2_3, p):
                    isPrime[j] = False
        
        # Counting positive integers up to m that are not divisible
        # by any of the first b primes
        def Phi(m: int, b: int) -> int:
            if b <= 0 or m <= 1:
                return m
            if m < primes[b - 1]:
                return 1
            if m < primes[b - 1] ** 2:
                return pi_(m) - b + 1
            
            return m - sum(Phi(m // primes[i], i) for i in range(b))
        
        # Counting primes up to m
        def pi_(m: int) -> int:
            if m <= n_2_3:
                l = 0
                r = len(primes)
                while l < r:
                    mid = l + ((r - l + 1) >> 1)
                    if primes[mid - 1] > m:
                        r = mid - 1
                    else:
                        l = mid
                return l
            
            cbrt_m = int(m ** (1/3) + 1e-8)
            sqrt_m = int(math.sqrt(m) + 1e-8)
            n = pi_(cbrt_m)
            mu = pi_(sqrt_m) - n
            
            return Phi(m, n) + n * (mu + 1) + mu * (mu - 1) // 2 - 1 - \
            sum(pi_(m // primes[i]) for i in range(n, n + mu))
        
        return pi_(n)
