## AesTilesVisibilityGroupRemoveParam Objects

```python
class AesTilesVisibilityGroupRemoveParam(AesTilesVisualApiParamBase)
```

Aes Tiles Visibility Group Remove Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_names`` (Array[Name]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupRemoveParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0, group_names: Array[Name] = []) -> None
```

<a id="unreal.AesTilesVisibilityGroupRemoveParam.group_names"></a>

#### group\_names

```python
@property
def group_names() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupRemoveParam.group_names"></a>

#### group\_names

```python
@group_names.setter
def group_names(value: Array[Name]) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam"></a>