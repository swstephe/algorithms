mutable struct SListNode
    value
    next::Union{SListNode, Nothing}

    SListNode(value, next=nothing) = new(value, next)
end

mutable struct SList
    head::Union{SListNode, Nothing}
    count::Integer

    SList() = new(nothing, 0)
    function SList(values...)
        head = nothing
        node = nothing
        count = 0
        for value in values
            if head == nothing
                head = SListNode(value)
                node = head
            else
                node.next = SListNode(value)
                node = node.next
            end
            count += 1
        end
        new(head, count)
    end
end

Base.isempty(list::SList) = list.head == nothing
Base.iterate(list::SList, node::Union{SListNode, Nothing}=list.head) =
    node == nothing ? nothing : (node.value, node.next)
Base.length(list::SList)::Integer = list.count

function Base.push!(list::SList, value)
    if isempty(list)
        list.head = SListNode(value)
        list.count = 1
    else
        last = list.head
        while last.next != nothing
            last = last.next
        end
        last.next = SListNode(value)
        list.count += 1
    end
end

function reverse(list::SList)
    prev, node = nothing, list.head
    while node != nothing
        prev, node.next, node = node, prev, node.next
    end
    list.head = prev
end

