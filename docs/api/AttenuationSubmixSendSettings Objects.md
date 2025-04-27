## AttenuationSubmixSendSettings Objects

```python
class AttenuationSubmixSendSettings(SoundSubmixSendInfoBase)
```

Attenuation Submix Send Settings

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_send_level_curve`` (RuntimeFloatCurve):  [Read-Write] The custom reverb send curve to use for distance-based send level.
- ``disable_manual_send_clamp`` (bool):  [Read-Write] Whether to disable the 0-1 clamp for manual SendLevel control
- ``max_send_distance`` (float):  [Read-Write] The max distance to send to the master
- ``max_send_level`` (float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the max send distance.
- ``min_send_distance`` (float):  [Read-Write] The min distance to send to the master
- ``min_send_level`` (float):  [Read-Write] The amount to send to master when sound is located at a distance equal to value specified in the min send distance.
- ``send_level`` (float):  [Read-Write] The amount of audio to send
- ``send_level_control_method`` (SendLevelControlMethod):  [Read-Write] Manual: Use Send Level only
  Linear: Interpolate between Min and Max Send Levels based on listener distance (between Distance Min and Distance Max)
  Custom Curve: Use the float curve to map Send Level to distance (0.0-1.0 on curve maps to Distance Min - Distance Max)
- ``sound_submix`` (SoundSubmixBase):  [Read-Write] The submix to send the audio to

<a id="unreal.AttenuationSubmixSendSettings.__init__"></a>

#### __init__

```python
def __init__(send_level_control_method:
             SendLevelControlMethod = SendLevelControlMethod.LINEAR,
             sound_submix: SoundSubmixBase = None,
             send_level: float = 0.000000,
             disable_manual_send_clamp: bool = False,
             min_send_level: float = 0.000000,
             max_send_level: float = 0.000000,
             min_send_distance: float = 0.000000,
             max_send_distance: float = 0.000000,
             custom_send_level_curve: RuntimeFloatCurve = []) -> None
```

<a id="unreal.SoundAttenuationSettings"></a>