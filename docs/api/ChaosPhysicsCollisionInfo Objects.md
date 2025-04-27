## ChaosPhysicsCollisionInfo Objects

```python
class ChaosPhysicsCollisionInfo(StructBase)
```

Chaos Physics Collision Info

**C++ Source:**

- **Module**: ChaosSolverEngine
- **File**: ChaosNotifyHandlerInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulated_impulse`` (Vector):  [Read-Write]
- ``angular_velocity`` (Vector):  [Read-Write]
- ``component`` (PrimitiveComponent):  [Read-Write]
- ``location`` (Vector):  [Read-Write] Location of the impact
- ``mass`` (float):  [Read-Write]
- ``normal`` (Vector):  [Read-Write] Normal at the impact
- ``other_angular_velocity`` (Vector):  [Read-Write]
- ``other_component`` (PrimitiveComponent):  [Read-Write]
- ``other_mass`` (float):  [Read-Write]
- ``other_velocity`` (Vector):  [Read-Write]
- ``velocity`` (Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.__init__"></a>

#### __init__

```python
def __init__(component: PrimitiveComponent = None,
             other_component: PrimitiveComponent = None,
             location: Vector = [0.000000, 0.000000, 0.000000],
             normal: Vector = [0.000000, 0.000000, 0.000000],
             accumulated_impulse: Vector = [0.000000, 0.000000, 0.000000],
             velocity: Vector = [0.000000, 0.000000, 0.000000],
             other_velocity: Vector = [0.000000, 0.000000, 0.000000],
             angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             other_angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             other_mass: float = 0.000000) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.component"></a>

#### component

```python
@component.setter
def component(value: PrimitiveComponent) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.other_component"></a>

#### other_component

```python
@property
def other_component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.other_component"></a>

#### other_component

```python
@other_component.setter
def other_component(value: PrimitiveComponent) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Location of the impact

<a id="unreal.ChaosPhysicsCollisionInfo.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Write] Normal at the impact

<a id="unreal.ChaosPhysicsCollisionInfo.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.accumulated_impulse"></a>

#### accumulated_impulse

```python
@property
def accumulated_impulse() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.accumulated_impulse"></a>

#### accumulated_impulse

```python
@accumulated_impulse.setter
def accumulated_impulse(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.velocity"></a>

#### velocity

```python
@velocity.setter
def velocity(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.other_velocity"></a>

#### other_velocity

```python
@property
def other_velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.other_velocity"></a>

#### other_velocity

```python
@other_velocity.setter
def other_velocity(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.angular_velocity"></a>

#### angular_velocity

```python
@angular_velocity.setter
def angular_velocity(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.other_angular_velocity"></a>

#### other_angular_velocity

```python
@property
def other_angular_velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.other_angular_velocity"></a>

#### other_angular_velocity

```python
@other_angular_velocity.setter
def other_angular_velocity(value: Vector) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.ChaosPhysicsCollisionInfo.other_mass"></a>

#### other_mass

```python
@property
def other_mass() -> float
```

(float):  [Read-Write]

<a id="unreal.ChaosPhysicsCollisionInfo.other_mass"></a>

#### other_mass

```python
@other_mass.setter
def other_mass(value: float) -> None
```

<a id="unreal.ChaosBreakingEventData"></a>