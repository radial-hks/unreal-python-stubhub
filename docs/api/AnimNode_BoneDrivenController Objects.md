## AnimNode_BoneDrivenController Objects

```python
class AnimNode_BoneDrivenController(AnimNode_SkeletalControlBase)
```

This is the runtime version of a bone driven controller, which maps part of the state from one bone to another (e.g., 2 * source.x -> target.z)

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BoneDrivenController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_target_rotation_x`` (bool):  [Read-Write] Affect the X component of rotation on the target bone
- ``affect_target_rotation_y`` (bool):  [Read-Write] Affect the Y component of rotation on the target bone
- ``affect_target_rotation_z`` (bool):  [Read-Write] Affect the Z component of rotation on the target bone
- ``affect_target_scale_x`` (bool):  [Read-Write] Affect the X component of scale on the target bone
- ``affect_target_scale_y`` (bool):  [Read-Write] Affect the Y component of scale on the target bone
- ``affect_target_scale_z`` (bool):  [Read-Write] Affect the Z component of scale on the target bone
- ``affect_target_translation_x`` (bool):  [Read-Write] Affect the X component of translation on the target bone
- ``affect_target_translation_y`` (bool):  [Read-Write] Affect the Y component of translation on the target bone
- ``affect_target_translation_z`` (bool):  [Read-Write] Affect the Z component of translation on the target bone
- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``destination_mode`` (DrivenDestinationMode):  [Read-Write] Type of destination to drive, currently either bone or morph target
- ``driving_curve`` (CurveFloat):  [Read-Write] Curve used to map from the source attribute to the driven attributes if present (otherwise the Multiplier will be used)
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``modification_mode`` (DrivenBoneModificationMode):  [Read-Write] The type of modification to make to the destination component(s)
- ``multiplier`` (float):  [Read-Write] Multiplier to apply to the input value (Note: Ignored when a curve is used)
- ``parameter_name`` (Name):  [Read-Write] Name of Morph Target to drive using the source attribute
- ``range_max`` (double):  [Read-Write] Maximum limit of the input value (mapped to RemappedMax, only used when limiting the source range)
  If this is rotation, the unit is radian
- ``range_min`` (double):  [Read-Write] Minimum limit of the input value (mapped to RemappedMin, only used when limiting the source range)
  If this is rotation, the unit is radian
- ``remapped_max`` (double):  [Read-Write] Maximum value to apply to the destination (remapped from the input range)
  If this is rotation, the unit is radian
- ``remapped_min`` (double):  [Read-Write] Minimum value to apply to the destination (remapped from the input range)
  If this is rotation, the unit is radian
- ``source_bone`` (BoneReference):  [Read-Write] Bone to use as controller input
- ``source_component`` (ComponentType):  [Read-Write] Transform component to use as input
- ``target_bone`` (BoneReference):  [Read-Write] Bone to drive using controller input
- ``use_range`` (bool):  [Read-Write] Whether or not to clamp the driver value and remap it before scaling it

<a id="unreal.AnimNode_BoneDrivenController.__init__"></a>

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

<a id="unreal.AnimNode_CCDIK"></a>