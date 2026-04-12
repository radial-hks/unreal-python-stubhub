## CreateRealTimeVideosParams Objects

```python
class CreateRealTimeVideosParams(StructBase)
```

Create Real Time Videos Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RealTimeVideoParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``real_time_video_style`` (CoverRealTimeVideoStyle):  [Read-Write]

<a id="unreal.CreateRealTimeVideosParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_entity_eid: str = "",
             real_time_video_style: CoverRealTimeVideoStyle = [
                 "", [600.000000, 510.000000], [0.000000, 0.000000], 0.000000,
                 [[0.000000, 0.000000], [0.000000, 0.000000],
                  [0.000000, 0.000000], [0.000000, 0.000000]]
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreateRealTimeVideosParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateRealTimeVideosParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateRealTimeVideosParams.real_time_video_style"></a>

#### real\_time\_video\_style

```python
@property
def real_time_video_style() -> CoverRealTimeVideoStyle
```

(CoverRealTimeVideoStyle):  [Read-Write]

<a id="unreal.CreateRealTimeVideosParams.real_time_video_style"></a>

#### real\_time\_video\_style

```python
@real_time_video_style.setter
def real_time_video_style(value: CoverRealTimeVideoStyle) -> None
```

<a id="unreal.CreateRealTimeVideosParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreateRealTimeVideosParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateRealTimeVideoParams_Batch"></a>