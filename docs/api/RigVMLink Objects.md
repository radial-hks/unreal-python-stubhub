## RigVMLink Objects

```python
class RigVMLink(Object)
```

The Link represents a connection between two Pins
within a Graph. The Link can be accessed on the
Graph itself - or through the URigVMPin::GetLinks()
method.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMLink.h

<a id="unreal.RigVMLink.get_target_pin"></a>

#### get_target_pin

```python
def get_target_pin() -> RigVMPin
```

x.get_target_pin() -> RigVMPin
Returns the target Pin of this Link (or nullptr)

Returns:
    RigVMPin:

<a id="unreal.RigVMLink.get_target_node"></a>

#### get_target_node

```python
def get_target_node() -> RigVMNode
```

x.get_target_node() -> RigVMNode
Returns the target Node of this Link (or nullptr)

Returns:
    RigVMNode:

<a id="unreal.RigVMLink.get_source_pin"></a>

#### get_source_pin

```python
def get_source_pin() -> RigVMPin
```

x.get_source_pin() -> RigVMPin
Returns the source Pin of this Link (or nullptr)

Returns:
    RigVMPin:

<a id="unreal.RigVMLink.get_source_node"></a>

#### get_source_node

```python
def get_source_node() -> RigVMNode
```

x.get_source_node() -> RigVMNode
Returns the source Node of this Link (or nullptr)

Returns:
    RigVMNode:

<a id="unreal.RigVMLink.get_pin_path_representation"></a>

#### get_pin_path_representation

```python
def get_pin_path_representation() -> str
```

x.get_pin_path_representation() -> str
Returns a string representation of the Link,
for example: "NodeA.Color.R -> NodeB.Translation.X"
note: can be split again using SplitPinPathRepresentation

Returns:
    str:

<a id="unreal.RigVMLink.get_opposite_pin"></a>

#### get_opposite_pin

```python
def get_opposite_pin(pin: RigVMPin) -> RigVMPin
```

x.get_opposite_pin(pin) -> RigVMPin
Returns the opposite Pin of this Link given one of its edges (or nullptr)

Args:
    pin (RigVMPin): 

Returns:
    RigVMPin:

<a id="unreal.RigVMLink.get_link_index"></a>

#### get_link_index

```python
def get_link_index() -> int
```

x.get_link_index() -> int32
Returns the current index of this Link within its owning Graph.

Returns:
    int32:

<a id="unreal.RigVMLink.get_graph_depth"></a>

#### get_graph_depth

```python
def get_graph_depth() -> int
```

x.get_graph_depth() -> int32
Returns the graph nesting depth of this link

Returns:
    int32:

<a id="unreal.RigVMLink.get_graph"></a>

#### get_graph

```python
def get_graph() -> RigVMGraph
```

x.get_graph() -> RigVMGraph
Returns the Link's owning Graph/

Returns:
    RigVMGraph:

<a id="unreal.RigVMInjectionInfo"></a>