## SubmixEffectFlexiverbSettings Objects

```python
class SubmixEffectFlexiverbSettings(StructBase)
```

Submix Effect Flexiverb Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectFlexiverb.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``complexity`` (int32):  [Read-Write]
- ``decay_time`` (float):  [Read-Write] Time in seconds it will take for the impulse response to decay to -60 dB.
- ``pre_delay`` (float):  [Read-Write] PreDelay - 0.01 < 10.0 < 40.0 - Amount of delay to the first echo in milliseconds.
- ``room_dampening`` (float):  [Read-Write] Room Dampening - 0.0 < 0.85 < 1.0 - Frequency at which the room dampens.

<a id="unreal.SubmixEffectFlexiverbSettings.__init__"></a>

#### __init__

```python
def __init__(pre_delay: float = 0.000000,
             decay_time: float = 0.000000,
             room_dampening: float = 0.000000,
             complexity: int = 0) -> None
```

<a id="unreal.SubmixEffectFlexiverbSettings.pre_delay"></a>

#### pre_delay

```python
@property
def pre_delay() -> float
```

(float):  [Read-Write] PreDelay - 0.01 < 10.0 < 40.0 - Amount of delay to the first echo in milliseconds.

<a id="unreal.SubmixEffectFlexiverbSettings.pre_delay"></a>

#### pre_delay

```python
@pre_delay.setter
def pre_delay(value: float) -> None
```

<a id="unreal.SubmixEffectFlexiverbSettings.decay_time"></a>

#### decay_time

```python
@property
def decay_time() -> float
```

(float):  [Read-Write] Time in seconds it will take for the impulse response to decay to -60 dB.

<a id="unreal.SubmixEffectFlexiverbSettings.decay_time"></a>

#### decay_time

```python
@decay_time.setter
def decay_time(value: float) -> None
```

<a id="unreal.SubmixEffectFlexiverbSettings.room_dampening"></a>

#### room_dampening

```python
@property
def room_dampening() -> float
```

(float):  [Read-Write] Room Dampening - 0.0 < 0.85 < 1.0 - Frequency at which the room dampens.

<a id="unreal.SubmixEffectFlexiverbSettings.room_dampening"></a>

#### room_dampening

```python
@room_dampening.setter
def room_dampening(value: float) -> None
```

<a id="unreal.SubmixEffectFlexiverbSettings.complexity"></a>

#### complexity

```python
@property
def complexity() -> int
```

(int32):  [Read-Write]

<a id="unreal.SubmixEffectFlexiverbSettings.complexity"></a>

#### complexity

```python
@complexity.setter
def complexity(value: int) -> None
```

<a id="unreal.DynamicsBandSettings"></a>