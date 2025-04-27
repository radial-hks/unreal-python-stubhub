## DistortionPointInfo Objects

```python
class DistortionPointInfo(DataTablePointInfoBase)
```

Distortion Point Info struct

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distortion_info`` (DistortionInfo):  [Read-Write] Lens distortion parameter
- ``focus`` (float):  [Read-Write] Point Focus Value
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.DistortionPointInfo.__init__"></a>

#### __init__

```python
def __init__(focus: float = 0.000000,
             zoom: float = 0.000000,
             distortion_info: DistortionInfo = [[]]) -> None
```

<a id="unreal.DistortionPointInfo.distortion_info"></a>

#### distortion_info

```python
@property
def distortion_info() -> DistortionInfo
```

(DistortionInfo):  [Read-Write] Lens distortion parameter

<a id="unreal.DistortionPointInfo.distortion_info"></a>

#### distortion_info

```python
@distortion_info.setter
def distortion_info(value: DistortionInfo) -> None
```

<a id="unreal.FocalLengthPointInfo"></a>