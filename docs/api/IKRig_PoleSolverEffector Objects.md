## IKRig_PoleSolverEffector Objects

```python
class IKRig_PoleSolverEffector(Object)
```

IKRig Pole Solver Effector

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_PoleSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Blend the effector on/off. Range is 0-1. Default is 1.0.
- ``bone_name`` (Name):  [Read-Only]
- ``goal_name`` (Name):  [Read-Only]

<a id="unreal.IKRig_PoleSolverEffector.goal_name"></a>

#### goal_name

```python
@property
def goal_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.IKRig_PoleSolverEffector.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.IKRig_PoleSolverEffector.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] Blend the effector on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_PoleSolverEffector.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.IKRig_PoleSolver"></a>