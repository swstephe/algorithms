const MAX_INT = 10
const COUNT = 10
const REPEAT = 40

@testset "trees" begin
    @testset "test_binary" begin
        data = Set()
        tree = Algorithms.BinaryTree()
        for c = 1 : COUNT
            for i = 1 : c
                value = rand(-MAX_INT:MAX_INT)
                Algorithms.insert(tree, value)
                push!(data, value)
                @test Algorithms.inorder(tree) == sort(collect(data))
            end
            for value in data
                Algorithms.delete(tree, value)
                pop!(data, value)
                @test Algorithms.inorder(tree) == sort(collect(data))
            end
            @test Algorithms.count(tree) == 0
            @test Algorithms.inorder(tree) == []
        end
    end

    @testset "test_binary1" begin
        tree = Algorithms.BinaryTree()
        Algorithms.insert(tree, 50)
        Algorithms.insert(tree, 30)
        Algorithms.insert(tree, 20)
        Algorithms.insert(tree, 40)
        Algorithms.insert(tree, 70)
        Algorithms.insert(tree, 60)
        Algorithms.insert(tree, 80)
        @test Algorithms.inorder(tree) == [20, 30, 40, 50, 60, 70, 80]
        Algorithms.delete(tree, 20)
        @test Algorithms.inorder(tree) == [30, 40, 50, 60, 70, 80]
        Algorithms.delete(tree, 30)
        @test Algorithms.inorder(tree) == [40, 50, 60, 70, 80]
        Algorithms.delete(tree, 50)
        @test Algorithms.inorder(tree) == [40, 60, 70, 80]
        Algorithms.delete(tree, 80)
        @test Algorithms.inorder(tree) == [40, 60, 70]
    end
end
