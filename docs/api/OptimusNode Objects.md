## OptimusNode Objects

```python
class OptimusNode(Object)
```

Optimus Node

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusNode.h

<a id="unreal.OptimusNode.set_graph_position"></a>

#### set_graph_position

```python
def set_graph_position(position: Vector2D) -> bool
```

x.set_graph_position(position) -> bool
Sets the position in the graph UI that the node should be shown at.

Args:
    position (Vector2D): The coordinates of the node's position.

Returns:
    bool: true if setting the position was successful.

<a id="unreal.OptimusNode.get_node_name"></a>

#### get_node_name

```python
def get_node_name() -> Name
```

x.get_node_name() -> Name
Returns the node class name. This name is immutable for the given node class.

Returns:
    Name: The node class name.

<a id="unreal.OptimusNode.get_node_category"></a>

#### get_node_category

```python
def get_node_category() -> Name
```

x.get_node_category() -> Name
Returns the node class category. This is used for categorizing the node for display.

Returns:
    Name: The node class category.

<a id="unreal.OptimusNode.get_graph_position"></a>

#### get_graph_position

```python
def get_graph_position() -> Vector2D
```

x.get_graph_position() -> Vector2D
Returns the position in the graph UI where the node is shown.

Returns:
    Vector2D: The coordinates of the node's position.

<a id="unreal.OptimusNode.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

x.get_display_name() -> Text
Returns the display name to use on the graphical node in the graph editor.

Returns:
    Text: The display name to show to the user.

<a id="unreal.OptimusNode_DataInterface"></a>