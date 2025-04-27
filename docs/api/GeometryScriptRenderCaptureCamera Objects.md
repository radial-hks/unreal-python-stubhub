## GeometryScriptRenderCaptureCamera Objects

```python
class GeometryScriptRenderCaptureCamera(StructBase)
```

Render Capture data structures

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_of_view_degrees`` (double):  [Read-Write]
- ``near_plane_dist`` (double):  [Read-Write]
- ``resolution`` (int32):  [Read-Write] The pixel resolution of render capture photo set, this value is used for width and height
- ``view_direction`` (Vector):  [Read-Write]
- ``view_position`` (Vector):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamera.__init__"></a>

#### __init__

```python
def __init__(resolution: int = 0,
             field_of_view_degrees: float = 0.000000,
             view_position: Vector = [0.000000, 0.000000, 0.000000],
             view_direction: Vector = [0.000000, 0.000000, 0.000000],
             near_plane_dist: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamera.resolution"></a>

#### resolution

```python
@property
def resolution() -> int
```

(int32):  [Read-Write] The pixel resolution of render capture photo set, this value is used for width and height

<a id="unreal.GeometryScriptRenderCaptureCamera.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: int) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamera.field_of_view_degrees"></a>

#### field_of_view_degrees

```python
@property
def field_of_view_degrees() -> float
```

(double):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamera.field_of_view_degrees"></a>

#### field_of_view_degrees

```python
@field_of_view_degrees.setter
def field_of_view_degrees(value: float) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamera.view_position"></a>

#### view_position

```python
@property
def view_position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamera.view_position"></a>

#### view_position

```python
@view_position.setter
def view_position(value: Vector) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamera.view_direction"></a>

#### view_direction

```python
@property
def view_direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamera.view_direction"></a>

#### view_direction

```python
@view_direction.setter
def view_direction(value: Vector) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamera.near_plane_dist"></a>

#### near_plane_dist

```python
@property
def near_plane_dist() -> float
```

(double):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamera.near_plane_dist"></a>

#### near_plane_dist

```python
@near_plane_dist.setter
def near_plane_dist(value: float) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions"></a>