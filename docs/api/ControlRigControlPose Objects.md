## ControlRigControlPose Objects

```python
class ControlRigControlPose(StructBase)
```

The Data Stored For Each Pose and associated Functions to Store and Paste It

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``copy_of_controls`` (Array[RigControlCopy]):  [Read-Write]

<a id="unreal.ControlRigControlPose.__init__"></a>

#### __init__

```python
def __init__(copy_of_controls: Array[RigControlCopy] = []) -> None
```

<a id="unreal.ControlRigControlPose.copy_of_controls"></a>

#### copy_of_controls

```python
@property
def copy_of_controls() -> Array[RigControlCopy]
```

(Array[RigControlCopy]):  [Read-Write]

<a id="unreal.ControlRigControlPose.copy_of_controls"></a>

#### copy_of_controls

```python
@copy_of_controls.setter
def copy_of_controls(value: Array[RigControlCopy]) -> None
```

<a id="unreal.RigVMDispatchFactory"></a>