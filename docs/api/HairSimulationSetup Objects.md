## HairSimulationSetup Objects

```python
class HairSimulationSetup(StructBase)
```

Hair Simulation Setup

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_velocity_scale`` (float):  [Read-Write] The amount of angular velocities sent to the local groom space from the reference bone
- ``debug_simulation`` (bool):  [Read-Write] Boolean to make the simulation strands visible
- ``linear_velocity_scale`` (float):  [Read-Write] The amount of linear velocities sent to the local groom space from the reference bone
- ``local_bone`` (str):  [Read-Write] Bone used for the simulation local space
- ``local_simulation`` (bool):  [Read-Write] Strands simulation is done in local space
- ``reset_simulation`` (bool):  [Read-Write] Boolean to control if we want to reset trhe simulation at some point in time
- ``teleport_distance`` (float):  [Read-Write] Teleport distance threshold to reset the simulation

<a id="unreal.HairSimulationSetup.__init__"></a>

#### __init__

```python
def __init__(reset_simulation: bool = False,
             debug_simulation: bool = False,
             local_simulation: bool = False,
             linear_velocity_scale: float = 0.000000,
             angular_velocity_scale: float = 0.000000,
             local_bone: str = "",
             teleport_distance: float = 0.000000) -> None
```

<a id="unreal.HairSimulationSetup.reset_simulation"></a>

#### reset_simulation

```python
@property
def reset_simulation() -> bool
```

(bool):  [Read-Write] Boolean to control if we want to reset trhe simulation at some point in time

<a id="unreal.HairSimulationSetup.reset_simulation"></a>

#### reset_simulation

```python
@reset_simulation.setter
def reset_simulation(value: bool) -> None
```

<a id="unreal.HairSimulationSetup.debug_simulation"></a>

#### debug_simulation

```python
@property
def debug_simulation() -> bool
```

(bool):  [Read-Write] Boolean to make the simulation strands visible

<a id="unreal.HairSimulationSetup.debug_simulation"></a>

#### debug_simulation

```python
@debug_simulation.setter
def debug_simulation(value: bool) -> None
```

<a id="unreal.HairSimulationSetup.local_simulation"></a>

#### local_simulation

```python
@property
def local_simulation() -> bool
```

(bool):  [Read-Write] Strands simulation is done in local space

<a id="unreal.HairSimulationSetup.local_simulation"></a>

#### local_simulation

```python
@local_simulation.setter
def local_simulation(value: bool) -> None
```

<a id="unreal.HairSimulationSetup.linear_velocity_scale"></a>

#### linear_velocity_scale

```python
@property
def linear_velocity_scale() -> float
```

(float):  [Read-Write] The amount of linear velocities sent to the local groom space from the reference bone

<a id="unreal.HairSimulationSetup.linear_velocity_scale"></a>

#### linear_velocity_scale

```python
@linear_velocity_scale.setter
def linear_velocity_scale(value: float) -> None
```

<a id="unreal.HairSimulationSetup.angular_velocity_scale"></a>

#### angular_velocity_scale

```python
@property
def angular_velocity_scale() -> float
```

(float):  [Read-Write] The amount of angular velocities sent to the local groom space from the reference bone

<a id="unreal.HairSimulationSetup.angular_velocity_scale"></a>

#### angular_velocity_scale

```python
@angular_velocity_scale.setter
def angular_velocity_scale(value: float) -> None
```

<a id="unreal.HairSimulationSetup.local_bone"></a>

#### local_bone

```python
@property
def local_bone() -> str
```

(str):  [Read-Write] Bone used for the simulation local space

<a id="unreal.HairSimulationSetup.local_bone"></a>

#### local_bone

```python
@local_bone.setter
def local_bone(value: str) -> None
```

<a id="unreal.HairSimulationSetup.teleport_distance"></a>

#### teleport_distance

```python
@property
def teleport_distance() -> float
```

(float):  [Read-Write] Teleport distance threshold to reset the simulation

<a id="unreal.HairSimulationSetup.teleport_distance"></a>

#### teleport_distance

```python
@teleport_distance.setter
def teleport_distance(value: float) -> None
```

<a id="unreal.HairSimulationSettings"></a>