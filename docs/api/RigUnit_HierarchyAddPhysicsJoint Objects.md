## RigUnit_HierarchyAddPhysicsJoint Objects

```python
class RigUnit_HierarchyAddPhysicsJoint(RigUnit_HierarchyAddElement)
```

Adds a new physics joint to the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Physics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add
- ``settings`` (RigPhysicsSettings):  [Read-Write] * The settings of the new physics element
- ``solver`` (RigPhysicsSolverID):  [Read-Write] * The solver to relate this new physics element to
- ``transform`` (Transform):  [Read-Write] * The initial global transform of the spawned element

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             parent: RigElementKey = [RigElementType.NONE, "None"],
             name: Name = "None",
             item: RigElementKey = [RigElementType.NONE, "None"],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             solver: RigPhysicsSolverID = [[]],
             settings: RigPhysicsSettings = [1.000000]) -> None
```

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] * The initial global transform of the spawned element

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.solver"></a>

#### solver

```python
@property
def solver() -> RigPhysicsSolverID
```

(RigPhysicsSolverID):  [Read-Write] * The solver to relate this new physics element to

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.solver"></a>

#### solver

```python
@solver.setter
def solver(value: RigPhysicsSolverID) -> None
```

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.settings"></a>

#### settings

```python
@property
def settings() -> RigPhysicsSettings
```

(RigPhysicsSettings):  [Read-Write] * The settings of the new physics element

<a id="unreal.RigUnit_HierarchyAddPhysicsJoint.settings"></a>

#### settings

```python
@settings.setter
def settings(value: RigPhysicsSettings) -> None
```

<a id="unreal.RigUnit_PrepareForExecution"></a>