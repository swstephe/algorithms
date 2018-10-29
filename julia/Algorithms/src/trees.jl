mutable struct BinaryNode
    value
    left::Union{BinaryNode, Nothing}
    right::Union{BinaryNode, Nothing}

    BinaryNode(value) = new(value, nothing, nothing)
end

mutable struct BinaryTree
    root::Union{BinaryNode, Nothing}

    BinaryTree() = new(nothing)

    function BinaryTree(values...)
        root = nothing
        for value in values
            root = insert(root, value)
        end
        new(root)
    end
end

function count(node::Nothing)::Integer
    return 0
end

function count(node::BinaryNode)::Integer
    return count(node.left) + count(node.right) + 1
end

function count(tree::BinaryTree)::Integer
    return count(tree.root)
end

function height(node::Nothing)::Integer
    return 0
end

function height(node::BinaryNode)::Integer
    return max(height(node.left), height(node.right)) + 1
end

function height(tree::BinaryTree)::Integer
    return height(tree.root)
end

function find_min(node::BinaryNode)::BinaryNode
    return node.left == nothing ? node : find_min(node.left)
end

function find_max(node::BinaryNode)::BinaryNode
    return node.right == nothing ? node : find_max(node.right)
end

function find(node::Nothing, value)::Nothing
    return nothing
end

function find(node::BinaryNode, value)::BinaryNode
    if value == node.value
        return node
    end
    return find(value < node.value ? node.left : node.right, value)
end

function find(tree::BinaryTree, value)::BinaryNode
    return find(tree.root)
end

function delete(node::Nothing, value)
end

function delete(node::BinaryNode, value)
    if value < node.value
        node.left = delete(node.left, value)
    elseif value > node.value
        node.right = delete(node.right, value)
    else
        if node.left == nothing && node.right == nothing
            return nothing
        elseif node.left == nothing
            return node.right
        elseif node.right == nothing
            return node.left
        else
            child = find_min(node.right)
            node.value = child.value
            node.right = delete(node.right, child.value)
        end
    end
    return node
end

function delete(tree::BinaryTree, value)
    tree.root = delete(tree.root, value)
end

function insert(node::Nothing, value)::BinaryNode
    return BinaryNode(value)
end

function insert(node::BinaryNode, value)::BinaryNode
    if value < node.value
        node.left = insert(node.left, value)
    elseif value > node.value
        node.right = insert(node.right, value)
    end
    return node
end

function insert(tree::BinaryTree, value)
    tree.root = insert(tree.root, value)
end

function inorder(node::Nothing)::Array
    return []
end

function inorder(node::BinaryNode)::Array
    a = inorder(node.left)
    push!(a, node.value)
    append!(a, inorder(node.right))
    return a
end

function inorder(tree::BinaryTree)::Array
    return inorder(tree.root)
end

function leaves(node::Nothing)::Array
    return []
end

function leaves(node::BinaryNode)::Array
    if node.left == nothing && node.right == nothing
        return [node.value]
    end
    a = leaves(node.left)
    append!(a, leaves(node.right))
    return a
end

function leaves(tree::BinaryTree)::Array
    return leaves(tree.root)
end

function paths(node::Nothing)::Array
    return []
end

function paths(node::BinaryNode)::Array
    if node.left == nothing && node.right == nothing
        return [[node.value]]
    end
    a = []
    for path in paths(node.left)
        prepend!(path, node.value)
        append(a, path)
    end
    for path in paths(node.right)
        prepends!(path, node.value)
        append!(a, path)
    end
end

function paths(tree::BinaryTree)::Array
    return paths(tree.root)
end
