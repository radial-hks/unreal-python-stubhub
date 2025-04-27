## SoundWaveTimecodeInfo Objects

```python
class SoundWaveTimecodeInfo(StructBase)
```

Sound Wave Timecode Info

**C++ Source:**

- **Module**: Engine
- **File**: SoundWaveTimecodeInfo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Only]
- ``num_samples_per_second`` (uint32):  [Read-Only]
- ``num_samples_since_midnight`` (uint64):  [Read-Only]
- ``originator_date`` (str):  [Read-Only]
- ``originator_description`` (str):  [Read-Only]
- ``originator_reference`` (str):  [Read-Only]
- ``originator_time`` (str):  [Read-Only]
- ``timecode_is_drop_frame`` (bool):  [Read-Only]
- ``timecode_rate`` (FrameRate):  [Read-Only]

<a id="unreal.SoundWaveTimecodeInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SoundWaveCloudStreamingPlatformSettings"></a>