## AnimNode_RotationOffsetBlendSpace Objects

```python
class AnimNode_RotationOffsetBlendSpace(AnimNode_BlendSpacePlayer)
```

TODO:: Comment

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RotationOffsetBlendSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the AimOffset
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``base_pose`` (PoseLink):  [Read-Write]
- ``blend_space`` (BlendSpace):  [Read-Write] The blendspace asset to play
- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``group_name`` (Name):  [Read-Write] The group name that we synchronize with (NAME_None if it is not part of any group). Note that
  this is the name of the group used to sync the output of this node - it will not force
  syncing of animations contained by it.
- ``group_role`` (AnimGroupRole):  [Read-Write] The role this node can assume within the group (ignored if GroupName is not set). Note
  that this is the role of the output of this node, not of animations contained by it.
- ``ignore_for_relevancy_test`` (bool):  [Read-Write] If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``loop`` (bool):  [Read-Write] Should the animation loop back to the start when it reaches the end?
- ``method`` (AnimSyncMethod):  [Read-Write] How this node will synchronize with other animations. Note that this determines how the output
  of this node is used for synchronization, not of animations contained by it.
- ``play_rate`` (float):  [Read-Write] The play rate multiplier. Can be negative, which will cause the animation to play in reverse.
- ``reset_play_time_when_blend_space_changes`` (bool):  [Read-Write] Whether we should reset the current play time when the blend space changes
- ``start_position`` (float):  [Read-Write] The start position in [0, 1] to use when initializing. When looping, play will still jump back to the beginning when reaching the end.
- ``x`` (float):  [Read-Write] The X coordinate to sample in the blendspace
- ``y`` (float):  [Read-Write] The Y coordinate to sample in the blendspace

<a id="unreal.AnimNode_RotationOffsetBlendSpace.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             base_pose: PoseLink = [],
             lod_threshold: int = 0,
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
             alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT,
             alpha_bool_enabled: bool = False) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.base_pose"></a>

#### base_pose

```python
@property
def base_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.base_pose"></a>

#### base_pose

```python
@base_pose.setter
def base_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.lod_threshold"></a>

#### lod_threshold

```python
@property
def lod_threshold() -> int
```

(int32):  [Read-Write] * Max LOD that this node is allowed to run
* For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
* when the component LOD becomes 3, it will stop update/evaluate
* currently transition would be issue and that has to be re-visited

<a id="unreal.AnimNode_RotationOffsetBlendSpace.lod_threshold"></a>

#### lod_threshold

```python
@lod_threshold.setter
def lod_threshold(value: int) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] Current strength of the AimOffset

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@property
def alpha_bool_blend() -> InputAlphaBoolBlend
```

(InputAlphaBoolBlend):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@alpha_bool_blend.setter
def alpha_bool_blend(value: InputAlphaBoolBlend) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_curve_name"></a>

#### alpha_curve_name

```python
@property
def alpha_curve_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_curve_name"></a>

#### alpha_curve_name

```python
@alpha_curve_name.setter
def alpha_curve_name(value: Name) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@property
def alpha_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@alpha_scale_bias_clamp.setter
def alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_input_type"></a>

#### alpha_input_type

```python
@property
def alpha_input_type() -> AnimAlphaInputType
```

(AnimAlphaInputType):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_input_type"></a>

#### alpha_input_type

```python
@alpha_input_type.setter
def alpha_input_type(value: AnimAlphaInputType) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@property
def alpha_bool_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@alpha_bool_enabled.setter
def alpha_bool_enabled(value: bool) -> None
```

<a id="unreal.AnimNode_RotationOffsetBlendSpaceGraph"></a>