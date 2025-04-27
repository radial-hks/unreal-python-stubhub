## AnimNode_IKRig Objects

```python
class AnimNode_IKRig(AnimNode_CustomProperty)
```

Anim Node IKRig

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: AnimNode_IKRig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write] alpha value handler *
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``debug_scale`` (float):  [Read-Write] Adjust size of debug drawing.
- ``enable_debug_draw`` (bool):  [Read-Write] Toggle debug drawing of goals when node is selected.
- ``goals`` (Array[IKRigGoal]):  [Read-Write] The input goal transforms used by the IK Rig solvers.
- ``rig_definition_asset`` (IKRigDefinition):  [Read-Write] The IK rig to use to modify the incoming source pose.
- ``source`` (PoseLink):  [Read-Write] The input pose to start the IK solve relative to.
- ``start_from_ref_pose`` (bool):  [Read-Write] optionally ignore the input pose and start from the reference pose each solve

<a id="unreal.AnimNode_IKRig.__init__"></a>

#### __init__

```python
def __init__(
    goals: Array[IKRigGoal] = [],
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

<a id="unreal.AnimNode_IKRig.goals"></a>

#### goals

```python
@property
def goals() -> Array[IKRigGoal]
```

(Array[IKRigGoal]):  [Read-Write] The input goal transforms used by the IK Rig solvers.

<a id="unreal.AnimNode_IKRig.goals"></a>

#### goals

```python
@goals.setter
def goals(value: Array[IKRigGoal]) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_input_type"></a>

#### alpha_input_type

```python
@property
def alpha_input_type() -> AnimAlphaInputType
```

(AnimAlphaInputType):  [Read-Write] alpha value handler *

<a id="unreal.AnimNode_IKRig.alpha_input_type"></a>

#### alpha_input_type

```python
@alpha_input_type.setter
def alpha_input_type(value: AnimAlphaInputType) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@property
def alpha_bool_enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_IKRig.alpha_bool_enabled"></a>

#### alpha_bool_enabled

```python
@alpha_bool_enabled.setter
def alpha_bool_enabled(value: bool) -> None
```

<a id="unreal.AnimNode_IKRig.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] Current strength of the skeletal control

<a id="unreal.AnimNode_IKRig.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_IKRig.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@property
def alpha_bool_blend() -> InputAlphaBoolBlend
```

(InputAlphaBoolBlend):  [Read-Write]

<a id="unreal.AnimNode_IKRig.alpha_bool_blend"></a>

#### alpha_bool_blend

```python
@alpha_bool_blend.setter
def alpha_bool_blend(value: InputAlphaBoolBlend) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_curve_name"></a>

#### alpha_curve_name

```python
@property
def alpha_curve_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AnimNode_IKRig.alpha_curve_name"></a>

#### alpha_curve_name

```python
@alpha_curve_name.setter
def alpha_curve_name(value: Name) -> None
```

<a id="unreal.AnimNode_IKRig.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@property
def alpha_scale_bias_clamp() -> InputScaleBiasClamp
```

(InputScaleBiasClamp):  [Read-Write]

<a id="unreal.AnimNode_IKRig.alpha_scale_bias_clamp"></a>

#### alpha_scale_bias_clamp

```python
@alpha_scale_bias_clamp.setter
def alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

<a id="unreal.IKRigGoal"></a>