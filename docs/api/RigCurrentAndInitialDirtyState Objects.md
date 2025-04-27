## RigCurrentAndInitialDirtyState Objects

```python
class RigCurrentAndInitialDirtyState(StructBase)
```

Rig Current and Initial Dirty State

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current`` (RigLocalAndGlobalDirtyState):  [Read-Write]
- ``initial`` (RigLocalAndGlobalDirtyState):  [Read-Write]

<a id="unreal.RigCurrentAndInitialDirtyState.__init__"></a>

#### __init__

```python
def __init__(current: RigLocalAndGlobalDirtyState = [[], []],
             initial: RigLocalAndGlobalDirtyState = [[], []]) -> None
```

<a id="unreal.RigCurrentAndInitialDirtyState.current"></a>

#### current

```python
@property
def current() -> RigLocalAndGlobalDirtyState
```

(RigLocalAndGlobalDirtyState):  [Read-Only]

<a id="unreal.RigCurrentAndInitialDirtyState.initial"></a>

#### initial

```python
@property
def initial() -> RigLocalAndGlobalDirtyState
```

(RigLocalAndGlobalDirtyState):  [Read-Only]

<a id="unreal.RigComputedTransform"></a>