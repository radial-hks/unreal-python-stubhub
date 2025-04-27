## WaveOscillator Objects

```python
class WaveOscillator(StructBase)
```

A wave oscillator for a single number.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: WaveOscillatorCameraShakePattern.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude`` (float):  [Read-Write] Amplitude of the sinusoidal oscillation.
- ``frequency`` (float):  [Read-Write] Frequency of the sinusoidal oscillation.
- ``initial_offset_type`` (InitialWaveOscillatorOffsetType):  [Read-Write] Defines how to begin the oscillation.

<a id="unreal.WaveOscillator.__init__"></a>

#### __init__

```python
def __init__(
    amplitude: float = 0.000000,
    frequency: float = 0.000000,
    initial_offset_type:
    InitialWaveOscillatorOffsetType = InitialWaveOscillatorOffsetType.RANDOM
) -> None
```

<a id="unreal.WaveOscillator.amplitude"></a>

#### amplitude

```python
@property
def amplitude() -> float
```

(float):  [Read-Write] Amplitude of the sinusoidal oscillation.

<a id="unreal.WaveOscillator.amplitude"></a>

#### amplitude

```python
@amplitude.setter
def amplitude(value: float) -> None
```

<a id="unreal.WaveOscillator.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] Frequency of the sinusoidal oscillation.

<a id="unreal.WaveOscillator.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.WaveOscillator.initial_offset_type"></a>

#### initial_offset_type

```python
@property
def initial_offset_type() -> InitialWaveOscillatorOffsetType
```

(InitialWaveOscillatorOffsetType):  [Read-Write] Defines how to begin the oscillation.

<a id="unreal.WaveOscillator.initial_offset_type"></a>

#### initial_offset_type

```python
@initial_offset_type.setter
def initial_offset_type(value: InitialWaveOscillatorOffsetType) -> None
```

<a id="unreal.CameraRigAssetReference"></a>