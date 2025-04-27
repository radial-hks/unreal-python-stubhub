## TransformableControlHandle Objects

```python
class TransformableControlHandle(TransformableHandle)
```

UTransformableControlHandle

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigTransformableHandle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constraint_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] possible bindingID
- ``control_name`` (Name):  [Read-Write] The ControlName of the control that this handle is pointing at.
- ``control_rig`` (ControlRig):  [Read-Write] The ControlRig that this handle is pointing at.

<a id="unreal.TransformableControlHandle.control_rig"></a>

#### control_rig

```python
@property
def control_rig() -> ControlRig
```

(ControlRig):  [Read-Only] The ControlRig that this handle is pointing at.

<a id="unreal.TransformableControlHandle.control_name"></a>

#### control_name

```python
@property
def control_name() -> Name
```

(Name):  [Read-Only] The ControlName of the control that this handle is pointing at.

<a id="unreal.ControlRigAnimInstance"></a>