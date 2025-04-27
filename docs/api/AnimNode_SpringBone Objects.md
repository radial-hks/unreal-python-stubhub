## AnimNode_SpringBone Objects

```python
class AnimNode_SpringBone(AnimNode_SkeletalControlBase)
```

Simple controller that replaces or adds to the translation/rotation of a single bone.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_SpringBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``error_reset_thresh`` (double):  [Read-Write] If spring stretches more than this, reset it. Useful for catching teleports etc
- ``limit_displacement`` (bool):  [Read-Write] Limit the amount that a bone can stretch from its ref-pose length.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``max_displacement`` (double):  [Read-Write] If bLimitDisplacement is true, this indicates how long a bone can stretch beyond its length in the ref-pose.
- ``rotate_x`` (bool):  [Read-Write] If true take the spring calculation for rotation in X
- ``rotate_y`` (bool):  [Read-Write] If true take the spring calculation for rotation in Y
- ``rotate_z`` (bool):  [Read-Write] If true take the spring calculation for rotation in Z
- ``spring_bone`` (BoneReference):  [Read-Write] Name of bone to control. This is the main bone chain to modify from. *
- ``spring_damping`` (double):  [Read-Write] Damping of spring
- ``spring_stiffness`` (double):  [Read-Write] Stiffness of spring
- ``translate_x`` (bool):  [Read-Write] If true take the spring calculation for translation in X
- ``translate_y`` (bool):  [Read-Write] If true take the spring calculation for translation in Y
- ``translate_z`` (bool):  [Read-Write] If true take the spring calculation for translation in Z

<a id="unreal.AnimNode_SpringBone.__init__"></a>

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
             max_displacement: float = 0.000000) -> None
```

<a id="unreal.AnimNode_SpringBone.max_displacement"></a>

#### max_displacement

```python
@property
def max_displacement() -> float
```

(double):  [Read-Write] If bLimitDisplacement is true, this indicates how long a bone can stretch beyond its length in the ref-pose.

<a id="unreal.AnimNode_SpringBone.max_displacement"></a>

#### max_displacement

```python
@max_displacement.setter
def max_displacement(value: float) -> None
```

<a id="unreal.AnimNode_Trail"></a>