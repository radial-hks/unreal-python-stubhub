## AnimNode_TwoWayBlend Objects

```python
class AnimNode_TwoWayBlend(AnimNode_Base)
```

This represents a baked transition

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_TwoWayBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (PoseLink):  [Read-Write]
- ``alpha`` (float):  [Read-Write] The float value that controls the alpha blending when the alpha input type is set to 'Float'
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write] The boolean value that controls the alpha blending when the alpha input type is set to 'Bool'
- ``alpha_curve_name`` (Name):  [Read-Write] The animation curve that controls the alpha blending when the alpha input type is set to 'Curve'
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write] The data type used to control the alpha blending between the A and B poses.
                Note: Changing this value will disconnect alpha input pins.
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``always_update_children`` (bool):  [Read-Write] Always update children, regardless of whether or not that child has weight.
- ``b`` (PoseLink):  [Read-Write]
- ``reset_child_on_activation`` (bool):  [Read-Write] This reinitializes child pose when re-activated. For example, when active child changes

<a id="unreal.AnimNode_TwoWayBlend.__init__"></a>

#### __init__

```python
def __init__(
    a: PoseLink = [],
    b: PoseLink = [],
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

<a id="unreal.AnimNode_TwoWayBlend.a"></a>

#### a

```python
@property
def a() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_TwoWayBlend.a"></a>

#### a

```python
@a.setter
def a(value: PoseLink) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.b"></a>

#### b

```python
@property
def b() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_TwoWayBlend.b"></a>

#### b

```python
@b.setter
def b(value: PoseLink) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_input_type"></a>

#### alpha_input_type

```python
@property
def alpha_input_type() -> AnimAlphaInputType
```

(AnimAlphaInputType):  [Read-Write] The data type used to control the alpha blending between the A and B poses.
              Note: Changing this value will disconnect alpha input pins.

<a id="unreal.AnimNode_TwoWayBlend.alpha_input_type"></a>

#### alpha_input_type

```python
@alpha_input_type.setter
def alpha_input_type(value: AnimAlphaInputType) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@property
def alpha_bool_enabled() -> bool
```

(bool):  [Read-Write] The boolean value that controls the alpha blending when the alpha input type is set to 'Bool'

<a id="unreal.AnimNode_TwoWayBlend.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@alpha_bool_enabled.setter
def alpha_bool_enabled(value: bool) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] The float value that controls the alpha blending when the alpha input type is set to 'Float'

<a id="unreal.AnimNode_TwoWayBlend.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_TwoWayBlend.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@property
def alpha_bool_blend() -> InputAlphaBoolBlend
```

(InputAlphaBoolBlend):  [Read-Write]

<a id="unreal.AnimNode_TwoWayBlend.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@alpha_bool_blend.setter
def alpha_bool_blend(value: InputAlphaBoolBlend) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_curve_name"></a>

#### alpha_curve_name

```python
@property
def alpha_curve_name() -> Name
```

(Name):  [Read-Write] The animation curve that controls the alpha blending when the alpha input type is set to 'Curve'

<a id="unreal.AnimNode_TwoWayBlend.alpha_curve_name"></a>

#### alpha_curve_name

```python
@alpha_curve_name.setter
def alpha_curve_name(value: Name) -> None
```

<a id="unreal.AnimNode_TwoWayBlend.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@property
def alpha_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_TwoWayBlend.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@alpha_scale_bias_clamp.setter
def alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.AnimationNode_TwoWayBlend"></a>