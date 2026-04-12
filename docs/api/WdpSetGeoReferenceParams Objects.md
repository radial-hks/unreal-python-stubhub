## WdpSetGeoReferenceParams Objects

```python
class WdpSetGeoReferenceParams(ParamsBase)
```

Wdp Set Geo Reference Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_crs`` (str):  [Read-Write]
- ``coord_type`` (WdpCoordType):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``origin`` (Vector):  [Read-Write]
- ``scene_crs`` (str):  [Read-Write]
- ``setting_mode`` (WdpGeoRefSettingMode):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(setting_mode: WdpGeoRefSettingMode = WdpGeoRefSettingMode.AUTO,
             coord_type: WdpCoordType = WdpCoordType.GEO,
             scene_crs: str = "",
             api_crs: str = "",
             origin: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WdpSetGeoReferenceParams.setting_mode"></a>

#### setting\_mode

```python
@property
def setting_mode() -> WdpGeoRefSettingMode
```

(WdpGeoRefSettingMode):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.setting_mode"></a>

#### setting\_mode

```python
@setting_mode.setter
def setting_mode(value: WdpGeoRefSettingMode) -> None
```

<a id="unreal.WdpSetGeoReferenceParams.coord_type"></a>

#### coord\_type

```python
@property
def coord_type() -> WdpCoordType
```

(WdpCoordType):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.coord_type"></a>

#### coord\_type

```python
@coord_type.setter
def coord_type(value: WdpCoordType) -> None
```

<a id="unreal.WdpSetGeoReferenceParams.scene_crs"></a>

#### scene\_crs

```python
@property
def scene_crs() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.scene_crs"></a>

#### scene\_crs

```python
@scene_crs.setter
def scene_crs(value: str) -> None
```

<a id="unreal.WdpSetGeoReferenceParams.api_crs"></a>

#### api\_crs

```python
@property
def api_crs() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.api_crs"></a>

#### api\_crs

```python
@api_crs.setter
def api_crs(value: str) -> None
```

<a id="unreal.WdpSetGeoReferenceParams.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpSetGeoReferenceParams.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.WdpGetGeoReferenceResult"></a>