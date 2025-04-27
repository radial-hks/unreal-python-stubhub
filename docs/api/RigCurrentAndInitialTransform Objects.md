## RigCurrentAndInitialTransform Objects

```python
class RigCurrentAndInitialTransform(StructBase)
```

Rig Current and Initial Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current`` (RigLocalAndGlobalTransform):  [Read-Write]
- ``initial`` (RigLocalAndGlobalTransform):  [Read-Write]

<a id="unreal.RigCurrentAndInitialTransform.__init__"></a>

#### __init__

```python
def __init__(current: RigLocalAndGlobalTransform = [[], []],
             initial: RigLocalAndGlobalTransform = [[], []]) -> None
```

<a id="unreal.RigCurrentAndInitialTransform.current"></a>

#### current

```python
@property
def current() -> RigLocalAndGlobalTransform
```

(RigLocalAndGlobalTransform):  [Read-Only]

<a id="unreal.RigCurrentAndInitialTransform.initial"></a>

#### initial

```python
@property
def initial() -> RigLocalAndGlobalTransform
```

(RigLocalAndGlobalTransform):  [Read-Only]

<a id="unreal.RigSingleParentElement"></a>