## AnimNode_BlendListBase Objects

```python
class AnimNode_BlendListBase(AnimNode_Base)
```

Blend list node; has many children

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendListBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_pose`` (Array[PoseLink]):  [Read-Write]
- ``blend_profile`` (BlendProfile):  [Read-Write]
- ``blend_time`` (Array[float]):  [Read-Write]
- ``blend_type`` (AlphaBlendOption):  [Read-Write]
- ``custom_blend_curve`` (CurveFloat):  [Read-Write]
- ``reset_child_on_activation`` (bool):  [Read-Write] This reinitializes the re-activated child if the child's weight was zero.
- ``transition_type`` (BlendListTransitionType):  [Read-Write]

<a id="unreal.AnimNode_BlendListBase.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_BlendListByBool"></a>