## FocalLengthPointInfo Objects

```python
class FocalLengthPointInfo(DataTablePointInfoBase)
```

Focal Length Point Info struct

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``focal_length_info`` (FocalLengthInfo):  [Read-Write] Focal Length parameter
- ``focus`` (float):  [Read-Write] Point Focus Value
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.FocalLengthPointInfo.__init__"></a>

#### __init__

```python
def __init__(
        focus: float = 0.000000,
        zoom: float = 0.000000,
        focal_length_info: FocalLengthInfo = [[1.000000, 1.777778]]) -> None
```

<a id="unreal.FocalLengthPointInfo.focal_length_info"></a>

#### focal_length_info

```python
@property
def focal_length_info() -> FocalLengthInfo
```

(FocalLengthInfo):  [Read-Write] Focal Length parameter

<a id="unreal.FocalLengthPointInfo.focal_length_info"></a>

#### focal_length_info

```python
@focal_length_info.setter
def focal_length_info(value: FocalLengthInfo) -> None
```

<a id="unreal.STMapPointInfo"></a>