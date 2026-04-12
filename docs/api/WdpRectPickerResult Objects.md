## WdpRectPickerResult Objects

```python
class WdpRectPickerResult(ResultBase)
```

Wdp Rect Picker Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpRectPickerResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             eids: Array[int] = []) -> None
```

<a id="unreal.WdpRectPickerResult.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.WdpRectPickerResult.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.PickMaterialApiResult"></a>