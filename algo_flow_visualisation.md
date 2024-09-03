###### Build a Binary tree

```mermaid
graph TD
    A --> B
    A --> C
    B --> D
    B --> E
    C --> F
    C --> G
```

Llama Index : Is a Tree Index

    - Binary Tree Based algorithm

    - Search the data, we need to know how the data is searched?

Tree Traversals:

1) Depth First Traversal
   
     - Uses Stack for storing the nodes when traversing
   
   1) In order : 
   
   2) Pre order
   
   3) Post order
- Breadth First Traversal

        - Uses queue for storing the nodes when traversing

```mermaid
graph TD
    A --> B
    A --> C
```

Based on above graph the DF traversals are as below:

> Pre order: A -> B -> C
> 
> Post order: B ->C -> A
> 
> In order: B -> A -> C

Breadth First:

> L1 = A
> 
> L2 = B , C

###### Why are we Stack for DFS?

- Stack is LiFo : Node that entered last will pop First
  
  - How the list appends the elements? It appends from the right and it pops from right

```mermaid
graph LR
    A --> B --> C --> D
```

###### Can we append and pop from left of the Python List?

1. insert(0, idx)

2. pop(idx)

3. 

```mermaid
graph RL
    A --> B
    B --> C
```

###### Why are we Queue for BFS ?

- Queue is FiFo: Node that entered very first, will be poped first

```plantuml
@startuml
    class Node1{
        data
        next
     }
     class Node2{
        data
        next
     }
     class Node3{
        data
        next
     }
     Node1::next --> Node2::data
     Node2::next --> Node3::data
@enduml
```

```plantuml
@startuml
    class Node1{
        data
        next
     }
     class Node2{
        data
        next
     }
     class Node3{
        data
        next
     }
     Node3::next --> Node2::data
     Node2::next --> Node1::data
@enduml
```












