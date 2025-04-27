## NodalOffsetPointInfo Objects

```python
class NodalOffsetPointInfo(DataTablePointInfoBase)
```

Nodal Point Point Info struct

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``focus`` (float):  [Read-Write] Point Focus Value
- ``nodal_point_offset`` (NodalPointOffset):  [Read-Write] Nodal Point parameter
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.NodalOffsetPointInfo.__init__"></a>

#### __init__

```python
def __init__(
    focus: float = 0.000000,
    zoom: float = 0.000000,
    nodal_point_offset: NodalPointOffset = [[0.000000, 0.000000, 0.000000],
                                            [
                                                0.000000, 0.000000, 0.000000,
                                                1.000000
                                            ]]
) -> None
```

<a id="unreal.NodalOffsetPointInfo.nodal_point_offset"></a>

#### nodal_point_offset

```python
@property
def nodal_point_offset() -> NodalPointOffset
```

(NodalPointOffset):  [Read-Write] Nodal Point parameter

<a id="unreal.NodalOffsetPointInfo.nodal_point_offset"></a>

#### nodal_point_offset

```python
@nodal_point_offset.setter
def nodal_point_offset(value: NodalPointOffset) -> None
```

<a id="unreal.LensDistortionState"></a>