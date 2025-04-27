## AnimNode_BlendListByEnum Objects

```python
class AnimNode_BlendListByEnum(AnimNode_BlendListBase)
```

Blend List by Enum, it changes based on enum input that enters

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendListByEnum.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_enum_value`` (uint8):  [Read-Write] The currently selected pose (as an enum value)
- ``blend_pose`` (Array[PoseLink]):  [Read-Write]
- ``blend_profile`` (BlendProfile):  [Read-Write]
- ``blend_time`` (Array[float]):  [Read-Write]
- ``blend_type`` (AlphaBlendOption):  [Read-Write]
- ``custom_blend_curve`` (CurveFloat):  [Read-Write]
- ``reset_child_on_activation`` (bool):  [Read-Write] This reinitializes the re-activated child if the child's weight was zero.
- ``transition_type`` (BlendListTransitionType):  [Read-Write]

<a id="unreal.AnimNode_BlendListByEnum.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_BlendListByInt"></a>