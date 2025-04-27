## AnimNode_BlendListByBool Objects

```python
class AnimNode_BlendListByBool(AnimNode_BlendListBase)
```

This node is effectively a 'branch', picking one of two input poses based on an input Boolean value

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendListByBool.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_value`` (bool):  [Read-Write] Which input should be connected to the output?
- ``blend_pose`` (Array[PoseLink]):  [Read-Write]
- ``blend_profile`` (BlendProfile):  [Read-Write]
- ``blend_time`` (Array[float]):  [Read-Write]
- ``blend_type`` (AlphaBlendOption):  [Read-Write]
- ``custom_blend_curve`` (CurveFloat):  [Read-Write]
- ``reset_child_on_activation`` (bool):  [Read-Write] This reinitializes the re-activated child if the child's weight was zero.
- ``transition_type`` (BlendListTransitionType):  [Read-Write]

<a id="unreal.AnimNode_BlendListByBool.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_BlendListByEnum"></a>