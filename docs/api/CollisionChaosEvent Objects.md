## CollisionChaosEvent Objects

```python
class CollisionChaosEvent(StructBase)
```

Collision Chaos Event

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulated_impulse`` (Vector):  [Read-Write]
- ``body1`` (CollisionChaosEventBodyInfo):  [Read-Write]
- ``body2`` (CollisionChaosEventBodyInfo):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``normal`` (Vector):  [Read-Write]
- ``penetration_depth`` (float):  [Read-Write]

<a id="unreal.CollisionChaosEvent.__init__"></a>

#### __init__

```python
def __init__(
    location: Vector = [0.000000, 0.000000, 0.000000],
    accumulated_impulse: Vector = [0.000000, 0.000000, 0.000000],
    normal: Vector = [0.000000, 0.000000, 0.000000],
    penetration_depth: float = 0.000000,
    body1: CollisionChaosEventBodyInfo = [[0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          0.000000, None, None, 0, "None"],
    body2: CollisionChaosEventBodyInfo = [[0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          0.000000, None, None, 0, "None"]
) -> None
```

<a id="unreal.CollisionChaosEvent.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEvent.accumulated_impulse"></a>

#### accumulated_impulse

```python
@property
def accumulated_impulse() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEvent.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEvent.penetration_depth"></a>

#### penetration_depth

```python
@property
def penetration_depth() -> float
```

(float):  [Read-Only]

<a id="unreal.CollisionChaosEvent.body1"></a>

#### body1

```python
@property
def body1() -> CollisionChaosEventBodyInfo
```

(CollisionChaosEventBodyInfo):  [Read-Only]

<a id="unreal.CollisionChaosEvent.body2"></a>

#### body2

```python
@property
def body2() -> CollisionChaosEventBodyInfo
```

(CollisionChaosEventBodyInfo):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo"></a>