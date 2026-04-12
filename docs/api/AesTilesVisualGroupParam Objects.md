## AesTilesVisualGroupParam Objects

```python
class AesTilesVisualGroupParam(AesTilesVisualApiParamBase)
```

Aes Tiles Visual Group Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.AesTilesVisualGroupParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0, group_name: Name = "None") -> None
```

<a id="unreal.AesTilesVisualGroupParam.group_name"></a>

#### group\_name

```python
@property
def group_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesVisualGroupParam.group_name"></a>

#### group\_name

```python
@group_name.setter
def group_name(value: Name) -> None
```

<a id="unreal.AesTilesVisualGroupUpdateNodes"></a>