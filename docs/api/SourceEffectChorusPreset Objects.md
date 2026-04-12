## SourceEffectChorusPreset Objects

```python
class SourceEffectChorusPreset(SoundEffectSourcePreset)
```

Source Effect Chorus Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectChorus.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SourceEffectChorusSettings):  [Read-Write]

<a id="unreal.SourceEffectChorusPreset.settings"></a>

#### settings

```python
@property
def settings() -> SourceEffectChorusSettings
```

(SourceEffectChorusSettings):  [Read-Only]

<a id="unreal.SourceEffectChorusPreset.set_wet_modulators"></a>

#### set\_wet\_modulators

```python
def set_wet_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_wet_modulators(modulators) -> None
Set Wet Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_wet_modulator"></a>

#### set\_wet\_modulator

```python
def set_wet_modulator(modulator: SoundModulatorBase) -> None
```

x.set_wet_modulator(modulator) -> None
Set Wet Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_wet"></a>

#### set\_wet

```python
def set_wet(wet_amount: float) -> None
```

x.set_wet(wet_amount) -> None
Set Wet

Args:
    wet_amount (float):

<a id="unreal.SourceEffectChorusPreset.set_spread_modulators"></a>

#### set\_spread\_modulators

```python
def set_spread_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_spread_modulators(modulators) -> None
Set Spread Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_spread_modulator"></a>

#### set\_spread\_modulator

```python
def set_spread_modulator(modulator: SoundModulatorBase) -> None
```

x.set_spread_modulator(modulator) -> None
Set Spread Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_spread"></a>

#### set\_spread

```python
def set_spread(spread: float) -> None
```

x.set_spread(spread) -> None
Set Spread

Args:
    spread (float):

<a id="unreal.SourceEffectChorusPreset.set_settings"></a>

#### set\_settings

```python
def set_settings(settings: SourceEffectChorusBaseSettings) -> None
```

x.set_settings(settings) -> None
Sets just base (i.e. carrier) setting values without modifying modulation source references

Args:
    settings (SourceEffectChorusBaseSettings):

<a id="unreal.SourceEffectChorusPreset.set_modulation_settings"></a>

#### set\_modulation\_settings

```python
def set_modulation_settings(
        modulation_settings: SourceEffectChorusSettings) -> None
```

x.set_modulation_settings(modulation_settings) -> None
Set Modulation Settings

Args:
    modulation_settings (SourceEffectChorusSettings):

<a id="unreal.SourceEffectChorusPreset.set_frequency_modulators"></a>

#### set\_frequency\_modulators

```python
def set_frequency_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_frequency_modulators(modulators) -> None
Set Frequency Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_frequency_modulator"></a>

#### set\_frequency\_modulator

```python
def set_frequency_modulator(modulator: SoundModulatorBase) -> None
```

x.set_frequency_modulator(modulator) -> None
Set Frequency Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_frequency"></a>

#### set\_frequency

```python
def set_frequency(frequency: float) -> None
```

x.set_frequency(frequency) -> None
Set Frequency

Args:
    frequency (float):

<a id="unreal.SourceEffectChorusPreset.set_feedback_modulators"></a>

#### set\_feedback\_modulators

```python
def set_feedback_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_feedback_modulators(modulators) -> None
Set Feedback Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_feedback_modulator"></a>

#### set\_feedback\_modulator

```python
def set_feedback_modulator(modulator: SoundModulatorBase) -> None
```

x.set_feedback_modulator(modulator) -> None
Set Feedback Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_feedback"></a>

#### set\_feedback

```python
def set_feedback(feedback: float) -> None
```

x.set_feedback(feedback) -> None
Set Feedback

Args:
    feedback (float):

<a id="unreal.SourceEffectChorusPreset.set_dry_modulators"></a>

#### set\_dry\_modulators

```python
def set_dry_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_dry_modulators(modulators) -> None
Set Dry Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_dry_modulator"></a>

#### set\_dry\_modulator

```python
def set_dry_modulator(modulator: SoundModulatorBase) -> None
```

x.set_dry_modulator(modulator) -> None
Set Dry Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_dry"></a>

#### set\_dry

```python
def set_dry(dry_amount: float) -> None
```

x.set_dry(dry_amount) -> None
Set Dry

Args:
    dry_amount (float):

<a id="unreal.SourceEffectChorusPreset.set_depth_modulators"></a>

#### set\_depth\_modulators

```python
def set_depth_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_depth_modulators(modulators) -> None
Set Depth Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectChorusPreset.set_depth_modulator"></a>

#### set\_depth\_modulator

```python
def set_depth_modulator(modulator: SoundModulatorBase) -> None
```

x.set_depth_modulator(modulator) -> None
Set Depth Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset.set_depth"></a>

#### set\_depth

```python
def set_depth(depth: float) -> None
```

x.set_depth(depth) -> None
Set Depth

Args:
    depth (float):

<a id="unreal.SourceEffectConvolutionReverbPreset"></a>