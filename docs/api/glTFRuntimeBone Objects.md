## glTFRuntimeBone Objects

```python
class glTFRuntimeBone(StructBase)
```

Gl TFRuntime Bone

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (str):  [Read-Write]
- ``parent_index`` (int32):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.glTFRuntimeBone.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    bone_name: str = "",
    parent_index: int = 0,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.glTFRuntimeBone.bone_name"></a>

#### bone\_name

```python
@property
def bone_name() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeBone.bone_name"></a>

#### bone\_name

```python
@bone_name.setter
def bone_name(value: str) -> None
```

<a id="unreal.glTFRuntimeBone.parent_index"></a>

#### parent\_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeBone.parent_index"></a>

#### parent\_index

```python
@parent_index.setter
def parent_index(value: int) -> None
```

<a id="unreal.glTFRuntimeBone.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.glTFRuntimeBone.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.glTFRuntimeMorphTarget"></a>