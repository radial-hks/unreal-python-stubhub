## AnimNode_SkeletalControlBase Objects

```python
class AnimNode_SkeletalControlBase(AnimNode_Base)
```

Anim Node Skeletal Control Base

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_SkeletalControlBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited

<a id="unreal.AnimNode_SkeletalControlBase.__init__"></a>

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

<a id="unreal.AnimNode_SkeletalControlBase.component_pose"></a>

#### component_pose

```python
@property
def component_pose() -> ComponentSpacePoseLink
```

(ComponentSpacePoseLink):  [Read-Write] Input link

<a id="unreal.AnimNode_SkeletalControlBase.component_pose"></a>

#### component_pose

```python
@component_pose.setter
def component_pose(value: ComponentSpacePoseLink) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.lod_threshold"></a>

#### lod_threshold

```python
@property
def lod_threshold() -> int
```

(int32):  [Read-Write] * Max LOD that this node is allowed to run
* For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
* when the component LOD becomes 3, it will stop update/evaluate
* currently transition would be issue and that has to be re-visited

<a id="unreal.AnimNode_SkeletalControlBase.lod_threshold"></a>

#### lod_threshold

```python
@lod_threshold.setter
def lod_threshold(value: int) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_input_type"></a>

#### alpha_input_type

```python
@property
def alpha_input_type() -> AnimAlphaInputType
```

(AnimAlphaInputType):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_input_type"></a>

#### alpha_input_type

```python
@alpha_input_type.setter
def alpha_input_type(value: AnimAlphaInputType) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@property
def alpha_bool_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@alpha_bool_enabled.setter
def alpha_bool_enabled(value: bool) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] Current strength of the skeletal control

<a id="unreal.AnimNode_SkeletalControlBase.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@property
def alpha_bool_blend() -> InputAlphaBoolBlend
```

(InputAlphaBoolBlend):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@alpha_bool_blend.setter
def alpha_bool_blend(value: InputAlphaBoolBlend) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_curve_name"></a>

#### alpha_curve_name

```python
@property
def alpha_curve_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_curve_name"></a>

#### alpha_curve_name

```python
@alpha_curve_name.setter
def alpha_curve_name(value: Name) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@property
def alpha_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_SkeletalControlBase.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@alpha_scale_bias_clamp.setter
def alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.InputScaleBiasClamp"></a>