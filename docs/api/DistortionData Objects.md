## DistortionData Objects

```python
class DistortionData(StructBase)
```

Distortion data evaluated for given FZ pair based on lens parameters

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distorted_u_vs`` (Array[Vector2D]):  [Read-Only]
- ``overscan_factor`` (float):  [Read-Write] Estimated overscan factor based on distortion to have distorted cg covering full size

<a id="unreal.DistortionData.__init__"></a>

#### __init__

```python
def __init__(distorted_u_vs: Array[Vector2D] = [],
             overscan_factor: float = 0.000000) -> None
```

<a id="unreal.DistortionData.distorted_u_vs"></a>

#### distorted_u_vs

```python
@property
def distorted_u_vs() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Only]

<a id="unreal.DistortionData.overscan_factor"></a>

#### overscan_factor

```python
@property
def overscan_factor() -> float
```

(float):  [Read-Write] Estimated overscan factor based on distortion to have distorted cg covering full size

<a id="unreal.DistortionData.overscan_factor"></a>

#### overscan_factor

```python
@overscan_factor.setter
def overscan_factor(value: float) -> None
```

<a id="unreal.DataTablePointInfoBase"></a>