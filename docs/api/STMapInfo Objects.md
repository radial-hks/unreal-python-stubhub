## STMapInfo Objects

```python
class STMapInfo(StructBase)
```

Pre generate STMap and normalized focal length information

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distortion_map`` (Texture):  [Read-Write] Pre calibrated UVMap/STMap
- ``map_format`` (CalibratedMapFormat):  [Read-Write] Calibrated map format

<a id="unreal.STMapInfo.__init__"></a>

#### __init__

```python
def __init__(distortion_map: Texture = None) -> None
```

<a id="unreal.STMapInfo.distortion_map"></a>

#### distortion_map

```python
@property
def distortion_map() -> Texture
```

(Texture):  [Read-Write] Pre calibrated UVMap/STMap

<a id="unreal.STMapInfo.distortion_map"></a>

#### distortion_map

```python
@distortion_map.setter
def distortion_map(value: Texture) -> None
```

<a id="unreal.DistortionInfo"></a>