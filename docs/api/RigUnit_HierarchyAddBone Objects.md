## RigUnit_HierarchyAddBone Objects

```python
class RigUnit_HierarchyAddBone(RigUnit_HierarchyAddElement)
```

Adds a new bone to the hierarchy
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transform should be interpreted in local or global space
- ``transform`` (Transform):  [Read-Write] * The initial transform of the new element

<a id="unreal.RigUnit_HierarchyAddBone.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        parent: RigElementKey = [RigElementType.NONE, "None"],
        name: Name = "None",
        item: RigElementKey = [RigElementType.NONE, "None"],
        transform: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_HierarchyAddBone.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] * The initial transform of the new element

<a id="unreal.RigUnit_HierarchyAddBone.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyAddBone.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transform should be interpreted in local or global space

<a id="unreal.RigUnit_HierarchyAddBone.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_HierarchyAddNull"></a>