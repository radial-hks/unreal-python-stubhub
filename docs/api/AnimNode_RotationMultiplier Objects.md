## AnimNode_RotationMultiplier Objects

```python
class AnimNode_RotationMultiplier(AnimNode_SkeletalControlBase)
```

Simple controller that multiplies scalar value to the translation/rotation/scale of a single bone.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RotationMultiplier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``is_additive`` (bool):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``multiplier`` (float):  [Read-Write] To make these to be easily pin-hookable, I'm not making it struct, but each variable
  0.f is invalid, and default
- ``rotation_axis_to_refer`` (BoneAxis):  [Read-Write]
- ``source_bone`` (BoneReference):  [Read-Write] Source to get transform from
- ``target_bone`` (BoneReference):  [Read-Write] Name of bone to control. This is the main bone chain to modify from.

<a id="unreal.AnimNode_RotationMultiplier.__init__"></a>

#### __init__

```python
def __init__(component_pose: ComponentSpacePoseLink = [],
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
                 False, False, False, [0.000000,
                                       1.000000], [0.000000, 1.000000],
                 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
             ],
             multiplier: float = 0.000000) -> None
```

<a id="unreal.AnimNode_RotationMultiplier.multiplier"></a>

#### multiplier

```python
@property
def multiplier() -> float
```

(float):  [Read-Write] To make these to be easily pin-hookable, I'm not making it struct, but each variable
0.f is invalid, and default

<a id="unreal.AnimNode_RotationMultiplier.multiplier"></a>

#### multiplier

```python
@multiplier.setter
def multiplier(value: float) -> None
```

<a id="unreal.BlendSpaceReference"></a>