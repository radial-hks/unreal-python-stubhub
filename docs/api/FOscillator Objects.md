## FOscillator Objects

```python
class FOscillator(StructBase)
```

Defines oscillation of a single number.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: LegacyCameraShake.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude`` (float):  [Read-Write] Amplitude of the sinusoidal oscillation.
- ``frequency`` (float):  [Read-Write] Frequency of the sinusoidal oscillation.
- ``initial_offset`` (InitialOscillatorOffset):  [Read-Write] Defines how to begin (either at zero, or at a randomized value.
- ``waveform`` (OscillatorWaveform):  [Read-Write] Type of waveform to use for oscillation.

<a id="unreal.FOscillator.__init__"></a>

#### __init__

```python
def __init__(
        amplitude: float = 0.000000,
        frequency: float = 0.000000,
        waveform: OscillatorWaveform = OscillatorWaveform.SINE_WAVE) -> None
```

<a id="unreal.FOscillator.amplitude"></a>

#### amplitude

```python
@property
def amplitude() -> float
```

(float):  [Read-Write] Amplitude of the sinusoidal oscillation.

<a id="unreal.FOscillator.amplitude"></a>

#### amplitude

```python
@amplitude.setter
def amplitude(value: float) -> None
```

<a id="unreal.FOscillator.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] Frequency of the sinusoidal oscillation.

<a id="unreal.FOscillator.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.FOscillator.waveform"></a>

#### waveform

```python
@property
def waveform() -> OscillatorWaveform
```

(OscillatorWaveform):  [Read-Write] Type of waveform to use for oscillation.

<a id="unreal.FOscillator.waveform"></a>

#### waveform

```python
@waveform.setter
def waveform(value: OscillatorWaveform) -> None
```

<a id="unreal.ROscillator"></a>