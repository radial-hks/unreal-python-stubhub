## TimecodeCustomAttributeNameSettings Objects

```python
class TimecodeCustomAttributeNameSettings(StructBase)
```

Settings that identify the names of custom attributes that represent the individual components of a timecode and a subframe along with a take name.

**C++ Source:**

- **Module**: Engine
- **File**: CustomAttributes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the frame component of a timecode.
- ``hour_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the hour component of a timecode.
- ``minute_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the minute component of a timecode.
- ``rate_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the timecode rate. This may be different from
            the animation or capture frame rate, for example when capturing "high" frame rate data
                at 120 frames per second but recording SMPTE timecode at 30 frames per second.
- ``second_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the second component of a timecode.
- ``subframe_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing a subframe value. Though not strictly a component
                of a timecode, this attribute can be authored to identify samples in between timecodes.
- ``takename_attribute_name`` (Name):  [Read-Write] Name of the custom attribute representing the name of a take.

<a id="unreal.TimecodeCustomAttributeNameSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CustomAttributeSetting"></a>