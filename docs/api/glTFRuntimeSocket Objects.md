## glTFRuntimeSocket Objects

```python
class glTFRuntimeSocket(StructBase)
```

Gl TFRuntime Socket

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (str):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.glTFRuntimeSocket.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    bone_name: str = "",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.glTFRuntimeSocket.bone_name"></a>

#### bone\_name

```python
@property
def bone_name() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeSocket.bone_name"></a>

#### bone\_name

```python
@bone_name.setter
def bone_name(value: str) -> None
```

<a id="unreal.glTFRuntimeSocket.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.glTFRuntimeSocket.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.glTFRuntimeBone"></a>