function isprime0(n::Integer)::Bool
    if n <= 4
        return n in (2, 3)
    end
    for i = 2 : trunc(√n)
        if n % i == 0
            return false
        end
    end
    return true
end

function isprime1(n::Integer)::Bool
    if n <= 4
        return n in (2, 3)
    end
    if n % 2 == 0 || n % 3 == 0
        return false
    end
    for i = 5 : 6 : trunc(√n)
        if n % i == 0 || n % (i + 2) == 0
            return false
        end
    end
    return true
end

function fermat(n::Integer, k::Integer=15)::Bool
    if n <= 4
        return n in (2, 3)
    end
    for i in 1 : k
        a = rand(2 : n - 2)
        if powermod(a, n - 1, n) != 1
            return false
        end
    end
    return true
end

function miller_test(d::Integer, n::Integer)::Bool
    a = rand(2 : n - 1)
    x = powermod(a, d, n)
    if x in (1, n - 1)
        return true
    end
    while d != n - 1
        x = (x * x) % n
        d *= 2
        if x == 1
            return false
        end
        if x == n - 1
            return true
        end
    end
    return false
end


function miller(n::Integer, k::Integer=4)::Bool
    if n <= 4
        return n in (2, 3)
    end
    d = n - 1
    while d % 2 == 0
        d >>= 1
    end

    for i = 1 : k
        if !miller_test(d, n)
            return false
        end
    end
    return true
end
