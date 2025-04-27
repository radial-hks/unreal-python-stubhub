## HairSimulationConstraints Objects

```python
class HairSimulationConstraints(StructBase)
```

Hair Simulation Constraints

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetPhysics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bend_damping`` (float):  [Read-Write] Damping for the bend constraint between 0 and 1
- ``bend_stiffness`` (float):  [Read-Write] Stiffness for the bend constraint in GPa
- ``collision_radius`` (float):  [Read-Write] Radius that will be used for the collision detection against the physics asset
- ``kinetic_friction`` (float):  [Read-Write] Kinetic friction used for collision against the physics asset
- ``static_friction`` (float):  [Read-Write] Static friction used for collision against the physics asset
- ``strands_viscosity`` (float):  [Read-Write] Viscosity parameter between 0 and 1 that will be used for self collision
- ``stretch_damping`` (float):  [Read-Write] Damping for the stretch constraint between 0 and 1
- ``stretch_stiffness`` (float):  [Read-Write] Stiffness for the stretch constraint in GPa

<a id="unreal.HairSimulationConstraints.__init__"></a>

#### __init__

```python
def __init__(bend_damping: float = 0.000000,
             bend_stiffness: float = 0.000000,
             stretch_damping: float = 0.000000,
             stretch_stiffness: float = 0.000000,
             static_friction: float = 0.000000,
             kinetic_friction: float = 0.000000,
             strands_viscosity: float = 0.000000,
             collision_radius: float = 0.000000) -> None
```

<a id="unreal.HairSimulationConstraints.bend_damping"></a>

#### bend_damping

```python
@property
def bend_damping() -> float
```

(float):  [Read-Write] Damping for the bend constraint between 0 and 1

<a id="unreal.HairSimulationConstraints.bend_damping"></a>

#### bend_damping

```python
@bend_damping.setter
def bend_damping(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.bend_stiffness"></a>

#### bend_stiffness

```python
@property
def bend_stiffness() -> float
```

(float):  [Read-Write] Stiffness for the bend constraint in GPa

<a id="unreal.HairSimulationConstraints.bend_stiffness"></a>

#### bend_stiffness

```python
@bend_stiffness.setter
def bend_stiffness(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.stretch_damping"></a>

#### stretch_damping

```python
@property
def stretch_damping() -> float
```

(float):  [Read-Write] Damping for the stretch constraint between 0 and 1

<a id="unreal.HairSimulationConstraints.stretch_damping"></a>

#### stretch_damping

```python
@stretch_damping.setter
def stretch_damping(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.stretch_stiffness"></a>

#### stretch_stiffness

```python
@property
def stretch_stiffness() -> float
```

(float):  [Read-Write] Stiffness for the stretch constraint in GPa

<a id="unreal.HairSimulationConstraints.stretch_stiffness"></a>

#### stretch_stiffness

```python
@stretch_stiffness.setter
def stretch_stiffness(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.static_friction"></a>

#### static_friction

```python
@property
def static_friction() -> float
```

(float):  [Read-Write] Static friction used for collision against the physics asset

<a id="unreal.HairSimulationConstraints.static_friction"></a>

#### static_friction

```python
@static_friction.setter
def static_friction(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.kinetic_friction"></a>

#### kinetic_friction

```python
@property
def kinetic_friction() -> float
```

(float):  [Read-Write] Kinetic friction used for collision against the physics asset

<a id="unreal.HairSimulationConstraints.kinetic_friction"></a>

#### kinetic_friction

```python
@kinetic_friction.setter
def kinetic_friction(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.strands_viscosity"></a>

#### strands_viscosity

```python
@property
def strands_viscosity() -> float
```

(float):  [Read-Write] Viscosity parameter between 0 and 1 that will be used for self collision

<a id="unreal.HairSimulationConstraints.strands_viscosity"></a>

#### strands_viscosity

```python
@strands_viscosity.setter
def strands_viscosity(value: float) -> None
```

<a id="unreal.HairSimulationConstraints.collision_radius"></a>

#### collision_radius

```python
@property
def collision_radius() -> float
```

(float):  [Read-Write] Radius that will be used for the collision detection against the physics asset

<a id="unreal.HairSimulationConstraints.collision_radius"></a>

#### collision_radius

```python
@collision_radius.setter
def collision_radius(value: float) -> None
```

<a id="unreal.HairSimulationSetup"></a>