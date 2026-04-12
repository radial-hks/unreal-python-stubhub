## WdpGlobalGetCoordZTypeParams Objects

```python
class WdpGlobalGetCoordZTypeParams(ResultBase)
```

Wdp Global Get Coord ZType Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_type_value`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGlobalGetCoordZTypeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             coord_z_type_value: int = 0) -> None
```

<a id="unreal.WdpGlobalGetCoordZTypeParams.coord_z_type_value"></a>

#### coord\_z\_type\_value

```python
@property
def coord_z_type_value() -> int
```

(int32):  [Read-Write]

<a id="unreal.WdpGlobalGetCoordZTypeParams.coord_z_type_value"></a>

#### coord\_z\_type\_value

```python
@coord_z_type_value.setter
def coord_z_type_value(value: int) -> None
```

<a id="unreal.WdpWorldPosParams"></a>