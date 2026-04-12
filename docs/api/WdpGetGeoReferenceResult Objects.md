## WdpGetGeoReferenceResult Objects

```python
class WdpGetGeoReferenceResult(ResultBase)
```

Wdp Get Geo Reference Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_crs`` (str):  [Read-Write]
- ``coord_type`` (WdpCoordType):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``origin`` (Vector):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``scene_crs`` (str):  [Read-Write]
- ``setting_mode`` (WdpGeoRefSettingMode):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             setting_mode: WdpGeoRefSettingMode = WdpGeoRefSettingMode.AUTO,
             coord_type: WdpCoordType = WdpCoordType.GEO,
             scene_crs: str = "",
             api_crs: str = "",
             origin: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WdpGetGeoReferenceResult.setting_mode"></a>

#### setting\_mode

```python
@property
def setting_mode() -> WdpGeoRefSettingMode
```

(WdpGeoRefSettingMode):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.setting_mode"></a>

#### setting\_mode

```python
@setting_mode.setter
def setting_mode(value: WdpGeoRefSettingMode) -> None
```

<a id="unreal.WdpGetGeoReferenceResult.coord_type"></a>

#### coord\_type

```python
@property
def coord_type() -> WdpCoordType
```

(WdpCoordType):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.coord_type"></a>

#### coord\_type

```python
@coord_type.setter
def coord_type(value: WdpCoordType) -> None
```

<a id="unreal.WdpGetGeoReferenceResult.scene_crs"></a>

#### scene\_crs

```python
@property
def scene_crs() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.scene_crs"></a>

#### scene\_crs

```python
@scene_crs.setter
def scene_crs(value: str) -> None
```

<a id="unreal.WdpGetGeoReferenceResult.api_crs"></a>

#### api\_crs

```python
@property
def api_crs() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.api_crs"></a>

#### api\_crs

```python
@api_crs.setter
def api_crs(value: str) -> None
```

<a id="unreal.WdpGetGeoReferenceResult.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpGetGeoReferenceResult.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.WdpLocalToGlobalGeoRefParams"></a>