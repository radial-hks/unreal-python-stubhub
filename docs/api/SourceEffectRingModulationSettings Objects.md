## SourceEffectRingModulationSettings Objects

```python
class SourceEffectRingModulationSettings(StructBase)
```

Source Effect Ring Modulation Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectRingModulation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_bus_modulator`` (AudioBus):  [Read-Write] Audio bus to use to modulate the effect
- ``depth`` (float):  [Read-Write] Ring modulation depth
- ``dry_level`` (float):  [Read-Write] Gain for the dry signal (no ring mod)
- ``frequency`` (float):  [Read-Write] Ring modulation frequency
- ``modulator_type`` (RingModulatorTypeSourceEffect):  [Read-Write] Ring modulation modulator oscillator type
- ``wet_level`` (float):  [Read-Write] Gain for the wet signal (with ring mod)

<a id="unreal.SourceEffectRingModulationSettings.__init__"></a>

#### __init__

```python
def __init__(
        modulator_type:
    RingModulatorTypeSourceEffect = RingModulatorTypeSourceEffect.SINE,
        frequency: float = 0.000000,
        depth: float = 0.000000,
        dry_level: float = 0.000000,
        wet_level: float = 0.000000,
        audio_bus_modulator: AudioBus = None) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.modulator_type"></a>

#### modulator_type

```python
@property
def modulator_type() -> RingModulatorTypeSourceEffect
```

(RingModulatorTypeSourceEffect):  [Read-Write] Ring modulation modulator oscillator type

<a id="unreal.SourceEffectRingModulationSettings.modulator_type"></a>

#### modulator_type

```python
@modulator_type.setter
def modulator_type(value: RingModulatorTypeSourceEffect) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] Ring modulation frequency

<a id="unreal.SourceEffectRingModulationSettings.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write] Ring modulation depth

<a id="unreal.SourceEffectRingModulationSettings.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.dry_level"></a>

#### dry_level

```python
@property
def dry_level() -> float
```

(float):  [Read-Write] Gain for the dry signal (no ring mod)

<a id="unreal.SourceEffectRingModulationSettings.dry_level"></a>

#### dry_level

```python
@dry_level.setter
def dry_level(value: float) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write] Gain for the wet signal (with ring mod)

<a id="unreal.SourceEffectRingModulationSettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SourceEffectRingModulationSettings.audio_bus_modulator"></a>

#### audio_bus_modulator

```python
@property
def audio_bus_modulator() -> AudioBus
```

(AudioBus):  [Read-Write] Audio bus to use to modulate the effect

<a id="unreal.SourceEffectRingModulationSettings.audio_bus_modulator"></a>

#### audio_bus_modulator

```python
@audio_bus_modulator.setter
def audio_bus_modulator(value: AudioBus) -> None
```

<a id="unreal.SourceEffectSimpleDelaySettings"></a>