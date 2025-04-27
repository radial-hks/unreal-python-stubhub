## AnimNode_Trail Objects

```python
class AnimNode_Trail(AnimNode_SkeletalControlBase)
```

Trail Controller

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_Trail.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_space_fake_vel`` (bool):  [Read-Write] Whether 'fake' velocity should be applied in actor or world space.
- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``base_joint`` (BoneReference):  [Read-Write] Base Joint to calculate velocity from. If none, it will use Component's World Transform. .
- ``chain_bone_axis`` (AxisType):  [Read-Write] Axis of the bones to point along trail.
- ``chain_length`` (int32):  [Read-Write] Number of bones above the active one in the hierarchy to modify. ChainLength should be at least 2.
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``debug_life_time`` (float):  [Read-Write] Debug Life Time
- ``enable_debug`` (bool):  [Read-Write] Enable Debug in the PIE. This doesn't work in game
- ``fake_velocity`` (Vector):  [Read-Write] 'Fake' velocity applied to bones.
- ``invert_chain_bone_axis`` (bool):  [Read-Write] Invert the direction specified in ChainBoneAxis.
- ``last_bone_rotation_anim_alpha_blend`` (float):  [Read-Write] How to set last bone rotation. It copies from previous joint if alpha is 0.f, or 1.f will use animated pose
         * This alpha dictates the blend between parent joint and animated pose, and how much you'd like to use animated pose for
- ``limit_rotation`` (bool):  [Read-Write] Limit the amount that a bone can stretch from its ref-pose length.
- ``limit_stretch`` (bool):  [Read-Write] Limit the amount that a bone can stretch from its ref-pose length.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``max_delta_time`` (float):  [Read-Write] To avoid hitches causing stretch of trail, you can use MaxDeltaTime to clamp the long delta time. If you want 30 fps to set it to 0.03333f ( = 1/30 ).
- ``planar_limits`` (Array[AnimPhysPlanarLimit]):  [Read-Write] List of available planar limits for this node
- ``relaxation_speed_scale`` (float):  [Read-Write]
- ``relaxation_speed_scale_input_processor`` (InputScaleBiasClamp):  [Read-Write]
- ``reorient_parent_to_child`` (bool):  [Read-Write] Fix up rotation to face child for the parent
- ``rotation_limits`` (Array[RotationLimit]):  [Read-Write]
- ``rotation_offsets`` (Array[Vector]):  [Read-Write]
- ``show_base_motion`` (bool):  [Read-Write] Show Base Motion
- ``show_limit`` (bool):  [Read-Write] Show Planar Limits *
- ``show_trail_location`` (bool):  [Read-Write] Show Trail Location *
- ``stretch_limit`` (float):  [Read-Write] If bLimitStretch is true, this indicates how long a bone can stretch beyond its length in the ref-pose.
- ``trail_bone`` (BoneReference):  [Read-Write] Reference to the active bone in the hierarchy to modify.
- ``trail_relaxation_speed`` (RuntimeFloatCurve):  [Read-Write] How quickly we 'relax' the bones to their animated positions. Time 0 will map to top root joint, time 1 will map to the bottom joint.
- ``use_planar_limit`` (bool):  [Read-Write] Whether to evaluate planar limits

<a id="unreal.AnimNode_Trail.__init__"></a>

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
             relaxation_speed_scale: float = 0.000000,
             relaxation_speed_scale_input_processor: InputScaleBiasClamp = [
                 False, False, False, [0.000000,
                                       1.000000], [0.000000, 1.000000],
                 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
             ],
             rotation_offsets: Array[Vector] = []) -> None
```

<a id="unreal.AnimNode_Trail.relaxation_speed_scale"></a>

#### relaxation_speed_scale

```python
@property
def relaxation_speed_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_Trail.relaxation_speed_scale"></a>

#### relaxation_speed_scale

```python
@relaxation_speed_scale.setter
def relaxation_speed_scale(value: float) -> None
```

<a id="unreal.AnimNode_Trail.relaxation_speed_scale_input_processor"></a>

#### relaxation_speed_scale_input_processor

```python
@property
def relaxation_speed_scale_input_processor() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_Trail.relaxation_speed_scale_input_processor"></a>

#### relaxation_speed_scale_input_processor

```python
@relaxation_speed_scale_input_processor.setter
def relaxation_speed_scale_input_processor(value: InputScaleBiasClamp) -> None
```

<a id="unreal.AnimNode_Trail.rotation_offsets"></a>

#### rotation_offsets

```python
@property
def rotation_offsets() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.AnimNode_Trail.rotation_offsets"></a>

#### rotation_offsets

```python
@rotation_offsets.setter
def rotation_offsets(value: Array[Vector]) -> None
```

<a id="unreal.AnimNode_TwistCorrectiveNode"></a>