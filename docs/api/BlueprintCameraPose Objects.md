## BlueprintCameraPose Objects

```python
class BlueprintCameraPose(StructBase)
```

Represents a camera pose.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aperture`` (float):  [Read-Write] The aperture (f-stop) of the camera's lens.
- ``aspect_ratio_axis_constraint`` (AspectRatioAxisConstraint):  [Read-Write] The aspect ratio axis constraint to use if aspect ratio is constrained.
- ``constrain_aspect_ratio`` (bool):  [Read-Write] Whether the camera should constrain aspect ratio.
- ``diaphragm_blade_count`` (int32):  [Read-Write] Number of blades in the lens diaphragm
- ``enable_physical_camera`` (bool):  [Read-Write] Whether to setup post-process settings based on physical camera properties such as Aperture,
  FocusDistance, DiaphragmBladeCount, and so on.
- ``far_clipping_plane`` (float):  [Read-Write] The camera's far clipping plane.
- ``field_of_view`` (float):  [Read-Write] The field of view of the camera. May be negative if driven by focal length.
- ``focal_length`` (float):  [Read-Write] The focal length of the camera. May be negative if driven directly by field of view.
- ``focus_distance`` (float):  [Read-Write] The focus distance of the camera, if different from target distance.
- ``iso`` (float):  [Read-Write] The camera sensor sensitivity in ISO.
- ``location`` (Vector):  [Read-Write] The location of the camera.
- ``near_clipping_plane`` (float):  [Read-Write] The camera's near clipping plane.
- ``rotation`` (Rotator):  [Read-Write] The rotation of the camera.
- ``sensor_height`` (float):  [Read-Write] The height of the camera's sensor.
- ``sensor_width`` (float):  [Read-Write] The width of the camera's sensor.
- ``shutter_speed`` (float):  [Read-Write] The shutter speed of the camera's lens, in 1/seconds
- ``squeeze_factor`` (float):  [Read-Write] The squeeze factor of the camera's lens.
- ``target_distance`` (double):  [Read-Write] The distance of the target of the camera.

<a id="unreal.BlueprintCameraPose.__init__"></a>

#### __init__

```python
def __init__(
    location: Vector = [0.000000, 0.000000, 0.000000],
    rotation: Rotator = [0.000000, 0.000000, 0.000000],
    target_distance: float = 0.000000,
    field_of_view: float = 0.000000,
    focal_length: float = 0.000000,
    aperture: float = 0.000000,
    shutter_speed: float = 0.000000,
    focus_distance: float = 0.000000,
    sensor_width: float = 0.000000,
    sensor_height: float = 0.000000,
    iso: float = 0.000000,
    squeeze_factor: float = 0.000000,
    diaphragm_blade_count: int = 0,
    near_clipping_plane: float = 0.000000,
    far_clipping_plane: float = 0.000000,
    enable_physical_camera: bool = False,
    constrain_aspect_ratio: bool = False,
    aspect_ratio_axis_constraint:
    AspectRatioAxisConstraint = AspectRatioAxisConstraint.
    ASPECT_RATIO_MAINTAIN_YFOV
) -> None
```

<a id="unreal.BlueprintCameraPose.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] The location of the camera.

<a id="unreal.BlueprintCameraPose.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.BlueprintCameraPose.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] The rotation of the camera.

<a id="unreal.BlueprintCameraPose.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.BlueprintCameraPose.target_distance"></a>

#### target_distance

```python
@property
def target_distance() -> float
```

(double):  [Read-Write] The distance of the target of the camera.

<a id="unreal.BlueprintCameraPose.target_distance"></a>

#### target_distance

```python
@target_distance.setter
def target_distance(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.field_of_view"></a>

#### field_of_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write] The field of view of the camera. May be negative if driven by focal length.

<a id="unreal.BlueprintCameraPose.field_of_view"></a>

#### field_of_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.focal_length"></a>

#### focal_length

```python
@property
def focal_length() -> float
```

(float):  [Read-Write] The focal length of the camera. May be negative if driven directly by field of view.

<a id="unreal.BlueprintCameraPose.focal_length"></a>

#### focal_length

```python
@focal_length.setter
def focal_length(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.aperture"></a>

#### aperture

```python
@property
def aperture() -> float
```

(float):  [Read-Write] The aperture (f-stop) of the camera's lens.

<a id="unreal.BlueprintCameraPose.aperture"></a>

#### aperture

```python
@aperture.setter
def aperture(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.shutter_speed"></a>

#### shutter_speed

```python
@property
def shutter_speed() -> float
```

(float):  [Read-Write] The shutter speed of the camera's lens, in 1/seconds

<a id="unreal.BlueprintCameraPose.shutter_speed"></a>

#### shutter_speed

```python
@shutter_speed.setter
def shutter_speed(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.focus_distance"></a>

#### focus_distance

```python
@property
def focus_distance() -> float
```

(float):  [Read-Write] The focus distance of the camera, if different from target distance.

<a id="unreal.BlueprintCameraPose.focus_distance"></a>

#### focus_distance

```python
@focus_distance.setter
def focus_distance(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.sensor_width"></a>

#### sensor_width

```python
@property
def sensor_width() -> float
```

(float):  [Read-Write] The width of the camera's sensor.

<a id="unreal.BlueprintCameraPose.sensor_width"></a>

#### sensor_width

```python
@sensor_width.setter
def sensor_width(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.sensor_height"></a>

#### sensor_height

```python
@property
def sensor_height() -> float
```

(float):  [Read-Write] The height of the camera's sensor.

<a id="unreal.BlueprintCameraPose.sensor_height"></a>

#### sensor_height

```python
@sensor_height.setter
def sensor_height(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.iso"></a>

#### iso

```python
@property
def iso() -> float
```

(float):  [Read-Write] The camera sensor sensitivity in ISO.

<a id="unreal.BlueprintCameraPose.iso"></a>

#### iso

```python
@iso.setter
def iso(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.squeeze_factor"></a>

#### squeeze_factor

```python
@property
def squeeze_factor() -> float
```

(float):  [Read-Write] The squeeze factor of the camera's lens.

<a id="unreal.BlueprintCameraPose.squeeze_factor"></a>

#### squeeze_factor

```python
@squeeze_factor.setter
def squeeze_factor(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.diaphragm_blade_count"></a>

#### diaphragm_blade_count

```python
@property
def diaphragm_blade_count() -> int
```

(int32):  [Read-Write] Number of blades in the lens diaphragm

<a id="unreal.BlueprintCameraPose.diaphragm_blade_count"></a>

#### diaphragm_blade_count

```python
@diaphragm_blade_count.setter
def diaphragm_blade_count(value: int) -> None
```

<a id="unreal.BlueprintCameraPose.near_clipping_plane"></a>

#### near_clipping_plane

```python
@property
def near_clipping_plane() -> float
```

(float):  [Read-Write] The camera's near clipping plane.

<a id="unreal.BlueprintCameraPose.near_clipping_plane"></a>

#### near_clipping_plane

```python
@near_clipping_plane.setter
def near_clipping_plane(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.far_clipping_plane"></a>

#### far_clipping_plane

```python
@property
def far_clipping_plane() -> float
```

(float):  [Read-Write] The camera's far clipping plane.

<a id="unreal.BlueprintCameraPose.far_clipping_plane"></a>

#### far_clipping_plane

```python
@far_clipping_plane.setter
def far_clipping_plane(value: float) -> None
```

<a id="unreal.BlueprintCameraPose.enable_physical_camera"></a>

#### enable_physical_camera

```python
@property
def enable_physical_camera() -> bool
```

(bool):  [Read-Write] Whether to setup post-process settings based on physical camera properties such as Aperture,
FocusDistance, DiaphragmBladeCount, and so on.

<a id="unreal.BlueprintCameraPose.enable_physical_camera"></a>

#### enable_physical_camera

```python
@enable_physical_camera.setter
def enable_physical_camera(value: bool) -> None
```

<a id="unreal.BlueprintCameraPose.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@property
def constrain_aspect_ratio() -> bool
```

(bool):  [Read-Write] Whether the camera should constrain aspect ratio.

<a id="unreal.BlueprintCameraPose.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@constrain_aspect_ratio.setter
def constrain_aspect_ratio(value: bool) -> None
```

<a id="unreal.BlueprintCameraPose.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@property
def aspect_ratio_axis_constraint() -> AspectRatioAxisConstraint
```

(AspectRatioAxisConstraint):  [Read-Write] The aspect ratio axis constraint to use if aspect ratio is constrained.

<a id="unreal.BlueprintCameraPose.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@aspect_ratio_axis_constraint.setter
def aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
```

<a id="unreal.BlueprintCameraVariableTable"></a>