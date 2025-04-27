## ChaosCrumblingEvent Objects

```python
class ChaosCrumblingEvent(StructBase)
```

Chaos Crumbling Event

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity`` (Vector):  [Read-Write] Angular Velocity of the crumbling cluster
- ``children`` (Array[int32]):  [Read-Write] List of children indices released (optional : see geometry collection component bCrumblingEventIncludesChildren)
- ``component`` (PrimitiveComponent):  [Read-Write] primitive component involved in the crumble event
- ``linear_velocity`` (Vector):  [Read-Write] Linear Velocity of the crumbling cluster
- ``local_bounds`` (Box):  [Read-Write] Local bounding box of the crumbling cluster
- ``location`` (Vector):  [Read-Write] World location of the crumbling cluster
- ``mass`` (float):  [Read-Write] Mass of the crumbling cluster
- ``orientation`` (Quat):  [Read-Write] World orientation of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.__init__"></a>

#### __init__

```python
def __init__(component: PrimitiveComponent = None,
             location: Vector = [0.000000, 0.000000, 0.000000],
             orientation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             linear_velocity: Vector = [0.000000, 0.000000, 0.000000],
             angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             local_bounds: Box = [[0.000000, 0.000000, 0.000000],
                                  [0.000000, 0.000000, 0.000000], False],
             children: Array[int] = []) -> None
```

<a id="unreal.ChaosCrumblingEvent.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only] primitive component involved in the crumble event

<a id="unreal.ChaosCrumblingEvent.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only] World location of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.orientation"></a>

#### orientation

```python
@property
def orientation() -> Quat
```

(Quat):  [Read-Only] World orientation of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.linear_velocity"></a>

#### linear_velocity

```python
@property
def linear_velocity() -> Vector
```

(Vector):  [Read-Only] Linear Velocity of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Only] Angular Velocity of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Only] Mass of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.local_bounds"></a>

#### local_bounds

```python
@property
def local_bounds() -> Box
```

(Box):  [Read-Only] Local bounding box of the crumbling cluster

<a id="unreal.ChaosCrumblingEvent.children"></a>

#### children

```python
@property
def children() -> Array[int]
```

(Array[int32]):  [Read-Only] List of children indices released (optional : see geometry collection component bCrumblingEventIncludesChildren)

<a id="unreal.Key"></a>