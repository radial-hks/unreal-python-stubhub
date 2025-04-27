## CameraFeedInfo Objects

```python
class CameraFeedInfo(StructBase)
```

Information about a camera feed, including its dimensions and aspect ratio.
The camera feed represents (potentially) an inner rect of a media input, excluding any masks / extractions that may surround it.

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aspect_ratio`` (float):  [Read-Only] Aspect Ratio of the Camera Feed
- ``dimensions`` (IntPoint):  [Read-Write] Dimensions of the Camera Feed

<a id="unreal.CameraFeedInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SimulcamInfo"></a>