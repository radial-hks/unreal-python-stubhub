## ChaosTrailingEventData Objects

```python
class ChaosTrailingEventData(StructBase)
```

A trailing event data structure.

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosTrailingEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity`` (Vector):  [Read-Write] The angular velocity of the trail.
- ``location`` (Vector):  [Read-Write] Current trail location.
- ``mass`` (float):  [Read-Write] The mass of the trail.
- ``particle_index`` (int32):  [Read-Write] The particle index of the trail.
- ``velocity`` (Vector):  [Read-Write] The velocity of the trail.

<a id="unreal.ChaosTrailingEventData.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             particle_index: int = 0) -> None
```

<a id="unreal.ChaosTrailingEventData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Current trail location.

<a id="unreal.ChaosTrailingEventData.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.ChaosTrailingEventData.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Write] The velocity of the trail.

<a id="unreal.ChaosTrailingEventData.velocity"></a>

#### velocity

```python
@velocity.setter
def velocity(value: Vector) -> None
```

<a id="unreal.ChaosTrailingEventData.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Write] The angular velocity of the trail.

<a id="unreal.ChaosTrailingEventData.angular_velocity"></a>

#### angular_velocity

```python
@angular_velocity.setter
def angular_velocity(value: Vector) -> None
```

<a id="unreal.ChaosTrailingEventData.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write] The mass of the trail.

<a id="unreal.ChaosTrailingEventData.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.ChaosTrailingEventData.particle_index"></a>

#### particle_index

```python
@property
def particle_index() -> int
```

(int32):  [Read-Write] The particle index of the trail.

<a id="unreal.ChaosTrailingEventData.particle_index"></a>

#### particle_index

```python
@particle_index.setter
def particle_index(value: int) -> None
```

<a id="unreal.BodyInstanceAsyncPhysicsTickHandle"></a>