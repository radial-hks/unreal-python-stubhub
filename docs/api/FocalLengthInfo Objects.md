## FocalLengthInfo Objects

```python
class FocalLengthInfo(StructBase)
```

Normalized focal length information for both width and height dimension
If focal length is in pixel, normalize using pixel dimensions
If focal length is in mm, normalize using sensor dimensions

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fx_fy`` (Vector2D):  [Read-Write] Value expected to be normalized (unitless)

<a id="unreal.FocalLengthInfo.__init__"></a>

#### __init__

```python
def __init__(fx_fy: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.FocalLengthInfo.fx_fy"></a>

#### fx_fy

```python
@property
def fx_fy() -> Vector2D
```

(Vector2D):  [Read-Write] Value expected to be normalized (unitless)

<a id="unreal.FocalLengthInfo.fx_fy"></a>

#### fx_fy

```python
@fx_fy.setter
def fx_fy(value: Vector2D) -> None
```

<a id="unreal.DistortionHandlerPicker"></a>