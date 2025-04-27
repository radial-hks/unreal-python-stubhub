## InputModifierScalar Objects

```python
class InputModifierScalar(InputModifier)
```

Scalar
Scales input by a set factor per axis

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scalar`` (Vector):  [Read-Write] The scalar that will be applied to the input value.

  For example, if you have a scalar of (2.0, 2.0, 2.0), each input axis will be multiplied by 2.0.

  Note: This will do nothing on boolean input action types, as they can only be true or false.

<a id="unreal.InputModifierScalar.scalar"></a>

#### scalar

```python
@property
def scalar() -> Vector
```

(Vector):  [Read-Write] The scalar that will be applied to the input value.

For example, if you have a scalar of (2.0, 2.0, 2.0), each input axis will be multiplied by 2.0.

Note: This will do nothing on boolean input action types, as they can only be true or false.

<a id="unreal.InputModifierScalar.scalar"></a>

#### scalar

```python
@scalar.setter
def scalar(value: Vector) -> None
```

<a id="unreal.InputModifierScaleByDeltaTime"></a>