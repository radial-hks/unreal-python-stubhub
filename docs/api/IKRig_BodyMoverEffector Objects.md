## IKRig_BodyMoverEffector Objects

```python
class IKRig_BodyMoverEffector(Object)
```

IKRig Body Mover Effector

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_BodyMover.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Only]
- ``goal_name`` (Name):  [Read-Only]
- ``influence_multiplier`` (float):  [Read-Write] Scale the influence this effector has on the body. Range is 0-10. Default is 1.0.

<a id="unreal.IKRig_BodyMoverEffector.goal_name"></a>

#### goal_name

```python
@property
def goal_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.IKRig_BodyMoverEffector.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.IKRig_BodyMoverEffector.influence_multiplier"></a>

#### influence_multiplier

```python
@property
def influence_multiplier() -> float
```

(float):  [Read-Write] Scale the influence this effector has on the body. Range is 0-10. Default is 1.0.

<a id="unreal.IKRig_BodyMoverEffector.influence_multiplier"></a>

#### influence_multiplier

```python
@influence_multiplier.setter
def influence_multiplier(value: float) -> None
```

<a id="unreal.IKRigSolver"></a>