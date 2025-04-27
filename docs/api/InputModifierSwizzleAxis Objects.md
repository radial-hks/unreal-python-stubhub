## InputModifierSwizzleAxis Objects

```python
class InputModifierSwizzleAxis(InputModifier)
```

Swizzle axis components of an input value.
Useful to map a 1D input onto the Y axis of a 2D action.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``order`` (InputAxisSwizzle):  [Read-Write] Default to XY swap, useful for binding 1D inputs to the Y axis.

<a id="unreal.InputModifierSwizzleAxis.order"></a>

#### order

```python
@property
def order() -> InputAxisSwizzle
```

(InputAxisSwizzle):  [Read-Write] Default to XY swap, useful for binding 1D inputs to the Y axis.

<a id="unreal.InputModifierSwizzleAxis.order"></a>

#### order

```python
@order.setter
def order(value: InputAxisSwizzle) -> None
```

<a id="unreal.InputTrigger"></a>