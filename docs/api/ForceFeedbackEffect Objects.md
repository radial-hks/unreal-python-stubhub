## ForceFeedbackEffect Objects

```python
class ForceFeedbackEffect(Object)
```

A predefined force-feedback effect to be played on a controller

**C++ Source:**

- **Module**: Engine
- **File**: ForceFeedbackEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_details`` (Array[ForceFeedbackChannelDetails]):  [Read-Write]
- ``device_properties`` (Array[InputDeviceProperty]):  [Read-Write] A map of input device properties that we want to set while this effect is playing
- ``duration`` (float):  [Read-Only] Duration of force feedback pattern in seconds.
- ``per_device_overrides`` (Map[Name, ForceFeedbackEffectOverridenChannelDetails]):  [Read-Write] A map of platform name -> ForceFeedback channel details

<a id="unreal.ForceFeedbackEffect.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Only] Duration of force feedback pattern in seconds.

<a id="unreal.InputDeviceProperty"></a>