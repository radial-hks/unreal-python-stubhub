## AesTilesVisualGroupUpdateName Objects

```python
class AesTilesVisualGroupUpdateName(AesTilesVisualGroupParam)
```

Aes Tiles Visual Group Update Name

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``target_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesVisualGroupUpdateName.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             target_name: Name = "None") -> None
```

<a id="unreal.AesTilesVisualGroupUpdateName.target_name"></a>

#### target\_name

```python
@property
def target_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesVisualGroupUpdateName.target_name"></a>

#### target\_name

```python
@target_name.setter
def target_name(value: Name) -> None
```

<a id="unreal.AesTilesVisualGroupMoveNodes"></a>