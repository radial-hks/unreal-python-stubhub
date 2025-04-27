## InputModifier Objects

```python
class InputModifier(Object)
```

Base class for building modifiers.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputModifiers.h

<a id="unreal.InputModifier.modify_raw"></a>

#### modify_raw

```python
def modify_raw(player_input: EnhancedPlayerInput,
               current_value: InputActionValue,
               delta_time: float) -> InputActionValue
```

x.modify_raw(player_input, current_value, delta_time) -> InputActionValue
ModifyRaw
Will be called by each modifier in the modifier chain

Args:
    player_input (EnhancedPlayerInput): 
    current_value (InputActionValue): The modified value returned by the previous modifier in the chain, or the base raw value if this is the first modifier in the chain.
    delta_time (float): 

Returns:
    InputActionValue:

<a id="unreal.InputModifier.get_visualization_color"></a>

#### get_visualization_color

```python
def get_visualization_color(sample_value: InputActionValue,
                            final_value: InputActionValue) -> LinearColor
```

x.get_visualization_color(sample_value, final_value) -> LinearColor
Helper to allow debug visualization of the modifier.

Args:
    sample_value (InputActionValue): The base input action value pre-modification (ranging -1 -> 1 across all applicable axes).
    final_value (InputActionValue): The post-modification input action value for the provided SampleValue.

Returns:
    LinearColor:

<a id="unreal.InputModifierSmoothDelta"></a>