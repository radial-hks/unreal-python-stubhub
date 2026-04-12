## GetSectionParams Objects

```python
class GetSectionParams(ResultBase)
```

Get Section Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetSectionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             coord_z_ref: str = "") -> None
```

<a id="unreal.GetSectionParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> str
```

(str):  [Read-Write]

<a id="unreal.GetSectionParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: str) -> None
```

<a id="unreal.UpdateSectionParams"></a>