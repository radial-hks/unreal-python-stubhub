## RigLocalAndGlobalDirtyState Objects

```python
class RigLocalAndGlobalDirtyState(StructBase)
```

Rig Local and Global Dirty State

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (RigTransformDirtyState):  [Read-Write]
- ``local`` (RigTransformDirtyState):  [Read-Write]

<a id="unreal.RigLocalAndGlobalDirtyState.__init__"></a>

#### __init__

```python
def __init__(global_: RigTransformDirtyState = [],
             local: RigTransformDirtyState = []) -> None
```

<a id="unreal.RigLocalAndGlobalDirtyState.global_"></a>

#### global_

```python
@property
def global_() -> RigTransformDirtyState
```

(RigTransformDirtyState):  [Read-Only]

<a id="unreal.RigLocalAndGlobalDirtyState.local"></a>

#### local

```python
@property
def local() -> RigTransformDirtyState
```

(RigTransformDirtyState):  [Read-Only]

<a id="unreal.RigCurrentAndInitialDirtyState"></a>