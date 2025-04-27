## FBIKEndEffector Objects

```python
class FBIKEndEffector(StructBase)
```

FBIKEnd Effector

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: FullBodyIK
- **File**: RigUnit_FullbodyIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Only] The last item in the chain to solve - the effector

<a id="unreal.FBIKEndEffector.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.FBIKEndEffector.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only] The last item in the chain to solve - the effector

<a id="unreal.RigUnit_FullbodyIK"></a>