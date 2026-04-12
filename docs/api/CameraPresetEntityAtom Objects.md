## CameraPresetEntityAtom Objects

```python
class CameraPresetEntityAtom(EntityAtomBase)
```

Camera Preset Entity Atom

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraPresetEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mode`` (str):  [Read-Write]
- ``default_camera`` (bool):  [Read-Write]
- ``field_of_view`` (float):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.default_camera"></a>

#### default\_camera

```python
@property
def default_camera() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.default_camera"></a>

#### default\_camera

```python
@default_camera.setter
def default_camera(value: bool) -> None
```

<a id="unreal.CameraPresetEntityAtom.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.CameraPresetEntityAtom.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.CameraPresetEntityAtom.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.CameraPresetEntityAtom.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.CameraPresetEntityAtom.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.CameraPresetEntityAtom.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.CameraPresetEntityAtom.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> str
```

(str):  [Read-Write]

<a id="unreal.CameraPresetEntityAtom.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: str) -> None
```

<a id="unreal.CameraRoamAtom"></a>