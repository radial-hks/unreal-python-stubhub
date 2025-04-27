## InputModifierSmoothDelta Objects

```python
class InputModifierSmoothDelta(InputModifier)
```

Normalized Smooth Delta

Produces a smoothed normalized delta of the current(new) and last(old) input value.
Boolean input values will be returned as is.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing_exponent`` (float):  [Read-Write] For ease functions, this controls the degree of the curve.

  This only affects the Interp_Ease_In, Interp_Ease_Out, and Interp_Ease_In_Out smoothing methods
- ``smoothing_method`` (NormalizeInputSmoothingType):  [Read-Write]
- ``speed`` (float):  [Read-Write] Speed, or Alpha. If the speed given is 0, then jump to the target.

<a id="unreal.InputModifierSmoothDelta.smoothing_method"></a>

#### smoothing_method

```python
@property
def smoothing_method() -> NormalizeInputSmoothingType
```

(NormalizeInputSmoothingType):  [Read-Write]

<a id="unreal.InputModifierSmoothDelta.smoothing_method"></a>

#### smoothing_method

```python
@smoothing_method.setter
def smoothing_method(value: NormalizeInputSmoothingType) -> None
```

<a id="unreal.InputModifierSmoothDelta.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write] Speed, or Alpha. If the speed given is 0, then jump to the target.

<a id="unreal.InputModifierSmoothDelta.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.InputModifierSmoothDelta.easing_exponent"></a>

#### easing_exponent

```python
@property
def easing_exponent() -> float
```

(float):  [Read-Write] For ease functions, this controls the degree of the curve.

This only affects the Interp_Ease_In, Interp_Ease_Out, and Interp_Ease_In_Out smoothing methods

<a id="unreal.InputModifierSmoothDelta.easing_exponent"></a>

#### easing_exponent

```python
@easing_exponent.setter
def easing_exponent(value: float) -> None
```

<a id="unreal.InputModifierDeadZone"></a>