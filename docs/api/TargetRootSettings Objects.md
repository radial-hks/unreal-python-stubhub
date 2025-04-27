## TargetRootSettings Objects

```python
class TargetRootSettings(StructBase)
```

Target Root Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_ik_horizontal`` (float):  [Read-Write] Range 0 to 1. Default 1. Control whether modifications made to the root will affect the horizontal component of IK positions.
  At 0 the IK positions are independent of the root modifications.
  At 1 the IK positions are calculated relative to the modified root location.
- ``affect_ik_vertical`` (float):  [Read-Write] Range 0 to 1. Default 0. Control whether modifications made to the root will affect the vertical component of IK positions.
  At 0 the IK positions are independent of the root modifications.
  At 1 the IK positions are calculated relative to the modified root location.
- ``blend_to_source`` (float):  [Read-Write] Range 0 to 1. Default 0. Blends the retarget root's translation to the exact source location.
  At 0 the root is placed at the retargeted location.
  At 1 the root is placed at the location of the source's retarget root bone.
- ``blend_to_source_weights`` (Vector):  [Read-Write] Per-axis weights for the Blend to Source.
- ``rotation_alpha`` (float):  [Read-Write] Range 0 to 1. Default 1. Blends the amount of retargeted root rotation to apply.
  At 0 the root is left at the rotation from the retarget pose.
  At 1 the root is rotated fully to match the source root rotation.
- ``rotation_offset`` (Rotator):  [Read-Write] Applies a static local-space rotation offset to the retarget root.
- ``scale_horizontal`` (float):  [Read-Write] Default 1. Scales the motion of the root position in the horizontal plane (X,Y).
- ``scale_vertical`` (float):  [Read-Write] Default 1. Scales the motion of the root position in the vertical direction (Z).
- ``translation_alpha`` (float):  [Read-Write] Range 0 to 1. Default 1. Blends the amount of retargeted root translation to apply.
  At 0 the root is left at the position from the retarget pose.
  At 1 the root will follow the source motion according to the behavior defined in the subsequent settings.
- ``translation_offset`` (Vector):  [Read-Write] Applies a static component-space translation offset to the retarget root.

<a id="unreal.TargetRootSettings.__init__"></a>

#### __init__

```python
def __init__(rotation_alpha: float = 0.000000,
             translation_alpha: float = 0.000000,
             blend_to_source: float = 0.000000,
             blend_to_source_weights: Vector = [0.000000, 0.000000, 0.000000],
             scale_horizontal: float = 0.000000,
             scale_vertical: float = 0.000000,
             translation_offset: Vector = [0.000000, 0.000000, 0.000000],
             rotation_offset: Rotator = [0.000000, 0.000000, 0.000000],
             affect_ik_horizontal: float = 0.000000,
             affect_ik_vertical: float = 0.000000) -> None
```

<a id="unreal.TargetRootSettings.rotation_alpha"></a>

#### rotation_alpha

```python
@property
def rotation_alpha() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 1. Blends the amount of retargeted root rotation to apply.
At 0 the root is left at the rotation from the retarget pose.
At 1 the root is rotated fully to match the source root rotation.

<a id="unreal.TargetRootSettings.rotation_alpha"></a>

#### rotation_alpha

```python
@rotation_alpha.setter
def rotation_alpha(value: float) -> None
```

<a id="unreal.TargetRootSettings.translation_alpha"></a>

#### translation_alpha

```python
@property
def translation_alpha() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 1. Blends the amount of retargeted root translation to apply.
At 0 the root is left at the position from the retarget pose.
At 1 the root will follow the source motion according to the behavior defined in the subsequent settings.

<a id="unreal.TargetRootSettings.translation_alpha"></a>

#### translation_alpha

```python
@translation_alpha.setter
def translation_alpha(value: float) -> None
```

<a id="unreal.TargetRootSettings.blend_to_source"></a>

#### blend_to_source

```python
@property
def blend_to_source() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 0. Blends the retarget root's translation to the exact source location.
At 0 the root is placed at the retargeted location.
At 1 the root is placed at the location of the source's retarget root bone.

<a id="unreal.TargetRootSettings.blend_to_source"></a>

#### blend_to_source

```python
@blend_to_source.setter
def blend_to_source(value: float) -> None
```

<a id="unreal.TargetRootSettings.blend_to_source_weights"></a>

#### blend_to_source_weights

```python
@property
def blend_to_source_weights() -> Vector
```

(Vector):  [Read-Write] Per-axis weights for the Blend to Source.

<a id="unreal.TargetRootSettings.blend_to_source_weights"></a>

#### blend_to_source_weights

```python
@blend_to_source_weights.setter
def blend_to_source_weights(value: Vector) -> None
```

<a id="unreal.TargetRootSettings.scale_horizontal"></a>

#### scale_horizontal

```python
@property
def scale_horizontal() -> float
```

(float):  [Read-Write] Default 1. Scales the motion of the root position in the horizontal plane (X,Y).

<a id="unreal.TargetRootSettings.scale_horizontal"></a>

#### scale_horizontal

```python
@scale_horizontal.setter
def scale_horizontal(value: float) -> None
```

<a id="unreal.TargetRootSettings.scale_vertical"></a>

#### scale_vertical

```python
@property
def scale_vertical() -> float
```

(float):  [Read-Write] Default 1. Scales the motion of the root position in the vertical direction (Z).

<a id="unreal.TargetRootSettings.scale_vertical"></a>

#### scale_vertical

```python
@scale_vertical.setter
def scale_vertical(value: float) -> None
```

<a id="unreal.TargetRootSettings.translation_offset"></a>

#### translation_offset

```python
@property
def translation_offset() -> Vector
```

(Vector):  [Read-Write] Applies a static component-space translation offset to the retarget root.

<a id="unreal.TargetRootSettings.translation_offset"></a>

#### translation_offset

```python
@translation_offset.setter
def translation_offset(value: Vector) -> None
```

<a id="unreal.TargetRootSettings.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Rotator
```

(Rotator):  [Read-Write] Applies a static local-space rotation offset to the retarget root.

<a id="unreal.TargetRootSettings.rotation_offset"></a>

#### rotation_offset

```python
@rotation_offset.setter
def rotation_offset(value: Rotator) -> None
```

<a id="unreal.TargetRootSettings.affect_ik_horizontal"></a>

#### affect_ik_horizontal

```python
@property
def affect_ik_horizontal() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 1. Control whether modifications made to the root will affect the horizontal component of IK positions.
At 0 the IK positions are independent of the root modifications.
At 1 the IK positions are calculated relative to the modified root location.

<a id="unreal.TargetRootSettings.affect_ik_horizontal"></a>

#### affect_ik_horizontal

```python
@affect_ik_horizontal.setter
def affect_ik_horizontal(value: float) -> None
```

<a id="unreal.TargetRootSettings.affect_ik_vertical"></a>

#### affect_ik_vertical

```python
@property
def affect_ik_vertical() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 0. Control whether modifications made to the root will affect the vertical component of IK positions.
At 0 the IK positions are independent of the root modifications.
At 1 the IK positions are calculated relative to the modified root location.

<a id="unreal.TargetRootSettings.affect_ik_vertical"></a>

#### affect_ik_vertical

```python
@affect_ik_vertical.setter
def affect_ik_vertical(value: float) -> None
```

<a id="unreal.TargetChainSettings"></a>