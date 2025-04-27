## ChaosCollisionEventData Objects

```python
class ChaosCollisionEventData(StructBase)
```

A collision event data structure

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosCollisionEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``impulse`` (Vector):  [Read-Write] The accumulated impulse vector of the collision event
- ``location`` (Vector):  [Read-Write] Location of the collision event
- ``mass1`` (float):  [Read-Write] The mass of object 1 of the collision event
- ``mass2`` (float):  [Read-Write] The mass of object 2 of the collision event
- ``normal`` (Vector):  [Read-Write] Normal of the collision event
- ``velocity1`` (Vector):  [Read-Write] The velocity of object 1 of the collision event
- ``velocity2`` (Vector):  [Read-Write] The velocity of object 2 of the collision event

<a id="unreal.ChaosCollisionEventData.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             normal: Vector = [0.000000, 0.000000, 0.000000],
             velocity1: Vector = [0.000000, 0.000000, 0.000000],
             velocity2: Vector = [0.000000, 0.000000, 0.000000],
             mass1: float = 0.000000,
             mass2: float = 0.000000,
             impulse: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.ChaosCollisionEventData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] Location of the collision event

<a id="unreal.ChaosCollisionEventData.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Only] Normal of the collision event

<a id="unreal.ChaosCollisionEventData.velocity1"></a>

#### velocity1

```python
@property
def velocity1() -> Vector
```

(Vector):  [Read-Only] The velocity of object 1 of the collision event

<a id="unreal.ChaosCollisionEventData.velocity2"></a>

#### velocity2

```python
@property
def velocity2() -> Vector
```

(Vector):  [Read-Only] The velocity of object 2 of the collision event

<a id="unreal.ChaosCollisionEventData.mass1"></a>

#### mass1

```python
@property
def mass1() -> float
```

(float):  [Read-Only] The mass of object 1 of the collision event

<a id="unreal.ChaosCollisionEventData.mass2"></a>

#### mass2

```python
@property
def mass2() -> float
```

(float):  [Read-Only] The mass of object 2 of the collision event

<a id="unreal.ChaosCollisionEventData.impulse"></a>

#### impulse

```python
@property
def impulse() -> Vector
```

(Vector):  [Read-Only] The accumulated impulse vector of the collision event

<a id="unreal.ChaosRemovalEventData"></a>