## AINoiseEvent Objects

```python
class AINoiseEvent(StructBase)
```

AINoise Event

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Hearing.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instigator`` (Actor):  [Read-Write] Actor triggering the sound.
- ``loudness`` (float):  [Read-Write] Loudness modifier of the sound.
  If MaxRange is non-zero, this modifies the range (by multiplication).
  If there is no MaxRange, then if Square(DistanceToSound) <= Square(HearingRange * Loudness), the sound is heard, false otherwise.
- ``max_range`` (float):  [Read-Write] Max range at which the sound can be heard. Multiplied by Loudness.
  A value of 0 indicates that there is no range limit, though listeners are still limited by their own hearing range.
- ``noise_location`` (Vector):  [Read-Write] if not set Instigator's location will be used
- ``tag`` (Name):  [Read-Write] Named identifier for the noise.

<a id="unreal.AINoiseEvent.__init__"></a>

#### __init__

```python
def __init__(noise_location: Vector = [0.000000, 0.000000, 0.000000],
             loudness: float = 0.000000,
             max_range: float = 0.000000,
             instigator: Actor = None,
             tag: Name = "None") -> None
```

<a id="unreal.AINoiseEvent.noise_location"></a>

#### noise_location

```python
@property
def noise_location() -> Vector
```

(Vector):  [Read-Write] if not set Instigator's location will be used

<a id="unreal.AINoiseEvent.noise_location"></a>

#### noise_location

```python
@noise_location.setter
def noise_location(value: Vector) -> None
```

<a id="unreal.AINoiseEvent.loudness"></a>

#### loudness

```python
@property
def loudness() -> float
```

(float):  [Read-Write] Loudness modifier of the sound.
If MaxRange is non-zero, this modifies the range (by multiplication).
If there is no MaxRange, then if Square(DistanceToSound) <= Square(HearingRange * Loudness), the sound is heard, false otherwise.

<a id="unreal.AINoiseEvent.loudness"></a>

#### loudness

```python
@loudness.setter
def loudness(value: float) -> None
```

<a id="unreal.AINoiseEvent.max_range"></a>

#### max_range

```python
@property
def max_range() -> float
```

(float):  [Read-Write] Max range at which the sound can be heard. Multiplied by Loudness.
A value of 0 indicates that there is no range limit, though listeners are still limited by their own hearing range.

<a id="unreal.AINoiseEvent.max_range"></a>

#### max_range

```python
@max_range.setter
def max_range(value: float) -> None
```

<a id="unreal.AINoiseEvent.instigator"></a>

#### instigator

```python
@property
def instigator() -> Actor
```

(Actor):  [Read-Write] Actor triggering the sound.

<a id="unreal.AINoiseEvent.instigator"></a>

#### instigator

```python
@instigator.setter
def instigator(value: Actor) -> None
```

<a id="unreal.AINoiseEvent.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write] Named identifier for the noise.

<a id="unreal.AINoiseEvent.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.StringValuePair"></a>