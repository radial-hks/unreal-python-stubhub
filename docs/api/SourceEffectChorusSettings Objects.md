## SourceEffectChorusSettings Objects

```python
class SourceEffectChorusSettings(StructBase)
```

Source Effect Chorus Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectChorus.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (float):  [Read-Write]
  deprecated: Property 'Depth' is deprecated.
- ``depth_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The depth of the chorus effect
- ``dry_level`` (float):  [Read-Write]
  deprecated: Property 'DryLevel' is deprecated.
- ``dry_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The dry level of the chorus effect
- ``feedback`` (float):  [Read-Write]
  deprecated: Property 'Feedback' is deprecated.
- ``feedback_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The feedback of the chorus effect
- ``frequency`` (float):  [Read-Write]
  deprecated: Property 'Frequency' is deprecated.
- ``frequency_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The frequency of the chorus effect
- ``spread`` (float):  [Read-Write]
  deprecated: Property 'Spread' is deprecated.
- ``spread_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The spread of the effect (larger means greater difference between left and right delay lines)
- ``wet_level`` (float):  [Read-Write]
  deprecated: Property 'WetLevel' is deprecated.
- ``wet_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The wet level of the chorus effect

<a id="unreal.SourceEffectChorusSettings.__init__"></a>

#### __init__

```python
def __init__(
    depth_modulation: SoundModulationDestinationSettings = [1.000000, []],
    frequency_modulation: SoundModulationDestinationSettings = [1.000000, []],
    feedback_modulation: SoundModulationDestinationSettings = [1.000000, []],
    wet_modulation: SoundModulationDestinationSettings = [1.000000, []],
    dry_modulation: SoundModulationDestinationSettings = [1.000000, []],
    spread_modulation: SoundModulationDestinationSettings = [1.000000, []]
) -> None
```

<a id="unreal.SourceEffectChorusSettings.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write]
deprecated: Property 'Depth' is deprecated.

<a id="unreal.SourceEffectChorusSettings.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write]
deprecated: Property 'Frequency' is deprecated.

<a id="unreal.SourceEffectChorusSettings.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.feedback"></a>

#### feedback

```python
@property
def feedback() -> float
```

(float):  [Read-Write]
deprecated: Property 'Feedback' is deprecated.

<a id="unreal.SourceEffectChorusSettings.feedback"></a>

#### feedback

```python
@feedback.setter
def feedback(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write]
deprecated: Property 'WetLevel' is deprecated.

<a id="unreal.SourceEffectChorusSettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.dry_level"></a>

#### dry_level

```python
@property
def dry_level() -> float
```

(float):  [Read-Write]
deprecated: Property 'DryLevel' is deprecated.

<a id="unreal.SourceEffectChorusSettings.dry_level"></a>

#### dry_level

```python
@dry_level.setter
def dry_level(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.spread"></a>

#### spread

```python
@property
def spread() -> float
```

(float):  [Read-Write]
deprecated: Property 'Spread' is deprecated.

<a id="unreal.SourceEffectChorusSettings.spread"></a>

#### spread

```python
@spread.setter
def spread(value: float) -> None
```

<a id="unreal.SourceEffectChorusSettings.depth_modulation"></a>

#### depth_modulation

```python
@property
def depth_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The depth of the chorus effect

<a id="unreal.SourceEffectChorusSettings.depth_modulation"></a>

#### depth_modulation

```python
@depth_modulation.setter
def depth_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusSettings.frequency_modulation"></a>

#### frequency_modulation

```python
@property
def frequency_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The frequency of the chorus effect

<a id="unreal.SourceEffectChorusSettings.frequency_modulation"></a>

#### frequency_modulation

```python
@frequency_modulation.setter
def frequency_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusSettings.feedback_modulation"></a>

#### feedback_modulation

```python
@property
def feedback_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The feedback of the chorus effect

<a id="unreal.SourceEffectChorusSettings.feedback_modulation"></a>

#### feedback_modulation

```python
@feedback_modulation.setter
def feedback_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusSettings.wet_modulation"></a>

#### wet_modulation

```python
@property
def wet_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The wet level of the chorus effect

<a id="unreal.SourceEffectChorusSettings.wet_modulation"></a>

#### wet_modulation

```python
@wet_modulation.setter
def wet_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusSettings.dry_modulation"></a>

#### dry_modulation

```python
@property
def dry_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The dry level of the chorus effect

<a id="unreal.SourceEffectChorusSettings.dry_modulation"></a>

#### dry_modulation

```python
@dry_modulation.setter
def dry_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusSettings.spread_modulation"></a>

#### spread_modulation

```python
@property
def spread_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The spread of the effect (larger means greater difference between left and right delay lines)

<a id="unreal.SourceEffectChorusSettings.spread_modulation"></a>

#### spread_modulation

```python
@spread_modulation.setter
def spread_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectConvolutionReverbSettings"></a>