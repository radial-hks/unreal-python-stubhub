## GeoReferenceAtom Objects

```python
class GeoReferenceAtom(EntityAtomBase)
```

Geo Reference Atom

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpCoordinate
- **File**: GeoReferenceAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_crs`` (str):  [Read-Write] Source CRS
- ``coord_type`` (WdpCoordType):  [Read-Write]
- ``origin_location`` (Vector):  [Read-Write]
- ``origin_rotation`` (Rotator):  [Read-Write]
- ``origin_scale`` (Vector):  [Read-Write]
- ``scene_crs`` (str):  [Read-Write] Target CRS
- ``setting_mode`` (WdpGeoRefSettingMode):  [Read-Write]

<a id="unreal.GeoReferenceAtom.setting_mode"></a>

#### setting\_mode

```python
@property
def setting_mode() -> WdpGeoRefSettingMode
```

(WdpGeoRefSettingMode):  [Read-Write]

<a id="unreal.GeoReferenceAtom.setting_mode"></a>

#### setting\_mode

```python
@setting_mode.setter
def setting_mode(value: WdpGeoRefSettingMode) -> None
```

<a id="unreal.GeoReferenceAtom.coord_type"></a>

#### coord\_type

```python
@property
def coord_type() -> WdpCoordType
```

(WdpCoordType):  [Read-Write]

<a id="unreal.GeoReferenceAtom.coord_type"></a>

#### coord\_type

```python
@coord_type.setter
def coord_type(value: WdpCoordType) -> None
```

<a id="unreal.GeoReferenceAtom.scene_crs"></a>

#### scene\_crs

```python
@property
def scene_crs() -> str
```

(str):  [Read-Write] Target CRS

<a id="unreal.GeoReferenceAtom.scene_crs"></a>

#### scene\_crs

```python
@scene_crs.setter
def scene_crs(value: str) -> None
```

<a id="unreal.GeoReferenceAtom.api_crs"></a>

#### api\_crs

```python
@property
def api_crs() -> str
```

(str):  [Read-Write] Source CRS

<a id="unreal.GeoReferenceAtom.api_crs"></a>

#### api\_crs

```python
@api_crs.setter
def api_crs(value: str) -> None
```

<a id="unreal.GeoReferenceAtom.origin_location"></a>

#### origin\_location

```python
@property
def origin_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeoReferenceAtom.origin_location"></a>

#### origin\_location

```python
@origin_location.setter
def origin_location(value: Vector) -> None
```

<a id="unreal.GeoReferenceAtom.origin_rotation"></a>

#### origin\_rotation

```python
@property
def origin_rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.GeoReferenceAtom.origin_rotation"></a>

#### origin\_rotation

```python
@origin_rotation.setter
def origin_rotation(value: Rotator) -> None
```

<a id="unreal.GeoReferenceAtom.origin_scale"></a>

#### origin\_scale

```python
@property
def origin_scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeoReferenceAtom.origin_scale"></a>

#### origin\_scale

```python
@origin_scale.setter
def origin_scale(value: Vector) -> None
```

<a id="unreal.LocalGeoReferenceAtom"></a>