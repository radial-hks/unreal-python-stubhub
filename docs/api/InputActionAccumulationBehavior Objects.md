## InputActionAccumulationBehavior Objects

```python
class InputActionAccumulationBehavior(EnumBase)
```

This is an advanced setting that allows you to change how the value of an Input Action is calculated when there are
multiple mappings to the same Input Action. The default behavior is to accept highest absolute value.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputAction.h

<a id="unreal.InputActionAccumulationBehavior.TAKE_HIGHEST_ABSOLUTE_VALUE"></a>

#### TAKE_HIGHEST_ABSOLUTE_VALUE

0: Take the value from the mapping with the highest Absolute Value.

For example, given a value of -0.3 and 0.5, the input action's value would be 0.5.

<a id="unreal.InputActionAccumulationBehavior.CUMULATIVE"></a>

#### CUMULATIVE

1: Cumulatively adds the key values for each mapping.

For example, a value of -0.7 and +0.75 on the same input action would result in a value of 0.05.

A practical example of when to use this would be for something like WASD movement, if you want pressing W and S to cancel each other out.

<a id="unreal.NormalizeInputSmoothingType"></a>