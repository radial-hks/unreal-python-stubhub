## SubmixEffectStereoDelayPreset Objects

```python
class SubmixEffectStereoDelayPreset(SoundEffectSubmixPreset)
```

USubmixEffectDelayPreset
Class which processes audio streams and uses parameters defined in the preset class.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectStereoDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectStereoDelaySettings):  [Read-Write]

<a id="unreal.SubmixEffectStereoDelayPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectStereoDelaySettings
```

(SubmixEffectStereoDelaySettings):  [Read-Write]

<a id="unreal.SubmixEffectStereoDelayPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectStereoDelaySettings) -> None
```

<a id="unreal.SubmixEffectStereoDelayPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectStereoDelaySettings) -> None
```

x.set_settings(settings) -> None
Set all tap delay settings. This will replace any dynamically added or modified taps.

Args:
    settings (SubmixEffectStereoDelaySettings):

<a id="unreal.SubmixEffectStereoToQuadPreset"></a>