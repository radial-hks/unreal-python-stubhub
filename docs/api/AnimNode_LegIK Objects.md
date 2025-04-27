## AnimNode_LegIK Objects

```python
class AnimNode_LegIK(AnimNode_SkeletalControlBase)
```

Anim Node Leg IK

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_LegIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``legs_definition`` (Array[AnimLegIKDefinition]):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``max_iterations`` (int32):  [Read-Write] Max Number of Iterations.
- ``reach_precision`` (float):  [Read-Write] Tolerance for reaching IK Target, in unreal units.
- ``soft_alpha`` (float):  [Read-Write] Default is 1.0 (full). Range is 0 to 1. Blends the effect of the "softness" on/off.
- ``soft_percent_length`` (float):  [Read-Write] Default is 1.0 (off). Range is 0.1 to 1.0. When set to a value less than 1, will "softly" approach full extension starting when the effector
  distance from the root of the chain is greater than this percent length of the bone chain. Typical values are around 0.97.
  This is useful for preventing the knee from "popping" when approaching full extension.

<a id="unreal.AnimNode_LegIK.__init__"></a>

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

<a id="unreal.AnimNode_LookAt"></a>