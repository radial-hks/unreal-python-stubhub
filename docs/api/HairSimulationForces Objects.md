## HairSimulationForces Objects

```python
class HairSimulationForces(StructBase)
```

Hair Simulation Forces

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air_drag`` (float):  [Read-Write] Coefficient between 0 and 1 to be used for the air drag
- ``air_velocity`` (Vector):  [Read-Write] Velocity of the surrounding air in cm/s
- ``gravity_vector`` (Vector):  [Read-Write] Acceleration vector in cm/s2 to be used for the gravity

<a id="unreal.HairSimulationForces.__init__"></a>

#### __init__

```python
def __init__(gravity_vector: Vector = [0.000000, 0.000000, 0.000000],
             air_drag: float = 0.000000,
             air_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.HairSimulationForces.gravity_vector"></a>

#### gravity_vector

```python
@property
def gravity_vector() -> Vector
```

(Vector):  [Read-Write] Acceleration vector in cm/s2 to be used for the gravity

<a id="unreal.HairSimulationForces.gravity_vector"></a>

#### gravity_vector

```python
@gravity_vector.setter
def gravity_vector(value: Vector) -> None
```

<a id="unreal.HairSimulationForces.air_drag"></a>

#### air_drag

```python
@property
def air_drag() -> float
```

(float):  [Read-Write] Coefficient between 0 and 1 to be used for the air drag

<a id="unreal.HairSimulationForces.air_drag"></a>

#### air_drag

```python
@air_drag.setter
def air_drag(value: float) -> None
```

<a id="unreal.HairSimulationForces.air_velocity"></a>

#### air_velocity

```python
@property
def air_velocity() -> Vector
```

(Vector):  [Read-Write] Velocity of the surrounding air in cm/s

<a id="unreal.HairSimulationForces.air_velocity"></a>

#### air_velocity

```python
@air_velocity.setter
def air_velocity(value: Vector) -> None
```

<a id="unreal.HairSimulationConstraints"></a>