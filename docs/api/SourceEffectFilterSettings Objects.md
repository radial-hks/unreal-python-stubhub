## SourceEffectFilterSettings Objects

```python
class SourceEffectFilterSettings(StructBase)
```

Source Effect Filter Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_bus_modulation`` (Array[SourceEffectFilterAudioBusModulationSettings]):  [Read-Write] Audio bus settings to use to modulate the filter frequency cutoff (auto-wah) with arbitrary audio from an audio bus
- ``cutoff_frequency`` (float):  [Read-Write] The filter cutoff frequency
- ``filter_circuit`` (SourceEffectFilterCircuit):  [Read-Write] The type of filter circuit to use.
- ``filter_q`` (float):  [Read-Write] The filter resonance.
- ``filter_type`` (SourceEffectFilterType):  [Read-Write] The type of filter to use.

<a id="unreal.SourceEffectFilterSettings.__init__"></a>

#### __init__

```python
def __init__(
    filter_circuit: SourceEffectFilterCircuit = SourceEffectFilterCircuit.
    ONE_POLE,
    filter_type: SourceEffectFilterType = SourceEffectFilterType.LOW_PASS,
    cutoff_frequency: float = 0.000000,
    filter_q: float = 0.000000,
    audio_bus_modulation: Array[
        SourceEffectFilterAudioBusModulationSettings] = []
) -> None
```

<a id="unreal.SourceEffectFilterSettings.filter_circuit"></a>

#### filter_circuit

```python
@property
def filter_circuit() -> SourceEffectFilterCircuit
```

(SourceEffectFilterCircuit):  [Read-Write] The type of filter circuit to use.

<a id="unreal.SourceEffectFilterSettings.filter_circuit"></a>

#### filter_circuit

```python
@filter_circuit.setter
def filter_circuit(value: SourceEffectFilterCircuit) -> None
```

<a id="unreal.SourceEffectFilterSettings.filter_type"></a>

#### filter_type

```python
@property
def filter_type() -> SourceEffectFilterType
```

(SourceEffectFilterType):  [Read-Write] The type of filter to use.

<a id="unreal.SourceEffectFilterSettings.filter_type"></a>

#### filter_type

```python
@filter_type.setter
def filter_type(value: SourceEffectFilterType) -> None
```

<a id="unreal.SourceEffectFilterSettings.cutoff_frequency"></a>

#### cutoff_frequency

```python
@property
def cutoff_frequency() -> float
```

(float):  [Read-Write] The filter cutoff frequency

<a id="unreal.SourceEffectFilterSettings.cutoff_frequency"></a>

#### cutoff_frequency

```python
@cutoff_frequency.setter
def cutoff_frequency(value: float) -> None
```

<a id="unreal.SourceEffectFilterSettings.filter_q"></a>

#### filter_q

```python
@property
def filter_q() -> float
```

(float):  [Read-Write] The filter resonance.

<a id="unreal.SourceEffectFilterSettings.filter_q"></a>

#### filter_q

```python
@filter_q.setter
def filter_q(value: float) -> None
```

<a id="unreal.SourceEffectFilterSettings.audio_bus_modulation"></a>

#### audio_bus_modulation

```python
@property
def audio_bus_modulation(
) -> Array[SourceEffectFilterAudioBusModulationSettings]
```

(Array[SourceEffectFilterAudioBusModulationSettings]):  [Read-Write] Audio bus settings to use to modulate the filter frequency cutoff (auto-wah) with arbitrary audio from an audio bus

<a id="unreal.SourceEffectFilterSettings.audio_bus_modulation"></a>

#### audio_bus_modulation

```python
@audio_bus_modulation.setter
def audio_bus_modulation(
        value: Array[SourceEffectFilterAudioBusModulationSettings]) -> None
```

<a id="unreal.SourceEffectFoldbackDistortionSettings"></a>