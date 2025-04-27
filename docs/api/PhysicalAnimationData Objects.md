## PhysicalAnimationData Objects

```python
class PhysicalAnimationData(StructBase)
```

Stores info on the type of motor that will be used for a given bone

**C++ Source:**

- **Module**: Engine
- **File**: PhysicalAnimationComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity_strength`` (float):  [Read-Write] The strength used to correct angular velocity error
- ``is_local_simulation`` (bool):  [Read-Write] Whether the drive targets are in world space or local
- ``max_angular_force`` (float):  [Read-Write] The max force used to correct angular errors
- ``max_linear_force`` (float):  [Read-Write] The max force used to correct linear errors
- ``orientation_strength`` (float):  [Read-Write] The strength used to correct orientation error
- ``position_strength`` (float):  [Read-Write] The strength used to correct linear position error. Only used for non-local simulation
- ``velocity_strength`` (float):  [Read-Write] The strength used to correct linear velocity error. Only used for non-local simulation

<a id="unreal.PhysicalAnimationData.__init__"></a>

#### __init__

```python
def __init__(is_local_simulation: bool = False,
             orientation_strength: float = 0.000000,
             angular_velocity_strength: float = 0.000000,
             position_strength: float = 0.000000,
             velocity_strength: float = 0.000000,
             max_linear_force: float = 0.000000,
             max_angular_force: float = 0.000000) -> None
```

<a id="unreal.PhysicalAnimationData.is_local_simulation"></a>

#### is_local_simulation

```python
@property
def is_local_simulation() -> bool
```

(bool):  [Read-Write] Whether the drive targets are in world space or local

<a id="unreal.PhysicalAnimationData.is_local_simulation"></a>

#### is_local_simulation

```python
@is_local_simulation.setter
def is_local_simulation(value: bool) -> None
```

<a id="unreal.PhysicalAnimationData.orientation_strength"></a>

#### orientation_strength

```python
@property
def orientation_strength() -> float
```

(float):  [Read-Write] The strength used to correct orientation error

<a id="unreal.PhysicalAnimationData.orientation_strength"></a>

#### orientation_strength

```python
@orientation_strength.setter
def orientation_strength(value: float) -> None
```

<a id="unreal.PhysicalAnimationData.angular_velocity_strength"></a>

#### angular_velocity_strength

```python
@property
def angular_velocity_strength() -> float
```

(float):  [Read-Write] The strength used to correct angular velocity error

<a id="unreal.PhysicalAnimationData.angular_velocity_strength"></a>

#### angular_velocity_strength

```python
@angular_velocity_strength.setter
def angular_velocity_strength(value: float) -> None
```

<a id="unreal.PhysicalAnimationData.position_strength"></a>

#### position_strength

```python
@property
def position_strength() -> float
```

(float):  [Read-Write] The strength used to correct linear position error. Only used for non-local simulation

<a id="unreal.PhysicalAnimationData.position_strength"></a>

#### position_strength

```python
@position_strength.setter
def position_strength(value: float) -> None
```

<a id="unreal.PhysicalAnimationData.velocity_strength"></a>

#### velocity_strength

```python
@property
def velocity_strength() -> float
```

(float):  [Read-Write] The strength used to correct linear velocity error. Only used for non-local simulation

<a id="unreal.PhysicalAnimationData.velocity_strength"></a>

#### velocity_strength

```python
@velocity_strength.setter
def velocity_strength(value: float) -> None
```

<a id="unreal.PhysicalAnimationData.max_linear_force"></a>

#### max_linear_force

```python
@property
def max_linear_force() -> float
```

(float):  [Read-Write] The max force used to correct linear errors

<a id="unreal.PhysicalAnimationData.max_linear_force"></a>

#### max_linear_force

```python
@max_linear_force.setter
def max_linear_force(value: float) -> None
```

<a id="unreal.PhysicalAnimationData.max_angular_force"></a>

#### max_angular_force

```python
@property
def max_angular_force() -> float
```

(float):  [Read-Write] The max force used to correct angular errors

<a id="unreal.PhysicalAnimationData.max_angular_force"></a>

#### max_angular_force

```python
@max_angular_force.setter
def max_angular_force(value: float) -> None
```

<a id="unreal.SkelMeshSkinWeightInfo"></a>