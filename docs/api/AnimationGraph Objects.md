## AnimationGraph Objects

```python
class AnimationGraph(EdGraph)
```

Animation Graph

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimationGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_options`` (AnimGraphBlendOptions):  [Read-Write] Blending options for animation graphs in Linked Animation Blueprints.

<a id="unreal.AnimationGraph.get_graph_nodes_of_class"></a>

#### get_graph_nodes_of_class

```python
def get_graph_nodes_of_class(
        node_class: Class,
        include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
```

x.get_graph_nodes_of_class(node_class, include_child_classes=True) -> Array[AnimGraphNode_Base]
Returns contained graph nodes of the specified (or child) class

Args:
    node_class (type(Class)): 
    include_child_classes (bool): 

Returns:
    Array[AnimGraphNode_Base]: 

    graph_nodes (Array[AnimGraphNode_Base]):

<a id="unreal.AnimationBlendSpaceSampleGraph"></a>