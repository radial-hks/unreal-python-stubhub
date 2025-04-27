## AnimationNode_TwoWayBlend Objects

```python
class AnimationNode_TwoWayBlend(AnimNode_TwoWayBlend)
```

deprecated: 'AnimationNode_TwoWayBlend' was renamed to 'AnimNode_TwoWayBlend'.

<a id="unreal.AnimationNode_TwoWayBlend.__init__"></a>

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

<a id="unreal.BlendListBaseReference"></a>