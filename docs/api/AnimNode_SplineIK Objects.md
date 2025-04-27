## AnimNode_SplineIK Objects

```python
class AnimNode_SplineIK(AnimNode_SkeletalControlBase)
```

Anim Node Spline IK

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_SplineIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``auto_calculate_spline`` (bool):  [Read-Write] The number of points in the spline if we are specifying it directly
- ``bone_axis`` (SplineBoneAxis):  [Read-Write] Axis of the controlled bone (ie the direction of the spline) to use as the direction for the curve.
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``control_points`` (Array[Transform]):  [Read-Write] Transforms applied to spline points *
- ``end_bone`` (BoneReference):  [Read-Write] Name of bone at the end of the spline chain. Bones after this will not be altered by the controller.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``offset`` (float):  [Read-Write] The distance along the spline from the start from which bones are constrained
- ``point_count`` (int32):  [Read-Write] The number of points in the spline if we are not auto-calculating
- ``roll`` (float):  [Read-Write] Overall roll of the spline, applied on top of other rotations along the direction of the spline
- ``start_bone`` (BoneReference):  [Read-Write] Name of root bone from which the spline extends *
- ``stretch`` (float):  [Read-Write] The maximum stretch allowed when fitting bones to the spline. 0.0 means bones do not stretch their length,
  1.0 means bones stretch to the length of the spline
- ``twist_blend`` (AlphaBlend):  [Read-Write] How to interpolate twist along the length of the spline
- ``twist_end`` (float):  [Read-Write] The twist of the end bone. Twist is interpolated along the spline according to Twist Blend.
- ``twist_start`` (float):  [Read-Write] The twist of the start bone. Twist is interpolated along the spline according to Twist Blend.

<a id="unreal.AnimNode_SplineIK.__init__"></a>

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
             control_points: Array[Transform] = [],
             roll: float = 0.000000,
             twist_start: float = 0.000000,
             twist_end: float = 0.000000,
             stretch: float = 0.000000,
             offset: float = 0.000000) -> None
```

<a id="unreal.AnimNode_SplineIK.control_points"></a>

#### control_points

```python
@property
def control_points() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] Transforms applied to spline points *

<a id="unreal.AnimNode_SplineIK.control_points"></a>

#### control_points

```python
@control_points.setter
def control_points(value: Array[Transform]) -> None
```

<a id="unreal.AnimNode_SplineIK.roll"></a>

#### roll

```python
@property
def roll() -> float
```

(float):  [Read-Write] Overall roll of the spline, applied on top of other rotations along the direction of the spline

<a id="unreal.AnimNode_SplineIK.roll"></a>

#### roll

```python
@roll.setter
def roll(value: float) -> None
```

<a id="unreal.AnimNode_SplineIK.twist_start"></a>

#### twist_start

```python
@property
def twist_start() -> float
```

(float):  [Read-Write] The twist of the start bone. Twist is interpolated along the spline according to Twist Blend.

<a id="unreal.AnimNode_SplineIK.twist_start"></a>

#### twist_start

```python
@twist_start.setter
def twist_start(value: float) -> None
```

<a id="unreal.AnimNode_SplineIK.twist_end"></a>

#### twist_end

```python
@property
def twist_end() -> float
```

(float):  [Read-Write] The twist of the end bone. Twist is interpolated along the spline according to Twist Blend.

<a id="unreal.AnimNode_SplineIK.twist_end"></a>

#### twist_end

```python
@twist_end.setter
def twist_end(value: float) -> None
```

<a id="unreal.AnimNode_SplineIK.stretch"></a>

#### stretch

```python
@property
def stretch() -> float
```

(float):  [Read-Write] The maximum stretch allowed when fitting bones to the spline. 0.0 means bones do not stretch their length,
1.0 means bones stretch to the length of the spline

<a id="unreal.AnimNode_SplineIK.stretch"></a>

#### stretch

```python
@stretch.setter
def stretch(value: float) -> None
```

<a id="unreal.AnimNode_SplineIK.offset"></a>

#### offset

```python
@property
def offset() -> float
```

(float):  [Read-Write] The distance along the spline from the start from which bones are constrained

<a id="unreal.AnimNode_SplineIK.offset"></a>

#### offset

```python
@offset.setter
def offset(value: float) -> None
```

<a id="unreal.AnimNode_SpringBone"></a>