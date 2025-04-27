## DistortionInfo Objects

```python
class DistortionInfo(StructBase)
```

Lens distortion parameters

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameters`` (Array[float]):  [Read-Write] Generic array of floating-point lens distortion parameters

<a id="unreal.DistortionInfo.__init__"></a>

#### __init__

```python
def __init__(parameters: Array[float] = []) -> None
```

<a id="unreal.DistortionInfo.parameters"></a>

#### parameters

```python
@property
def parameters() -> Array[float]
```

(Array[float]):  [Read-Write] Generic array of floating-point lens distortion parameters

<a id="unreal.DistortionInfo.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: Array[float]) -> None
```

<a id="unreal.NodalPointOffset"></a>