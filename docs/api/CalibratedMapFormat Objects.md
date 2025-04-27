## CalibratedMapFormat Objects

```python
class CalibratedMapFormat(StructBase)
```

Formatting options for processing a calibrated map

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: CalibratedMapFormat.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distortion_channels`` (CalibratedMapChannels):  [Read-Write] Specifies which two channels contain the distortion map (or None if there is no distortion data)
- ``pixel_origin`` (CalibratedMapPixelOrigin):  [Read-Write] Specifies where in the image the (0, 0) pixel is
- ``undistortion_channels`` (CalibratedMapChannels):  [Read-Write] Specifies which two channels contain the undistortion map (or None if there is no undistortion data)

<a id="unreal.CalibratedMapFormat.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.TakeRecorderTrackSettings"></a>