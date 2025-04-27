## AnimNode_TwistCorrectiveNode Objects

```python
class AnimNode_TwistCorrectiveNode(AnimNode_SkeletalControlBase)
```

This is the node that apply corrective morphtarget for twist
Good example is that if you twist your neck too far right or left, you're going to see odd stretch shape of neck,
This node can detect the angle and apply morphtarget curve
This isn't the twist control node for bone twist

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_TwistCorrectiveNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``base_frame`` (ReferenceBoneFrame):  [Read-Write] Base Frame of the reference for the twist node
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``curve_name`` (Name):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``range_max`` (float):  [Read-Write] Maximum limit of the input value (mapped to RemappedMax, only used when limiting the source range)
  We can't go more than 180 right now because this is dot product driver
- ``remapped_max`` (float):  [Read-Write] Maximum value to apply to the destination (remapped from the input range)
- ``remapped_min`` (float):  [Read-Write] Minimum value to apply to the destination (remapped from the input range)
- ``twist_frame`` (ReferenceBoneFrame):  [Read-Write] Transform component to use as input
- ``twist_plane_normal_axis`` (Axis):  [Read-Write] Normal of the Plane that we'd like to calculate angle calculation from in BaseFrame. Please note we're looking for Normal Axis

<a id="unreal.AnimNode_TwistCorrectiveNode.__init__"></a>

#### __init__

```python
def __init__(
    component_pose: ComponentSpacePoseLink = [],
    lod_threshold: int = 0,
    alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT,
    alpha_bool_enabled: bool = False,
    alpha: float = 0.000000,
    alpha_scale_bias: InputScaleBias = [1.000000, 0.000000],
    alpha_bool_blend: InputAlphaBoolBlend = [
        0.000000, 0.000000, AlphaBlendOption.LINEAR, None
    ],
    alpha_curve_name: Name = "None",
    alpha_scale_bias_clamp: InputScaleBiasClamp = [
        False, False, False, [0.000000, 1.000000], [0.000000, 1.000000],
        1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
    ]
) -> None
```

<a id="unreal.AnimNode_TwoBoneIK"></a>