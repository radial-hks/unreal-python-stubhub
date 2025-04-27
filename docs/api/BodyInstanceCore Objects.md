## BodyInstanceCore Objects

```python
class BodyInstanceCore(StructBase)
```

Body Instance Core

**C++ Source:**

- **Module**: PhysicsCore
- **File**: BodyInstanceCore.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_weld`` (bool):  [Read-Write] If true and is attached to a parent, the two bodies will be joined into a single rigid body. Physical settings like collision profile and body settings are determined by the root
- ``enable_gravity`` (bool):  [Read-Write] If object should have the force of gravity applied
- ``generate_wake_events`` (bool):  [Read-Write] Should 'wake/sleep' events fire when this object is woken up or put to sleep by the physics simulation.
- ``override_mass`` (bool):  [Read-Write] If true, mass will not be automatically computed and you must set it directly
- ``simulate_physics`` (bool):  [Read-Write] If true, this body will use simulation. If false, will be 'fixed' (ie kinematic) and move where it is told.
  For a Skeletal Mesh Component, simulating requires a physics asset setup and assigned on the SkeletalMesh asset.
  For a Static Mesh Component, simulating requires simple collision to be setup on the StaticMesh asset.
- ``start_awake`` (bool):  [Read-Write] If object should start awake, or if it should initially be sleeping
- ``update_kinematic_from_simulation`` (bool):  [Read-Write] When kinematic, whether the actor transform should be updated as a result of movement in the simulation, rather than immediately whenever a target transform is set.
- ``update_mass_when_scale_changes`` (bool):  [Read-Write] If true, it will update mass when scale change *

<a id="unreal.BodyInstanceCore.__init__"></a>

#### __init__

```python
def __init__(simulate_physics: bool = False,
             enable_gravity: bool = False,
             update_kinematic_from_simulation: bool = False,
             auto_weld: bool = False,
             start_awake: bool = False,
             generate_wake_events: bool = False,
             update_mass_when_scale_changes: bool = False) -> None
```

<a id="unreal.BodyInstanceCore.simulate_physics"></a>

#### simulate_physics

```python
@property
def simulate_physics() -> bool
```

(bool):  [Read-Write] If true, this body will use simulation. If false, will be 'fixed' (ie kinematic) and move where it is told.
For a Skeletal Mesh Component, simulating requires a physics asset setup and assigned on the SkeletalMesh asset.
For a Static Mesh Component, simulating requires simple collision to be setup on the StaticMesh asset.

<a id="unreal.BodyInstanceCore.simulate_physics"></a>

#### simulate_physics

```python
@simulate_physics.setter
def simulate_physics(value: bool) -> None
```

<a id="unreal.BodyInstanceCore.enable_gravity"></a>

#### enable_gravity

```python
@property
def enable_gravity() -> bool
```

(bool):  [Read-Only] If object should have the force of gravity applied

<a id="unreal.BodyInstanceCore.update_kinematic_from_simulation"></a>

#### update_kinematic_from_simulation

```python
@property
def update_kinematic_from_simulation() -> bool
```

(bool):  [Read-Only] When kinematic, whether the actor transform should be updated as a result of movement in the simulation, rather than immediately whenever a target transform is set.

<a id="unreal.BodyInstanceCore.auto_weld"></a>

#### auto_weld

```python
@property
def auto_weld() -> bool
```

(bool):  [Read-Write] If true and is attached to a parent, the two bodies will be joined into a single rigid body. Physical settings like collision profile and body settings are determined by the root

<a id="unreal.BodyInstanceCore.auto_weld"></a>

#### auto_weld

```python
@auto_weld.setter
def auto_weld(value: bool) -> None
```

<a id="unreal.BodyInstanceCore.start_awake"></a>

#### start_awake

```python
@property
def start_awake() -> bool
```

(bool):  [Read-Only] If object should start awake, or if it should initially be sleeping

<a id="unreal.BodyInstanceCore.generate_wake_events"></a>

#### generate_wake_events

```python
@property
def generate_wake_events() -> bool
```

(bool):  [Read-Only] Should 'wake/sleep' events fire when this object is woken up or put to sleep by the physics simulation.

<a id="unreal.BodyInstanceCore.update_mass_when_scale_changes"></a>

#### update_mass_when_scale_changes

```python
@property
def update_mass_when_scale_changes() -> bool
```

(bool):  [Read-Write] If true, it will update mass when scale change *

<a id="unreal.BodyInstanceCore.update_mass_when_scale_changes"></a>

#### update_mass_when_scale_changes

```python
@update_mass_when_scale_changes.setter
def update_mass_when_scale_changes(value: bool) -> None
```

<a id="unreal.BodyInstance"></a>