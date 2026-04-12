## glTFRuntimeScene Objects

```python
class glTFRuntimeScene(StructBase)
```

Gl TFRuntime Scene

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Only]
- ``name`` (str):  [Read-Only]
- ``root_nodes_indices`` (Array[int32]):  [Read-Only]

<a id="unreal.glTFRuntimeScene.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index: int = 0,
             name: str = "",
             root_nodes_indices: Array[int] = []) -> None
```

<a id="unreal.glTFRuntimeScene.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeScene.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Only]

<a id="unreal.glTFRuntimeScene.root_nodes_indices"></a>

#### root\_nodes\_indices

```python
@property
def root_nodes_indices() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.glTFRuntimeNode"></a>