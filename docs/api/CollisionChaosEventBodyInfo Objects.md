## CollisionChaosEventBodyInfo Objects

```python
class CollisionChaosEventBodyInfo(StructBase)
```

Collision Chaos Event Body Info

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity`` (Vector):  [Read-Write]
- ``body_index`` (int32):  [Read-Write]
- ``bone_name`` (Name):  [Read-Write]
- ``component`` (PrimitiveComponent):  [Read-Write]
- ``delta_velocity`` (Vector):  [Read-Write]
- ``mass`` (float):  [Read-Write]
- ``phys_material`` (PhysicalMaterial):  [Read-Write]
- ``velocity`` (Vector):  [Read-Write]

<a id="unreal.CollisionChaosEventBodyInfo.__init__"></a>

#### __init__

```python
def __init__(velocity: Vector = [0.000000, 0.000000, 0.000000],
             delta_velocity: Vector = [0.000000, 0.000000, 0.000000],
             angular_velocity: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             phys_material: PhysicalMaterial = None,
             component: PrimitiveComponent = None,
             body_index: int = 0,
             bone_name: Name = "None") -> None
```

<a id="unreal.CollisionChaosEventBodyInfo.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.delta_velocity"></a>

#### delta_velocity

```python
@property
def delta_velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.angular_velocity"></a>

#### angular_velocity

```python
@property
def angular_velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.phys_material"></a>

#### phys_material

```python
@property
def phys_material() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.body_index"></a>

#### body_index

```python
@property
def body_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.CollisionChaosEventBodyInfo.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.ChaosCrumblingEvent"></a>