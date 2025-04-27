## SubmixEffectStereoToQuadPreset Objects

```python
class SubmixEffectStereoToQuadPreset(SoundEffectSubmixPreset)
```

Submix effect which sends stereo audio to quad (left surround and right surround) if the channel count is greater than 2.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectStereoToQuad.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubmixEffectStereoToQuadSettings):  [Read-Write]

<a id="unreal.SubmixEffectStereoToQuadPreset.settings"></a>

#### settings

```python
@property
def settings() -> SubmixEffectStereoToQuadSettings
```

(SubmixEffectStereoToQuadSettings):  [Read-Write]

<a id="unreal.SubmixEffectStereoToQuadPreset.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SubmixEffectStereoToQuadSettings) -> None
```

<a id="unreal.SubmixEffectStereoToQuadPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SubmixEffectStereoToQuadSettings) -> None
```

x.set_settings(settings) -> None
Set all tap delay settings. This will replace any dynamically added or modified taps.

Args:
    settings (SubmixEffectStereoToQuadSettings):

<a id="unreal.SubmixEffectTapDelayPreset"></a>