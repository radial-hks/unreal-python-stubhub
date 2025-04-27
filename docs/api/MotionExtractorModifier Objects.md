## MotionExtractorModifier Objects

```python
class MotionExtractorModifier(AnimationModifier)
```

Extracts motion from a bone in the animation and bakes it into a curve

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: MotionExtractorModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_value`` (bool):  [Read-Write] Whether to convert the final value to absolute (positive)
- ``axis`` (MotionExtractor_Axis):  [Read-Write] Axis to get the value from
- ``bone_name`` (Name):  [Read-Write] Bone we are going to generate the curve from
- ``custom_curve_name`` (Name):  [Read-Write] Custom name for the curve we are going to generate.
- ``math_operation`` (MotionExtractor_MathOperation):  [Read-Write] Optional math operation to apply on the extracted value before add it to the generated curve
- ``modifier`` (float):  [Read-Write] Right operand for the math operation selected
- ``motion_type`` (MotionExtractor_MotionType):  [Read-Write] Type of motion to extract
- ``normalize`` (bool):  [Read-Write] Whether we want a normalized value (0 - 1)
- ``reapply_post_owner_change`` (bool):  [Read-Write] If this is set to true then the animation modifier will call it's reapply function after any change made to the owning asset.
- ``relative_to_bone_name`` (Name):  [Read-Write] Bone which we'll use as the reference frame to generate this curve from. Space must be RelativeToBone to use this.
- ``relative_to_first_frame`` (bool):  [Read-Write] Whether to extract the bone transforms relative to the first frame in the animation
- ``remove_curve_on_revert`` (bool):  [Read-Write] Whether we want to remove the curve when we revert or re-apply modifier
                Disabling this allows you to modify settings and create a new curve each time you re-apply the modifier
                Enabling this is the preferred setting when using a modifier that's applied in bulk and you may want to remove/rename curves
- ``sample_rate`` (int32):  [Read-Write] Rate used to sample the animation
- ``space`` (MotionExtractor_Space):  [Read-Write] Reference frame/space to use when extracting the bone pose.
- ``use_custom_curve_name`` (bool):  [Read-Write] Whether we want to specify a custom name for the curve. If false, the name of the curve will be auto generated based on the data we are going to extract

<a id="unreal.MotionExtractorModifier.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Write] Bone we are going to generate the curve from

<a id="unreal.MotionExtractorModifier.bone_name"></a>

#### bone_name

```python
@bone_name.setter
def bone_name(value: Name) -> None
```

<a id="unreal.MotionExtractorModifier.relative_to_bone_name"></a>

#### relative_to_bone_name

```python
@property
def relative_to_bone_name() -> Name
```

(Name):  [Read-Write] Bone which we'll use as the reference frame to generate this curve from. Space must be RelativeToBone to use this.

<a id="unreal.MotionExtractorModifier.relative_to_bone_name"></a>

#### relative_to_bone_name

```python
@relative_to_bone_name.setter
def relative_to_bone_name(value: Name) -> None
```

<a id="unreal.MotionExtractorModifier.motion_type"></a>

#### motion_type

```python
@property
def motion_type() -> MotionExtractor_MotionType
```

(MotionExtractor_MotionType):  [Read-Write] Type of motion to extract

<a id="unreal.MotionExtractorModifier.motion_type"></a>

#### motion_type

```python
@motion_type.setter
def motion_type(value: MotionExtractor_MotionType) -> None
```

<a id="unreal.MotionExtractorModifier.axis"></a>

#### axis

```python
@property
def axis() -> MotionExtractor_Axis
```

(MotionExtractor_Axis):  [Read-Write] Axis to get the value from

<a id="unreal.MotionExtractorModifier.axis"></a>

#### axis

```python
@axis.setter
def axis(value: MotionExtractor_Axis) -> None
```

<a id="unreal.MotionExtractorModifier.remove_curve_on_revert"></a>

#### remove_curve_on_revert

```python
@property
def remove_curve_on_revert() -> bool
```

(bool):  [Read-Write] Whether we want to remove the curve when we revert or re-apply modifier
              Disabling this allows you to modify settings and create a new curve each time you re-apply the modifier
              Enabling this is the preferred setting when using a modifier that's applied in bulk and you may want to remove/rename curves

<a id="unreal.MotionExtractorModifier.remove_curve_on_revert"></a>

#### remove_curve_on_revert

```python
@remove_curve_on_revert.setter
def remove_curve_on_revert(value: bool) -> None
```

<a id="unreal.MotionExtractorModifier.relative_to_first_frame"></a>

#### relative_to_first_frame

```python
@property
def relative_to_first_frame() -> bool
```

(bool):  [Read-Write] Whether to extract the bone transforms relative to the first frame in the animation

<a id="unreal.MotionExtractorModifier.relative_to_first_frame"></a>

#### relative_to_first_frame

```python
@relative_to_first_frame.setter
def relative_to_first_frame(value: bool) -> None
```

<a id="unreal.MotionExtractorModifier.space"></a>

#### space

```python
@property
def space() -> MotionExtractor_Space
```

(MotionExtractor_Space):  [Read-Write] Reference frame/space to use when extracting the bone pose.

<a id="unreal.MotionExtractorModifier.space"></a>

#### space

```python
@space.setter
def space(value: MotionExtractor_Space) -> None
```

<a id="unreal.MotionExtractorModifier.absolute_value"></a>

#### absolute_value

```python
@property
def absolute_value() -> bool
```

(bool):  [Read-Write] Whether to convert the final value to absolute (positive)

<a id="unreal.MotionExtractorModifier.absolute_value"></a>

#### absolute_value

```python
@absolute_value.setter
def absolute_value(value: bool) -> None
```

<a id="unreal.MotionExtractorModifier.math_operation"></a>

#### math_operation

```python
@property
def math_operation() -> MotionExtractor_MathOperation
```

(MotionExtractor_MathOperation):  [Read-Write] Optional math operation to apply on the extracted value before add it to the generated curve

<a id="unreal.MotionExtractorModifier.math_operation"></a>

#### math_operation

```python
@math_operation.setter
def math_operation(value: MotionExtractor_MathOperation) -> None
```

<a id="unreal.MotionExtractorModifier.modifier"></a>

#### modifier

```python
@property
def modifier() -> float
```

(float):  [Read-Write] Right operand for the math operation selected

<a id="unreal.MotionExtractorModifier.modifier"></a>

#### modifier

```python
@modifier.setter
def modifier(value: float) -> None
```

<a id="unreal.MotionExtractorModifier.normalize"></a>

#### normalize

```python
@property
def normalize() -> bool
```

(bool):  [Read-Write] Whether we want a normalized value (0 - 1)

<a id="unreal.MotionExtractorModifier.normalize"></a>

#### normalize

```python
@normalize.setter
def normalize(value: bool) -> None
```

<a id="unreal.MotionExtractorModifier.use_custom_curve_name"></a>

#### use_custom_curve_name

```python
@property
def use_custom_curve_name() -> bool
```

(bool):  [Read-Write] Whether we want to specify a custom name for the curve. If false, the name of the curve will be auto generated based on the data we are going to extract

<a id="unreal.MotionExtractorModifier.use_custom_curve_name"></a>

#### use_custom_curve_name

```python
@use_custom_curve_name.setter
def use_custom_curve_name(value: bool) -> None
```

<a id="unreal.MotionExtractorModifier.custom_curve_name"></a>

#### custom_curve_name

```python
@property
def custom_curve_name() -> Name
```

(Name):  [Read-Write] Custom name for the curve we are going to generate.

<a id="unreal.MotionExtractorModifier.custom_curve_name"></a>

#### custom_curve_name

```python
@custom_curve_name.setter
def custom_curve_name(value: Name) -> None
```

<a id="unreal.AnimationCompressionLibraryDatabaseFactory"></a>