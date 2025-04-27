## ChaosBreakEvent Objects

```python
class ChaosBreakEvent(StructBase)
```

Chaos Break Event

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity`` (Vector):  [Read-Write] Angular Velocity of the breaking particle
- ``component`` (PrimitiveComponent):  [Read-Write] primitive component involved in the break event
- ``extents`` (Vector):  [Read-Write] Extents of the bounding box
- ``from_crumble`` (bool):  [Read-Write] Whether the break event originated from a crumble event
- ``index`` (int32):  [Read-Write] Index of the geometry collection bone if positive
- ``location`` (Vector):  [Read-Write] World location of the break
- ``mass`` (float):  [Read-Write] Mass of the breaking particle
- ``velocity`` (Vector):  [Read-Write] Linear Velocity of the breaking particle

<a id="unreal.ChaosBreakEvent.__init__"></a>

#### __init__

```python
def __init__(component: PrimitiveComponent = None,
             location: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             extents: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             index: int = 0,
             from_crumble: bool = False) -> None
```

<a id="unreal.ChaosBreakEvent.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only] primitive component involved in the break event

<a id="unreal.ChaosBreakEvent.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] World location of the break

<a id="unreal.ChaosBreakEvent.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only] Linear Velocity of the breaking particle

<a id="unreal.ChaosBreakEvent.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Only] Angular Velocity of the breaking particle

<a id="unreal.ChaosBreakEvent.extents"></a>

#### extents

```python
@property
def extents() -> Vector
```

(Vector):  [Read-Only] Extents of the bounding box

<a id="unreal.ChaosBreakEvent.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Only] Mass of the breaking particle

<a id="unreal.ChaosBreakEvent.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only] Index of the geometry collection bone if positive

<a id="unreal.ChaosBreakEvent.from_crumble"></a>

#### from_crumble

```python
@property
def from_crumble() -> bool
```

(bool):  [Read-Only] Whether the break event originated from a crumble event

<a id="unreal.CollisionChaosEvent"></a>