## AnimNode_CopyBoneDelta Objects

```python
class AnimNode_CopyBoneDelta(AnimNode_SkeletalControlBase)
```

Simple controller to copy a transform relative to the ref pose to the target bone,
instead of the copy bone node which copies the absolute transform

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_CopyBoneDelta.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``copy_mode`` (CopyBoneDeltaMode):  [Read-Write]
- ``copy_rotation`` (bool):  [Read-Write]
- ``copy_scale`` (bool):  [Read-Write]
- ``copy_translation`` (bool):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``rotation_multiplier`` (float):  [Read-Write]
- ``scale_multiplier`` (float):  [Read-Write]
- ``source_bone`` (BoneReference):  [Read-Write]
- ``target_bone`` (BoneReference):  [Read-Write]
- ``translation_multiplier`` (float):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.__init__"></a>

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
             copy_translation: bool = False,
             copy_rotation: bool = False,
             copy_scale: bool = False,
             translation_multiplier: float = 0.000000,
             rotation_multiplier: float = 0.000000,
             scale_multiplier: float = 0.000000) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.copy_translation"></a>

#### copy_translation

```python
@property
def copy_translation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.copy_translation"></a>

#### copy_translation

```python
@copy_translation.setter
def copy_translation(value: bool) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.copy_rotation"></a>

#### copy_rotation

```python
@property
def copy_rotation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.copy_rotation"></a>

#### copy_rotation

```python
@copy_rotation.setter
def copy_rotation(value: bool) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.copy_scale"></a>

#### copy_scale

```python
@property
def copy_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.copy_scale"></a>

#### copy_scale

```python
@copy_scale.setter
def copy_scale(value: bool) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.translation_multiplier"></a>

#### translation_multiplier

```python
@property
def translation_multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.translation_multiplier"></a>

#### translation_multiplier

```python
@translation_multiplier.setter
def translation_multiplier(value: float) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.rotation_multiplier"></a>

#### rotation_multiplier

```python
@property
def rotation_multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.rotation_multiplier"></a>

#### rotation_multiplier

```python
@rotation_multiplier.setter
def rotation_multiplier(value: float) -> None
```

<a id="unreal.AnimNode_CopyBoneDelta.scale_multiplier"></a>

#### scale_multiplier

```python
@property
def scale_multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_CopyBoneDelta.scale_multiplier"></a>

#### scale_multiplier

```python
@scale_multiplier.setter
def scale_multiplier(value: float) -> None
```

<a id="unreal.AnimNode_Fabrik"></a>