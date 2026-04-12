## SourceEffectIndividualFilterSettings Objects

```python
class SourceEffectIndividualFilterSettings(StructBase)
```

Source Effect Individual Filter Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMotionFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cutoff_frequency`` (float):  [Read-Write] The filter cutoff frequency
- ``filter_circuit`` (SourceEffectMotionFilterCircuit):  [Read-Write] The type of filter circuit to use.
- ``filter_q`` (float):  [Read-Write] The filter resonance.
- ``filter_type`` (SourceEffectMotionFilterType):  [Read-Write] The type of filter to use.

<a id="unreal.SourceEffectIndividualFilterSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        filter_circuit:
    SourceEffectMotionFilterCircuit = SourceEffectMotionFilterCircuit.ONE_POLE,
        filter_type: SourceEffectMotionFilterType = SourceEffectMotionFilterType
    .LOW_PASS,
        cutoff_frequency: float = 0.000000,
        filter_q: float = 0.000000) -> None
```

<a id="unreal.SourceEffectIndividualFilterSettings.filter_circuit"></a>

#### filter\_circuit

```python
@property
def filter_circuit() -> SourceEffectMotionFilterCircuit
```

(SourceEffectMotionFilterCircuit):  [Read-Write] The type of filter circuit to use.

<a id="unreal.SourceEffectIndividualFilterSettings.filter_circuit"></a>

#### filter\_circuit

```python
@filter_circuit.setter
def filter_circuit(value: SourceEffectMotionFilterCircuit) -> None
```

<a id="unreal.SourceEffectIndividualFilterSettings.filter_type"></a>

#### filter\_type

```python
@property
def filter_type() -> SourceEffectMotionFilterType
```

(SourceEffectMotionFilterType):  [Read-Write] The type of filter to use.

<a id="unreal.SourceEffectIndividualFilterSettings.filter_type"></a>

#### filter\_type

```python
@filter_type.setter
def filter_type(value: SourceEffectMotionFilterType) -> None
```

<a id="unreal.SourceEffectIndividualFilterSettings.cutoff_frequency"></a>

#### cutoff\_frequency

```python
@property
def cutoff_frequency() -> float
```

(float):  [Read-Write] The filter cutoff frequency

<a id="unreal.SourceEffectIndividualFilterSettings.cutoff_frequency"></a>

#### cutoff\_frequency

```python
@cutoff_frequency.setter
def cutoff_frequency(value: float) -> None
```

<a id="unreal.SourceEffectIndividualFilterSettings.filter_q"></a>

#### filter\_q

```python
@property
def filter_q() -> float
```

(float):  [Read-Write] The filter resonance.

<a id="unreal.SourceEffectIndividualFilterSettings.filter_q"></a>

#### filter\_q

```python
@filter_q.setter
def filter_q(value: float) -> None
```

<a id="unreal.SourceEffectMotionFilterModulationSettings"></a>