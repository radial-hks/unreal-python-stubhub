## RigUnit_HierarchyAddPhysicsSolver Objects

```python
class RigUnit_HierarchyAddPhysicsSolver(RigUnit_DynamicHierarchyBaseMutable)
```

Adds a new physics solver to the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Physics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``name`` (Name):  [Read-Write] * The name of the new solver to add
- ``solver`` (RigPhysicsSolverID):  [Read-Write] * The identifier of the solver

<a id="unreal.RigUnit_HierarchyAddPhysicsSolver.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             name: Name = "None",
             solver: RigPhysicsSolverID = [[]]) -> None
```

<a id="unreal.RigUnit_HierarchyAddPhysicsSolver.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] * The name of the new solver to add

<a id="unreal.RigUnit_HierarchyAddPhysicsSolver.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_HierarchyAddPhysicsSolver.solver"></a>

#### solver

```python
@property
def solver() -> RigPhysicsSolverID
```

(RigPhysicsSolverID):  [Read-Only] * The identifier of the solver

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint"></a>