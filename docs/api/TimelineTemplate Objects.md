## TimelineTemplate Objects

```python
class TimelineTemplate(Object)
```

Timeline Template

**C++ Source:**

- **Module**: Engine
- **File**: TimelineTemplate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_play`` (bool):  [Read-Write] If we want the timeline to auto-play
- ``ignore_time_dilation`` (bool):  [Read-Write] If we want the timeline to ignore global time dilation
- ``length_mode`` (TimelineLengthMode):  [Read-Write] How we want the timeline to determine its own length (e.g. specified length, last keyframe)
- ``loop`` (bool):  [Read-Write] If we want the timeline to loop
- ``meta_data_array`` (Array[BPVariableMetaDataEntry]):  [Read-Write] Metadata information for this timeline
- ``replicated`` (bool):  [Read-Write] If we want the timeline to loop
- ``timeline_length`` (float):  [Read-Write] Length of this timeline

<a id="unreal.TimelineTemplate.replicated"></a>

#### replicated

```python
@property
def replicated() -> bool
```

(bool):  [Read-Write] If we want the timeline to loop

<a id="unreal.TimelineTemplate.replicated"></a>

#### replicated

```python
@replicated.setter
def replicated(value: bool) -> None
```

<a id="unreal.TriggerVolume"></a>