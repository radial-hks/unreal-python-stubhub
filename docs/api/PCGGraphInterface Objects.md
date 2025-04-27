## PCGGraphInterface Objects

```python
class PCGGraphInterface(Object)
```

PCGGraph Interface

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] Override of the color for the subgraph node for this graph.
- ``expose_to_library`` (bool):  [Read-Write]
- ``override_color`` (bool):  [Read-Write]
- ``override_title`` (bool):  [Read-Write]
- ``title`` (Text):  [Read-Write] Override of the title for the subgraph node for this graph.

<a id="unreal.PCGGraphInterface.expose_to_library"></a>

#### expose_to_library

```python
@property
def expose_to_library() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGraphInterface.expose_to_library"></a>

#### expose_to_library

```python
@expose_to_library.setter
def expose_to_library(value: bool) -> None
```

<a id="unreal.PCGGraphInterface.override_title"></a>

#### override_title

```python
@property
def override_title() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGraphInterface.override_title"></a>

#### override_title

```python
@override_title.setter
def override_title(value: bool) -> None
```

<a id="unreal.PCGGraphInterface.title"></a>

#### title

```python
@property
def title() -> Text
```

(Text):  [Read-Write] Override of the title for the subgraph node for this graph.

<a id="unreal.PCGGraphInterface.title"></a>

#### title

```python
@title.setter
def title(value: Text) -> None
```

<a id="unreal.PCGGraphInterface.override_color"></a>

#### override_color

```python
@property
def override_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGraphInterface.override_color"></a>

#### override_color

```python
@override_color.setter
def override_color(value: bool) -> None
```

<a id="unreal.PCGGraphInterface.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] Override of the color for the subgraph node for this graph.

<a id="unreal.PCGGraphInterface.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.PCGGraphInterface.get_mutable_pcg_graph"></a>

#### get_mutable_pcg_graph

```python
def get_mutable_pcg_graph() -> PCGGraph
```

x.get_mutable_pcg_graph() -> PCGGraph
Return the underlying PCG Graph for this interface.

Returns:
    PCGGraph:

<a id="unreal.PCGGraphInterface.get_const_pcg_graph"></a>

#### get_const_pcg_graph

```python
def get_const_pcg_graph() -> PCGGraph
```

x.get_const_pcg_graph() -> PCGGraph
Return the underlying PCG Graph for this interface.

Returns:
    PCGGraph:

<a id="unreal.PCGGraph"></a>