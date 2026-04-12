## GetWindowParams Objects

```python
class GetWindowParams(ResultBase)
```

Get Window Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: WindowAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``window_style`` (CoverWindowStyle):  [Read-Write]

<a id="unreal.GetWindowParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point_entity_eid: str = "",
             window_style: CoverWindowStyle = [
                 "", [600.000000, 510.000000], [0.000000, 0.000000]
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.GetWindowParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GetWindowParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.GetWindowParams.window_style"></a>

#### window\_style

```python
@property
def window_style() -> CoverWindowStyle
```

(CoverWindowStyle):  [Read-Write]

<a id="unreal.GetWindowParams.window_style"></a>

#### window\_style

```python
@window_style.setter
def window_style(value: CoverWindowStyle) -> None
```

<a id="unreal.GetWindowParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.GetWindowParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateWindowsParams"></a>