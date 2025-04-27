## STMapPointInfo Objects

```python
class STMapPointInfo(DataTablePointInfoBase)
```

ST Map Point Info struct

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``focus`` (float):  [Read-Write] Point Focus Value
- ``st_map_info`` (STMapInfo):  [Read-Write] ST Map parameter
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.STMapPointInfo.__init__"></a>

#### __init__

```python
def __init__(focus: float = 0.000000,
             zoom: float = 0.000000,
             st_map_info: STMapInfo = [None]) -> None
```

<a id="unreal.STMapPointInfo.st_map_info"></a>

#### st_map_info

```python
@property
def st_map_info() -> STMapInfo
```

(STMapInfo):  [Read-Write] ST Map parameter

<a id="unreal.STMapPointInfo.st_map_info"></a>

#### st_map_info

```python
@st_map_info.setter
def st_map_info(value: STMapInfo) -> None
```

<a id="unreal.ImageCenterPointInfo"></a>