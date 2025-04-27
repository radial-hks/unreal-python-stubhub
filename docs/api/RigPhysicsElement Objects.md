## RigPhysicsElement Objects

```python
class RigPhysicsElement(RigSingleParentElement)
```

Rig Physics Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``selected`` (bool):  [Read-Write]
- ``settings`` (RigPhysicsSettings):  [Read-Write]
- ``solver`` (RigPhysicsSolverID):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigPhysicsElement.__init__"></a>

#### __init__

```python
def __init__(key: RigElementKey = [RigElementType.NONE, "None"],
             index: int = 0,
             sub_index: int = 0,
             created_at_instruction_index: int = 0,
             selected: bool = False,
             solver: RigPhysicsSolverID = [[]],
             settings: RigPhysicsSettings = [1.000000]) -> None
```

<a id="unreal.RigPhysicsElement.solver"></a>

#### solver

```python
@property
def solver() -> RigPhysicsSolverID
```

(RigPhysicsSolverID):  [Read-Only]

<a id="unreal.RigPhysicsElement.settings"></a>

#### settings

```python
@property
def settings() -> RigPhysicsSettings
```

(RigPhysicsSettings):  [Read-Only]

<a id="unreal.RigReferenceElement"></a>