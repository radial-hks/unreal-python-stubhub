## SourceEffectBitCrusherSettings Objects

```python
class SourceEffectBitCrusherSettings(StructBase)
```

Source Effect Bit Crusher Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectBitCrusher.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bit_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The reduced bit depth to use for the audio stream
- ``sample_rate_modulation`` (SoundModulationDestinationSettings):  [Read-Write] The reduced frequency to use for the audio stream.

<a id="unreal.SourceEffectBitCrusherSettings.__init__"></a>

#### __init__

```python
def __init__(
    sample_rate_modulation: SoundModulationDestinationSettings = [
        1.000000, []
    ],
    bit_modulation: SoundModulationDestinationSettings = [1.000000,
                                                          []]) -> None
```

<a id="unreal.SourceEffectBitCrusherSettings.sample_rate_modulation"></a>

#### sample_rate_modulation

```python
@property
def sample_rate_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The reduced frequency to use for the audio stream.

<a id="unreal.SourceEffectBitCrusherSettings.sample_rate_modulation"></a>

#### sample_rate_modulation

```python
@sample_rate_modulation.setter
def sample_rate_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectBitCrusherSettings.bit_modulation"></a>

#### bit_modulation

```python
@property
def bit_modulation() -> SoundModulationDestinationSettings
```

(SoundModulationDestinationSettings):  [Read-Write] The reduced bit depth to use for the audio stream

<a id="unreal.SourceEffectBitCrusherSettings.bit_modulation"></a>

#### bit_modulation

```python
@bit_modulation.setter
def bit_modulation(value: SoundModulationDestinationSettings) -> None
```

<a id="unreal.SourceEffectChorusBaseSettings"></a>