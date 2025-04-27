## ControlRigTransformWorkflowOptions Objects

```python
class ControlRigTransformWorkflowOptions(ControlRigWorkflowOptions)
```

Control Rig Transform Workflow Options

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigNodeWorkflow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hierarchy`` (RigHierarchy):  [Read-Write]
- ``selection`` (Array[RigElementKey]):  [Read-Write]
- ``subject`` (Object):  [Read-Write]
- ``transform_type`` (RigTransformType):  [Read-Write] The type of transform to retrieve from the hierarchy
- ``workflow`` (RigVMUserWorkflow):  [Read-Write]

<a id="unreal.ControlRigTransformWorkflowOptions.transform_type"></a>

#### transform_type

```python
@property
def transform_type() -> RigTransformType
```

(RigTransformType):  [Read-Write] The type of transform to retrieve from the hierarchy

<a id="unreal.ControlRigTransformWorkflowOptions.transform_type"></a>

#### transform_type

```python
@transform_type.setter
def transform_type(value: RigTransformType) -> None
```

<a id="unreal.PyTestInterface"></a>