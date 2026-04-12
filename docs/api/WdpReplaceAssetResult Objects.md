## WdpReplaceAssetResult Objects

```python
class WdpReplaceAssetResult(ResultBase)
```

Wdp Replace Asset Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: WdpAssetAPI
- **File**: WdpAssetAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``old_to_new_eids`` (Map[int64, int64]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.WdpReplaceAssetResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             type: str = "",
             old_to_new_eids: Map[int, int] = {}) -> None
```

<a id="unreal.WdpReplaceAssetResult.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpReplaceAssetResult.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.WdpReplaceAssetResult.old_to_new_eids"></a>

#### old\_to\_new\_eids

```python
@property
def old_to_new_eids() -> Map[int, int]
```

(Map[int64, int64]):  [Read-Write]

<a id="unreal.WdpReplaceAssetResult.old_to_new_eids"></a>

#### old\_to\_new\_eids

```python
@old_to_new_eids.setter
def old_to_new_eids(value: Map[int, int]) -> None
```

<a id="unreal.WdpGetMeshSizeByIdParams"></a>