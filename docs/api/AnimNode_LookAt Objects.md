## AnimNode_LookAt Objects

```python
class AnimNode_LookAt(AnimNode_SkeletalControlBase)
```

Simple controller that make a bone to look at the point or another bone

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_LookAt.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``bone_to_modify`` (BoneReference):  [Read-Write] Name of bone to control. This is the main bone chain to modify from. *
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``interpolation_time`` (float):  [Read-Write]
- ``interpolation_trigger_threashold`` (float):  [Read-Write]
- ``interpolation_type`` (InterpolationBlend):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``look_at_axis`` (Axis):  [Read-Write]
- ``look_at_clamp`` (float):  [Read-Write] Look at Clamp value in degrees - if your look at axis is Z, only X, Y degree of clamp will be used
- ``look_at_location`` (Vector):  [Read-Write] Target Offset. It's in world space if LookAtBone is empty or it is based on LookAtBone or LookAtSocket in their local space
- ``look_at_target`` (BoneSocketTarget):  [Read-Write] Target socket to look at. Used if LookAtBone is empty. - You can use  LookAtLocation if you need offset from this point. That location will be used in their local space. *
- ``look_up_axis`` (Axis):  [Read-Write]
- ``use_look_up_axis`` (bool):  [Read-Write] Whether or not to use Look up axis

<a id="unreal.AnimNode_LookAt.__init__"></a>

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
        ],
        look_at_location: Vector = [0.000000, 0.000000, 0.000000],
        interpolation_type: InterpolationBlend = InterpolationBlend.LINEAR,
        look_at_clamp: float = 0.000000,
        interpolation_time: float = 0.000000,
        interpolation_trigger_threashold: float = 0.000000) -> None
```

<a id="unreal.AnimNode_LookAt.look_at_location"></a>

#### look_at_location

```python
@property
def look_at_location() -> Vector
```

(Vector):  [Read-Write] Target Offset. It's in world space if LookAtBone is empty or it is based on LookAtBone or LookAtSocket in their local space

<a id="unreal.AnimNode_LookAt.look_at_location"></a>

#### look_at_location

```python
@look_at_location.setter
def look_at_location(value: Vector) -> None
```

<a id="unreal.AnimNode_LookAt.interpolation_type"></a>

#### interpolation_type

```python
@property
def interpolation_type() -> InterpolationBlend
```

(InterpolationBlend):  [Read-Write]

<a id="unreal.AnimNode_LookAt.interpolation_type"></a>

#### interpolation_type

```python
@interpolation_type.setter
def interpolation_type(value: InterpolationBlend) -> None
```

<a id="unreal.AnimNode_LookAt.look_at_clamp"></a>

#### look_at_clamp

```python
@property
def look_at_clamp() -> float
```

(float):  [Read-Write] Look at Clamp value in degrees - if your look at axis is Z, only X, Y degree of clamp will be used

<a id="unreal.AnimNode_LookAt.look_at_clamp"></a>

#### look_at_clamp

```python
@look_at_clamp.setter
def look_at_clamp(value: float) -> None
```

<a id="unreal.AnimNode_LookAt.interpolation_time"></a>

#### interpolation_time

```python
@property
def interpolation_time() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_LookAt.interpolation_time"></a>

#### interpolation_time

```python
@interpolation_time.setter
def interpolation_time(value: float) -> None
```

<a id="unreal.AnimNode_LookAt.interpolation_trigger_threashold"></a>

#### interpolation_trigger_threashold

```python
@property
def interpolation_trigger_threashold() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_LookAt.interpolation_trigger_threashold"></a>

#### interpolation_trigger_threashold

```python
@interpolation_trigger_threashold.setter
def interpolation_trigger_threashold(value: float) -> None
```

<a id="unreal.AnimNode_ObserveBone"></a>