## AnimNodeControlRigLibrary Objects

```python
class AnimNodeControlRigLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a control rig anim node

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: AnimNode_ControlRig_Library.h

<a id="unreal.AnimNodeControlRigLibrary.set_control_rig_class"></a>

#### set_control_rig_class

```python
@classmethod
def set_control_rig_class(cls, node: ControlRigReference,
                          control_rig_class: Class) -> ControlRigReference
```

X.set_control_rig_class(node, control_rig_class) -> ControlRigReference
Set the control rig class on the node

Args:
    node (ControlRigReference): 
    control_rig_class (type(Class)): 

Returns:
    ControlRigReference:

<a id="unreal.AnimNodeControlRigLibrary.convert_to_control_rig_pure"></a>

#### convert_to_control_rig_pure

```python
@classmethod
def convert_to_control_rig_pure(
        cls, node: AnimNodeReference) -> Tuple[ControlRigReference, bool]
```

X.convert_to_control_rig_pure(node) -> (control_rig=ControlRigReference, result=bool)
Get a control rig context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    control_rig (ControlRigReference): 

    result (bool):

<a id="unreal.AnimNodeControlRigLibrary.convert_to_control_rig"></a>

#### convert_to_control_rig

```python
@classmethod
def convert_to_control_rig(
    cls, node: AnimNodeReference
) -> Tuple[ControlRigReference, AnimNodeReferenceConversionResult]
```

X.convert_to_control_rig(node) -> (ControlRigReference, result=AnimNodeReferenceConversionResult)
Get a control rig context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.TransformableControlHandle"></a>