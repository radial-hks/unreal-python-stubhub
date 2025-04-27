## SourceEffectBitCrusherPreset Objects

```python
class SourceEffectBitCrusherPreset(SoundEffectSourcePreset)
```

Source Effect Bit Crusher Preset

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectBitCrusher.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SourceEffectBitCrusherSettings):  [Read-Write]

<a id="unreal.SourceEffectBitCrusherPreset.settings"></a>

#### settings

```python
@property
def settings() -> SourceEffectBitCrusherSettings
```

(SourceEffectBitCrusherSettings):  [Read-Only]

<a id="unreal.SourceEffectBitCrusherPreset.set_settings"></a>

#### set_settings

```python
def set_settings(settings: SourceEffectBitCrusherBaseSettings) -> None
```

x.set_settings(settings) -> None
Sets just base (i.e. carrier) setting values without modifying modulation source references

Args:
    settings (SourceEffectBitCrusherBaseSettings):

<a id="unreal.SourceEffectBitCrusherPreset.set_sample_rate_modulators"></a>

#### set_sample_rate_modulators

```python
def set_sample_rate_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_sample_rate_modulators(modulators) -> None
Set Sample Rate Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectBitCrusherPreset.set_sample_rate_modulator"></a>

#### set_sample_rate_modulator

```python
def set_sample_rate_modulator(modulator: SoundModulatorBase) -> None
```

x.set_sample_rate_modulator(modulator) -> None
Set Sample Rate Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectBitCrusherPreset.set_sample_rate"></a>

#### set_sample_rate

```python
def set_sample_rate(sample_rate: float) -> None
```

x.set_sample_rate(sample_rate) -> None
Set Sample Rate

Args:
    sample_rate (float):

<a id="unreal.SourceEffectBitCrusherPreset.set_modulation_settings"></a>

#### set_modulation_settings

```python
def set_modulation_settings(
        modulation_settings: SourceEffectBitCrusherSettings) -> None
```

x.set_modulation_settings(modulation_settings) -> None
Set Modulation Settings

Args:
    modulation_settings (SourceEffectBitCrusherSettings):

<a id="unreal.SourceEffectBitCrusherPreset.set_bits"></a>

#### set_bits

```python
def set_bits(bits: float) -> None
```

x.set_bits(bits) -> None
Set Bits

Args:
    bits (float):

<a id="unreal.SourceEffectBitCrusherPreset.set_bit_modulators"></a>

#### set_bit_modulators

```python
def set_bit_modulators(modulators: Set[SoundModulatorBase]) -> None
```

x.set_bit_modulators(modulators) -> None
Set Bit Modulators

Args:
    modulators (Set[SoundModulatorBase]):

<a id="unreal.SourceEffectBitCrusherPreset.set_bit_modulator"></a>

#### set_bit_modulator

```python
def set_bit_modulator(modulator: SoundModulatorBase) -> None
```

x.set_bit_modulator(modulator) -> None
Set Bit Modulator

Args:
    modulator (SoundModulatorBase):

<a id="unreal.SourceEffectChorusPreset"></a>