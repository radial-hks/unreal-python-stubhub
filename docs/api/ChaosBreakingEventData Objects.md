## ChaosBreakingEventData Objects

```python
class ChaosBreakingEventData(StructBase)
```

A breaking event data structure.

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosBreakingEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write] Location of the breaking event (centroid)
- ``mass`` (float):  [Read-Write] The mass of the breaking event
- ``velocity`` (Vector):  [Read-Write] The velocity of the breaking event

<a id="unreal.ChaosBreakingEventData.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000) -> None
```

<a id="unreal.ChaosBreakingEventData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] Location of the breaking event (centroid)

<a id="unreal.ChaosBreakingEventData.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only] The velocity of the breaking event

<a id="unreal.ChaosBreakingEventData.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Only] The mass of the breaking event

<a id="unreal.ChaosCollisionEventData"></a>