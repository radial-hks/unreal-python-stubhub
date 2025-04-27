## ROscillator Objects

```python
class ROscillator(StructBase)
```

Defines FRotator oscillation.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: LegacyCameraShake.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pitch`` (FOscillator):  [Read-Write] Pitch oscillation.
- ``roll`` (FOscillator):  [Read-Write] Roll oscillation.
- ``yaw`` (FOscillator):  [Read-Write] Yaw oscillation.

<a id="unreal.ROscillator.__init__"></a>

#### __init__

```python
def __init__(
    pitch: FOscillator = [0.000000, 0.000000, OscillatorWaveform.SINE_WAVE],
    yaw: FOscillator = [0.000000, 0.000000, OscillatorWaveform.SINE_WAVE],
    roll: FOscillator = [0.000000, 0.000000, OscillatorWaveform.SINE_WAVE]
) -> None
```

<a id="unreal.ROscillator.pitch"></a>

#### pitch

```python
@property
def pitch() -> FOscillator
```

(FOscillator):  [Read-Write] Pitch oscillation.

<a id="unreal.ROscillator.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: FOscillator) -> None
```

<a id="unreal.ROscillator.yaw"></a>

#### yaw

```python
@property
def yaw() -> FOscillator
```

(FOscillator):  [Read-Write] Yaw oscillation.

<a id="unreal.ROscillator.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: FOscillator) -> None
```

<a id="unreal.ROscillator.roll"></a>

#### roll

```python
@property
def roll() -> FOscillator
```

(FOscillator):  [Read-Write] Roll oscillation.

<a id="unreal.ROscillator.roll"></a>

#### roll

```python
@roll.setter
def roll(value: FOscillator) -> None
```

<a id="unreal.VOscillator"></a>