## CesiumCamera Objects

```python
class CesiumCamera(StructBase)
```

brief: A camera description that {
link: Cesium3DTileset}s can use to decide what tiles need to be loaded to sufficiently cover the camera view.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumCamera.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_of_view_degrees`` (double):  [Read-Write]
  brief: The horizontal field of view of the camera in degrees.
- ``location`` (Vector):  [Read-Write]
  brief: The Unreal location of the camera.
- ``override_aspect_ratio`` (double):  [Read-Write]
  brief: The overriden aspect ratio for this camera. When this is 0.0f, use the aspect ratio implied by ViewportSize. This may be different from the aspect ratio implied by the ViewportSize and black bars are added as needed in order to achieve this aspect ratio within a larger viewport.
- ``rotation`` (Rotator):  [Read-Write]
  brief: The Unreal rotation of the camera.
- ``viewport_size`` (Vector2D):  [Read-Write]
  brief: The pixel dimensions of the viewport.

<a id="unreal.CesiumCamera.__init__"></a>

#### \_\_init\_\_

```python
def __init__(viewport_size: Vector2D = [0.000000, 0.000000],
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             field_of_view_degrees: float = 0.000000,
             override_aspect_ratio: float = 0.000000) -> None
```

<a id="unreal.CesiumCamera.viewport_size"></a>

#### viewport\_size

```python
@property
def viewport_size() -> Vector2D
```

(Vector2D):  [Read-Write]
brief: The pixel dimensions of the viewport.

<a id="unreal.CesiumCamera.viewport_size"></a>

#### viewport\_size

```python
@viewport_size.setter
def viewport_size(value: Vector2D) -> None
```

<a id="unreal.CesiumCamera.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]
brief: The Unreal location of the camera.

<a id="unreal.CesiumCamera.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.CesiumCamera.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]
brief: The Unreal rotation of the camera.

<a id="unreal.CesiumCamera.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.CesiumCamera.field_of_view_degrees"></a>

#### field\_of\_view\_degrees

```python
@property
def field_of_view_degrees() -> float
```

(double):  [Read-Write]
brief: The horizontal field of view of the camera in degrees.

<a id="unreal.CesiumCamera.field_of_view_degrees"></a>

#### field\_of\_view\_degrees

```python
@field_of_view_degrees.setter
def field_of_view_degrees(value: float) -> None
```

<a id="unreal.CesiumCamera.override_aspect_ratio"></a>

#### override\_aspect\_ratio

```python
@property
def override_aspect_ratio() -> float
```

(double):  [Read-Write]
brief: The overriden aspect ratio for this camera. When this is 0.0f, use the aspect ratio implied by ViewportSize. This may be different from the aspect ratio implied by the ViewportSize and black bars are added as needed in order to achieve this aspect ratio within a larger viewport.

<a id="unreal.CesiumCamera.override_aspect_ratio"></a>

#### override\_aspect\_ratio

```python
@override_aspect_ratio.setter
def override_aspect_ratio(value: float) -> None
```

<a id="unreal.CesiumFeatureIdAttribute"></a>