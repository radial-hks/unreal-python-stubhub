## VertexLayout Objects

```python
class VertexLayout(StructBase)
```

Vertex Layout

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: DNACommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``normal`` (int32):  [Read-Write]
- ``position`` (int32):  [Read-Write]
- ``texture_coordinate`` (int32):  [Read-Write]

<a id="unreal.VertexLayout.__init__"></a>

#### __init__

```python
def __init__(position: int = 0,
             texture_coordinate: int = 0,
             normal: int = 0) -> None
```

<a id="unreal.VertexLayout.position"></a>

#### position

```python
@property
def position() -> int
```

(int32):  [Read-Only]

<a id="unreal.VertexLayout.texture_coordinate"></a>

#### texture_coordinate

```python
@property
def texture_coordinate() -> int
```

(int32):  [Read-Only]

<a id="unreal.VertexLayout.normal"></a>

#### normal

```python
@property
def normal() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigLogicConfiguration"></a>