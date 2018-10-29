push!(LOAD_PATH, joinpath(dirname(@__FILE__), "..", "src"))
using Algorithms
using Test


tests = [
    # "primes",
    "trees",
]

if length(ARGS) > 0
    tests = ARGS
end

@testset "Algorithms" begin

for t in tests
    fp = joinpath(dirname(@__FILE__), "test_$t.jl")
    println("$fp ...")
    include(fp)
end

end # @testset