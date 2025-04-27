## MediaIOMode Objects

```python
class MediaIOMode(StructBase)
```

Identifies a media mode.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaIOCoreDefinitions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_mode_identifier`` (int32):  [Read-Only] The mode's identifier for the device.
- ``frame_rate`` (FrameRate):  [Read-Only] The mode's frame rate.
- ``resolution`` (IntPoint):  [Read-Only] The mode's image resolution.
- ``standard`` (MediaIOStandardType):  [Read-Only] The mode's scanning type.

<a id="unreal.MediaIOMode.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimationSetup"></a>