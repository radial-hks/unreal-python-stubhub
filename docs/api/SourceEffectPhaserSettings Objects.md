## SourceEffectPhaserSettings Objects

```python
class SourceEffectPhaserSettings(StructBase)
```

Source Effect Phaser Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectPhaser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``feedback`` (float):  [Read-Write] The feedback of the phaser effect
- ``frequency`` (float):  [Read-Write] The LFO frequency of the phaser effect
- ``lfo_type`` (PhaserLFOType):  [Read-Write] The phaser LFO type
- ``use_quadrature_phase`` (bool):  [Read-Write] Whether or not to use quadtrature phase for the LFO modulation
- ``wet_level`` (float):  [Read-Write] The wet level of the phaser effect

<a id="unreal.SourceEffectPhaserSettings.__init__"></a>

#### __init__

```python
def __init__(wet_level: float = 0.000000,
             frequency: float = 0.000000,
             feedback: float = 0.000000,
             lfo_type: PhaserLFOType = PhaserLFOType.SINE,
             use_quadrature_phase: bool = False) -> None
```

<a id="unreal.SourceEffectPhaserSettings.wet_level"></a>

#### wet_level

```python
@property
def wet_level() -> float
```

(float):  [Read-Write] The wet level of the phaser effect

<a id="unreal.SourceEffectPhaserSettings.wet_level"></a>

#### wet_level

```python
@wet_level.setter
def wet_level(value: float) -> None
```

<a id="unreal.SourceEffectPhaserSettings.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] The LFO frequency of the phaser effect

<a id="unreal.SourceEffectPhaserSettings.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.SourceEffectPhaserSettings.feedback"></a>

#### feedback

```python
@property
def feedback() -> float
```

(float):  [Read-Write] The feedback of the phaser effect

<a id="unreal.SourceEffectPhaserSettings.feedback"></a>

#### feedback

```python
@feedback.setter
def feedback(value: float) -> None
```

<a id="unreal.SourceEffectPhaserSettings.lfo_type"></a>

#### lfo_type

```python
@property
def lfo_type() -> PhaserLFOType
```

(PhaserLFOType):  [Read-Write] The phaser LFO type

<a id="unreal.SourceEffectPhaserSettings.lfo_type"></a>

#### lfo_type

```python
@lfo_type.setter
def lfo_type(value: PhaserLFOType) -> None
```

<a id="unreal.SourceEffectPhaserSettings.use_quadrature_phase"></a>

#### use_quadrature_phase

```python
@property
def use_quadrature_phase() -> bool
```

(bool):  [Read-Write] Whether or not to use quadtrature phase for the LFO modulation

<a id="unreal.SourceEffectPhaserSettings.use_quadrature_phase"></a>

#### use_quadrature_phase

```python
@use_quadrature_phase.setter
def use_quadrature_phase(value: bool) -> None
```

<a id="unreal.SourceEffectRingModulationSettings"></a>