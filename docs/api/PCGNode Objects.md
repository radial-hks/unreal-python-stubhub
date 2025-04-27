## PCGNode Objects

```python
class PCGNode(Object)
```

PCGNode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_pins`` (Array[PCGPin]):  [Read-Only]
- ``node_title`` (Name):  [Read-Write]
- ``node_title_color`` (LinearColor):  [Read-Write]
- ``output_pins`` (Array[PCGPin]):  [Read-Only]
- ``settings_interface`` (PCGSettingsInterface):  [Read-Only] Note: do not set this property directly from code, use SetSettingsInterface instead

<a id="unreal.PCGNode.node_title"></a>

#### node_title

```python
@property
def node_title() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGNode.node_title"></a>

#### node_title

```python
@node_title.setter
def node_title(value: Name) -> None
```

<a id="unreal.PCGNode.node_title_color"></a>

#### node_title_color

```python
@property
def node_title_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.PCGNode.node_title_color"></a>

#### node_title_color

```python
@node_title_color.setter
def node_title_color(value: LinearColor) -> None
```

<a id="unreal.PCGNode.settings_interface"></a>

#### settings_interface

```python
@property
def settings_interface() -> PCGSettingsInterface
```

(PCGSettingsInterface):  [Read-Only] Note: do not set this property directly from code, use SetSettingsInterface instead

<a id="unreal.PCGNode.input_pins"></a>

#### input_pins

```python
@property
def input_pins() -> Array[PCGPin]
```

(Array[PCGPin]):  [Read-Only]

<a id="unreal.PCGNode.output_pins"></a>

#### output_pins

```python
@property
def output_pins() -> Array[PCGPin]
```

(Array[PCGPin]):  [Read-Only]

<a id="unreal.PCGNode.set_node_position"></a>

#### set_node_position

```python
def set_node_position(position_x: int, position_y: int) -> None
```

x.set_node_position(position_x, position_y) -> None
Set Node Position

Args:
    position_x (int32): 
    position_y (int32):

<a id="unreal.PCGNode.remove_edge_to"></a>

#### remove_edge_to

```python
def remove_edge_to(from_pin_lable: Name, to: PCGNode,
                   to_pin_label: Name) -> bool
```

x.remove_edge_to(from_pin_lable, to, to_pin_label) -> bool
Removes an edge originating from this node

Args:
    from_pin_lable (Name): 
    to (PCGNode): 
    to_pin_label (Name): 

Returns:
    bool:

<a id="unreal.PCGNode.get_settings"></a>

#### get_settings

```python
def get_settings() -> PCGSettings
```

x.get_settings() -> PCGSettings
Returns the settings this node holds (either directly or through an instance)

Returns:
    PCGSettings:

<a id="unreal.PCGNode.get_node_position"></a>

#### get_node_position

```python
def get_node_position() -> Tuple[int, int]
```

x.get_node_position() -> (out_position_x=int32, out_position_y=int32)
Get Node Position

Returns:
    tuple: 

    out_position_x (int32): 

    out_position_y (int32):

<a id="unreal.PCGNode.get_graph"></a>

#### get_graph

```python
def get_graph() -> PCGGraph
```

x.get_graph() -> PCGGraph
Returns the owning graph

Returns:
    PCGGraph:

<a id="unreal.PCGNode.add_edge_to"></a>

#### add_edge_to

```python
def add_edge_to(from_pin_label: Name, to: PCGNode,
                to_pin_label: Name) -> PCGNode
```

x.add_edge_to(from_pin_label, to, to_pin_label) -> PCGNode
Adds an edge in the owning graph to the given "To" node.

Args:
    from_pin_label (Name): 
    to (PCGNode): 
    to_pin_label (Name): 

Returns:
    PCGNode:

<a id="unreal.PCGBaseSubgraphNode"></a>