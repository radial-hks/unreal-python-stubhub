## AIStimulus Objects

```python
class AIStimulus(StructBase)
```

AIStimulus

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``age`` (float):  [Read-Write]
- ``expiration_age`` (float):  [Read-Write]
- ``receiver_location`` (Vector):  [Read-Write]
- ``stimulus_location`` (Vector):  [Read-Write]
- ``strength`` (float):  [Read-Write]
- ``successfully_sensed`` (bool):  [Read-Write]
- ``tag`` (Name):  [Read-Write]

<a id="unreal.AIStimulus.__init__"></a>

#### __init__

```python
def __init__(age: float = 0.000000,
             expiration_age: float = 0.000000,
             strength: float = 0.000000,
             stimulus_location: Vector = [0.000000, 0.000000, 0.000000],
             receiver_location: Vector = [0.000000, 0.000000, 0.000000],
             tag: Name = "None",
             successfully_sensed: bool = False) -> None
```

<a id="unreal.AIStimulus.age"></a>

#### age

```python
@property
def age() -> float
```

(float):  [Read-Write]

<a id="unreal.AIStimulus.age"></a>

#### age

```python
@age.setter
def age(value: float) -> None
```

<a id="unreal.AIStimulus.expiration_age"></a>

#### expiration_age

```python
@property
def expiration_age() -> float
```

(float):  [Read-Write]

<a id="unreal.AIStimulus.expiration_age"></a>

#### expiration_age

```python
@expiration_age.setter
def expiration_age(value: float) -> None
```

<a id="unreal.AIStimulus.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write]

<a id="unreal.AIStimulus.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.AIStimulus.stimulus_location"></a>

#### stimulus_location

```python
@property
def stimulus_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AIStimulus.stimulus_location"></a>

#### stimulus_location

```python
@stimulus_location.setter
def stimulus_location(value: Vector) -> None
```

<a id="unreal.AIStimulus.receiver_location"></a>

#### receiver_location

```python
@property
def receiver_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AIStimulus.receiver_location"></a>

#### receiver_location

```python
@receiver_location.setter
def receiver_location(value: Vector) -> None
```

<a id="unreal.AIStimulus.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AIStimulus.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.AIStimulus.successfully_sensed"></a>

#### successfully_sensed

```python
@property
def successfully_sensed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AIStimulus.successfully_sensed"></a>

#### successfully_sensed

```python
@successfully_sensed.setter
def successfully_sensed(value: bool) -> None
```

<a id="unreal.AIRequestID"></a>