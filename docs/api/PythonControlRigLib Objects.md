## PythonControlRigLib Objects

```python
class PythonControlRigLib(BlueprintFunctionLibrary)
```

Python Control Rig Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonControlRigLib.h

<a id="unreal.PythonControlRigLib.get_control_shape_transform"></a>

#### get\_control\_shape\_transform

```python
@classmethod
def get_control_shape_transform(cls,
                                rig_hierarchy: RigHierarchy,
                                control_element: RigElementKey,
                                initial: bool = True) -> Transform
```

X.get_control_shape_transform(rig_hierarchy, control_element, initial=True) -> Transform
Get Control Shape Transform

Args:
    rig_hierarchy (RigHierarchy): 
    control_element (RigElementKey): 
    initial (bool): 

Returns:
    Transform:

<a id="unreal.PythonDataTableLib"></a>