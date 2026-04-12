## AesTilesVisualGroupVisibility Objects

```python
class AesTilesVisualGroupVisibility(AesTilesVisualGroupParam)
```

Aes Tiles Visual Group Visibility

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisualGroupVisibility.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             visible: bool = False) -> None
```

<a id="unreal.AesTilesVisualGroupVisibility.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesVisualGroupVisibility.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.AesTilesVisibilityGroupResult"></a>