## AIDamageEvent Objects

```python
class AIDamageEvent(StructBase)
```

AIDamage Event

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Damage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amount`` (float):  [Read-Write] Damage taken by DamagedActor.
  Note: 0-damage events do not get ignored
- ``damaged_actor`` (Actor):  [Read-Write] Damaged actor
- ``hit_location`` (Vector):  [Read-Write] Event's additional spatial information
  TODO: document
- ``instigator`` (Actor):  [Read-Write] Actor that instigated damage. Can be None
- ``location`` (Vector):  [Read-Write] Event's "Location", or what will be later treated as the perceived location for this sense.
      If not set, HitLocation will be used, if that is unset too DamagedActor's location
- ``tag`` (Name):  [Read-Write] Optional named identifier for the damage.

<a id="unreal.AIDamageEvent.__init__"></a>

#### __init__

```python
def __init__(amount: float = 0.000000,
             location: Vector = [0.000000, 0.000000, 0.000000],
             hit_location: Vector = [0.000000, 0.000000, 0.000000],
             damaged_actor: Actor = None,
             instigator: Actor = None,
             tag: Name = "None") -> None
```

<a id="unreal.AIDamageEvent.amount"></a>

#### amount

```python
@property
def amount() -> float
```

(float):  [Read-Write] Damage taken by DamagedActor.
Note: 0-damage events do not get ignored

<a id="unreal.AIDamageEvent.amount"></a>

#### amount

```python
@amount.setter
def amount(value: float) -> None
```

<a id="unreal.AIDamageEvent.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Event's "Location", or what will be later treated as the perceived location for this sense.
    If not set, HitLocation will be used, if that is unset too DamagedActor's location

<a id="unreal.AIDamageEvent.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.AIDamageEvent.hit_location"></a>

#### hit_location

```python
@property
def hit_location() -> Vector
```

(Vector):  [Read-Write] Event's additional spatial information
TODO: document

<a id="unreal.AIDamageEvent.hit_location"></a>

#### hit_location

```python
@hit_location.setter
def hit_location(value: Vector) -> None
```

<a id="unreal.AIDamageEvent.damaged_actor"></a>

#### damaged_actor

```python
@property
def damaged_actor() -> Actor
```

(Actor):  [Read-Write] Damaged actor

<a id="unreal.AIDamageEvent.damaged_actor"></a>

#### damaged_actor

```python
@damaged_actor.setter
def damaged_actor(value: Actor) -> None
```

<a id="unreal.AIDamageEvent.instigator"></a>

#### instigator

```python
@property
def instigator() -> Actor
```

(Actor):  [Read-Write] Actor that instigated damage. Can be None

<a id="unreal.AIDamageEvent.instigator"></a>

#### instigator

```python
@instigator.setter
def instigator(value: Actor) -> None
```

<a id="unreal.AIDamageEvent.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write] Optional named identifier for the damage.

<a id="unreal.AIDamageEvent.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.AINoiseEvent"></a>