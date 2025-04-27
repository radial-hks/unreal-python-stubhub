## LensInfo Objects

```python
class LensInfo(StructBase)
```

Information about the lens rig

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``image_dimensions`` (IntPoint):  [Read-Write] Resolution of the original footage that was captured by the camera (not necessarily the resolution of the media source).
  For example, the original footage might have been 4320x1746, but to transmit that image over SDI, it might have been scaled and fit into a 4096x2160 frame.
  In this case, the "Image Resolution" should be set to 4320x1746, while the "Media Resolution" will read 4096x2160.
- ``lens_model`` (type(Class)):  [Read-Write] Model of the lens (spherical, anamorphic, etc...)
- ``lens_model_name`` (str):  [Read-Write] Model name of the lens
- ``lens_serial_number`` (str):  [Read-Write] Serial number of the lens
- ``sensor_dimensions`` (Vector2D):  [Read-Write] Width and height of the calibrated camera's sensor, in millimeters
- ``squeeze_factor`` (float):  [Read-Write] Squeeze Factor (or Pixel Aspect) for anamorphic lenses. Spherical Lenses should keep this default to 1.0f

<a id="unreal.LensInfo.__init__"></a>

#### __init__

```python
def __init__(lens_model_name: str = "",
             lens_serial_number: str = "",
             lens_model: Class = None,
             sensor_dimensions: Vector2D = [0.000000, 0.000000],
             image_dimensions: IntPoint = [0, 0],
             squeeze_factor: float = 0.000000) -> None
```

<a id="unreal.LensInfo.lens_model_name"></a>

#### lens_model_name

```python
@property
def lens_model_name() -> str
```

(str):  [Read-Write] Model name of the lens

<a id="unreal.LensInfo.lens_model_name"></a>

#### lens_model_name

```python
@lens_model_name.setter
def lens_model_name(value: str) -> None
```

<a id="unreal.LensInfo.lens_serial_number"></a>

#### lens_serial_number

```python
@property
def lens_serial_number() -> str
```

(str):  [Read-Write] Serial number of the lens

<a id="unreal.LensInfo.lens_serial_number"></a>

#### lens_serial_number

```python
@lens_serial_number.setter
def lens_serial_number(value: str) -> None
```

<a id="unreal.LensInfo.lens_model"></a>

#### lens_model

```python
@property
def lens_model() -> Class
```

(type(Class)):  [Read-Write] Model of the lens (spherical, anamorphic, etc...)

<a id="unreal.LensInfo.lens_model"></a>

#### lens_model

```python
@lens_model.setter
def lens_model(value: Class) -> None
```

<a id="unreal.LensInfo.sensor_dimensions"></a>

#### sensor_dimensions

```python
@property
def sensor_dimensions() -> Vector2D
```

(Vector2D):  [Read-Write] Width and height of the calibrated camera's sensor, in millimeters

<a id="unreal.LensInfo.sensor_dimensions"></a>

#### sensor_dimensions

```python
@sensor_dimensions.setter
def sensor_dimensions(value: Vector2D) -> None
```

<a id="unreal.LensInfo.image_dimensions"></a>

#### image_dimensions

```python
@property
def image_dimensions() -> IntPoint
```

(IntPoint):  [Read-Write] Resolution of the original footage that was captured by the camera (not necessarily the resolution of the media source).
For example, the original footage might have been 4320x1746, but to transmit that image over SDI, it might have been scaled and fit into a 4096x2160 frame.
In this case, the "Image Resolution" should be set to 4320x1746, while the "Media Resolution" will read 4096x2160.

<a id="unreal.LensInfo.image_dimensions"></a>

#### image_dimensions

```python
@image_dimensions.setter
def image_dimensions(value: IntPoint) -> None
```

<a id="unreal.LensInfo.squeeze_factor"></a>

#### squeeze_factor

```python
@property
def squeeze_factor() -> float
```

(float):  [Read-Write] Squeeze Factor (or Pixel Aspect) for anamorphic lenses. Spherical Lenses should keep this default to 1.0f

<a id="unreal.LensInfo.squeeze_factor"></a>

#### squeeze_factor

```python
@squeeze_factor.setter
def squeeze_factor(value: float) -> None
```

<a id="unreal.CameraFeedInfo"></a>