const DATA = Any["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

@testset "slinked" begin
    @testset "test_init" begin
        list = Algorithms.SList(DATA...)
        @test collect(list) == DATA
        @test list.head.value == DATA[1]
        @test length(list) == length(DATA)
    end
    @testset "test_push!" begin
        list = Algorithms.SList()
        for day in DATA
            Algorithms.push!(list, day)
        end
        @test collect(list) == DATA
        @test list.head.value == DATA[1]
        @test length(list) == length(DATA)
    end
    @testset "test_reverse" begin
        list = Algorithms.SList(DATA...)
        Algorithms.reverse(list)
        @test length(list) == length(DATA)
    end
end
