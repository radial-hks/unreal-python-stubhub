## GeometryScriptGroupLayer Objects

```python
class GeometryScriptGroupLayer(StructBase)
```

FGeometryScriptGroupLayer identifies a PolyGroup Layer of a Mesh.
The Default Layer always exists, Extended layers may or may not exist.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_layer`` (bool):  [Read-Write] If true,the default/standard PolyGroup Layer is used
- ``extended_layer_index`` (int32):  [Read-Write] Index of an extended PolyGroup Layer (which may or may not exist on any given Mesh)

<a id="unreal.GeometryScriptGroupLayer.__init__"></a>

#### __init__

```python
def __init__(default_layer: bool = False,
             extended_layer_index: int = 0) -> None
```

<a id="unreal.GeometryScriptGroupLayer.default_layer"></a>

#### default_layer

```python
@property
def default_layer() -> bool
```

(bool):  [Read-Write] If true,the default/standard PolyGroup Layer is used

<a id="unreal.GeometryScriptGroupLayer.default_layer"></a>

#### default_layer

```python
@default_layer.setter
def default_layer(value: bool) -> None
```

<a id="unreal.GeometryScriptGroupLayer.extended_layer_index"></a>

#### extended_layer_index

```python
@property
def extended_layer_index() -> int
```

(int32):  [Read-Write] Index of an extended PolyGroup Layer (which may or may not exist on any given Mesh)

<a id="unreal.GeometryScriptGroupLayer.extended_layer_index"></a>

#### extended_layer_index

```python
@extended_layer_index.setter
def extended_layer_index(value: int) -> None
```

<a id="unreal.GeometryScriptIndexList"></a>