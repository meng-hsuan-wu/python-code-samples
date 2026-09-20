from functools import lru_cache 

@lru_cache(maxsize=None)
def traverse(freq: list, prev: int, n: int) -> int:
    if n <= 0:
        return 52
    
    freq_list = list(freq)
    ttl = 0
    
    for i in range(13):
        if freq_list[i] == 0:
            continue
 
        if i == prev:
            ttl += freq_list[i] * ((52 - n) + 1)
        else:
            freq_list[i] -= 1
            tmp = freq_list[i]
            new_freq = tuple(sorted(freq_list, reverse = True))
            ind = 0
            while new_freq[ind] != tmp:
                ind += 1
            ttl += (freq_list[i] + 1) * traverse(new_freq, ind, n - 1)
            freq_list[i] += 1
 
    ttl /= n
    return ttl
 
res = traverse((4, ) * 13, -1, 52)
print(f"{res:.8f}")
