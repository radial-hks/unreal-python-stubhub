## RigLocalAndGlobalTransform Objects

```python
class RigLocalAndGlobalTransform(StructBase)
```

Rig Local and Global Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (RigComputedTransform):  [Read-Write]
- ``local`` (RigComputedTransform):  [Read-Write]

<a id="unreal.RigLocalAndGlobalTransform.__init__"></a>

#### __init__

```python
def __init__(local: RigComputedTransform = [],
             global_: RigComputedTransform = []) -> None
```

<a id="unreal.RigLocalAndGlobalTransform.local"></a>

#### local

```python
@property
def local() -> RigComputedTransform
```

(RigComputedTransform):  [Read-Only]

<a id="unreal.RigLocalAndGlobalTransform.global_"></a>

#### global_

```python
@property
def global_() -> RigComputedTransform
```

(RigComputedTransform):  [Read-Only]

<a id="unreal.RigCurrentAndInitialTransform"></a>