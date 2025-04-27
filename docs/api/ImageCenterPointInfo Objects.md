## ImageCenterPointInfo Objects

```python
class ImageCenterPointInfo(DataTablePointInfoBase)
```

Image Center Point Info struct

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``focus`` (float):  [Read-Write] Point Focus Value
- ``image_center_info`` (ImageCenterInfo):  [Read-Write] Image Center parameter
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.ImageCenterPointInfo.__init__"></a>

#### __init__

```python
def __init__(
        focus: float = 0.000000,
        zoom: float = 0.000000,
        image_center_info: ImageCenterInfo = [[0.500000, 0.500000]]) -> None
```

<a id="unreal.ImageCenterPointInfo.image_center_info"></a>

#### image_center_info

```python
@property
def image_center_info() -> ImageCenterInfo
```

(ImageCenterInfo):  [Read-Write] Image Center parameter

<a id="unreal.ImageCenterPointInfo.image_center_info"></a>

#### image_center_info

```python
@image_center_info.setter
def image_center_info(value: ImageCenterInfo) -> None
```

<a id="unreal.NodalOffsetPointInfo"></a>