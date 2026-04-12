## glTFRuntimeNode Objects

```python
class glTFRuntimeNode(StructBase)
```

Gl TFRuntime Node

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_index`` (int32):  [Read-Only]
- ``children_indices`` (Array[int32]):  [Read-Only]
- ``index`` (int32):  [Read-Only]
- ``mesh_index`` (int32):  [Read-Only]
- ``name`` (str):  [Read-Only]
- ``parent_index`` (int32):  [Read-Only]
- ``skin_index`` (int32):  [Read-Only]
- ``transform`` (Transform):  [Read-Only]

<a id="unreal.glTFRuntimeNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index: int = 0,
             name: str = "",
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             mesh_index: int = 0,
             skin_index: int = 0,
             camera_index: int = 0,
             children_indices: Array[int] = [],
             parent_index: int = 0) -> None
```

<a id="unreal.glTFRuntimeNode.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeNode.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Only]

<a id="unreal.glTFRuntimeNode.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.glTFRuntimeNode.mesh_index"></a>

#### mesh\_index

```python
@property
def mesh_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeNode.skin_index"></a>

#### skin\_index

```python
@property
def skin_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeNode.camera_index"></a>

#### camera\_index

```python
@property
def camera_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeNode.children_indices"></a>

#### children\_indices

```python
@property
def children_indices() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.glTFRuntimeNode.parent_index"></a>

#### parent\_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeSocket"></a>