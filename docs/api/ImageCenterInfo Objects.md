## ImageCenterInfo Objects

```python
class ImageCenterInfo(StructBase)
```

Lens camera image center parameters

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``principal_point`` (Vector2D):  [Read-Write] Value expected to be normalized [0,1]

<a id="unreal.ImageCenterInfo.__init__"></a>

#### __init__

```python
def __init__(principal_point: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.ImageCenterInfo.principal_point"></a>

#### principal_point

```python
@property
def principal_point() -> Vector2D
```

(Vector2D):  [Read-Write] Value expected to be normalized [0,1]

<a id="unreal.ImageCenterInfo.principal_point"></a>

#### principal_point

```python
@principal_point.setter
def principal_point(value: Vector2D) -> None
```

<a id="unreal.FocalLengthInfo"></a>