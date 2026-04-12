## CameraStartAtom Objects

```python
class CameraStartAtom(EntityAtomBase)
```

Camera Start Atom

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraStartAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mode`` (str):  [Read-Write]
- ``field_of_view`` (float):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``location_limit`` (Array[Vector2D]):  [Read-Write]
- ``pitch_limit`` (Vector2D):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``view_distance_limit`` (Vector2D):  [Read-Write]
- ``yaw_limit`` (Vector2D):  [Read-Write]

<a id="unreal.CameraStartAtom.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.CameraStartAtom.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.CameraStartAtom.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.CameraStartAtom.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.CameraStartAtom.location_limit"></a>

#### location\_limit

```python
@property
def location_limit() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.CameraStartAtom.location_limit"></a>

#### location\_limit

```python
@location_limit.setter
def location_limit(value: Array[Vector2D]) -> None
```

<a id="unreal.CameraStartAtom.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraStartAtom.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.CameraStartAtom.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraStartAtom.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.CameraStartAtom.view_distance_limit"></a>

#### view\_distance\_limit

```python
@property
def view_distance_limit() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CameraStartAtom.view_distance_limit"></a>

#### view\_distance\_limit

```python
@view_distance_limit.setter
def view_distance_limit(value: Vector2D) -> None
```

<a id="unreal.CameraStartAtom.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.CameraStartAtom.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.CameraStartAtom.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> str
```

(str):  [Read-Write]

<a id="unreal.CameraStartAtom.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: str) -> None
```

<a id="unreal.MaterialAtom"></a>