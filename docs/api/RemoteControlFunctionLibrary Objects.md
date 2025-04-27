## RemoteControlFunctionLibrary Objects

```python
class RemoteControlFunctionLibrary(BlueprintFunctionLibrary)
```

Remote Control Function Library

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlFunctionLibrary.h

<a id="unreal.RemoteControlFunctionLibrary.expose_property"></a>

#### expose_property

```python
@classmethod
def expose_property(cls, preset: RemoteControlPreset, source_object: Object,
                    property_: str,
                    args: RemoteControlOptionalExposeArgs) -> bool
```

X.expose_property(preset, source_object, property_, args) -> bool
Expose a property in a remote control preset.

Args:
    preset (RemoteControlPreset): the preset to expose the property in.
    source_object (Object): the object that contains the property to expose.
    property_ (str): the name or path of the property to expose.
    args (RemoteControlOptionalExposeArgs): optional arguments.

Returns:
    bool: Whether the operation was successful.

<a id="unreal.RemoteControlFunctionLibrary.expose_function"></a>

#### expose_function

```python
@classmethod
def expose_function(cls, preset: RemoteControlPreset, source_object: Object,
                    function: str,
                    args: RemoteControlOptionalExposeArgs) -> bool
```

X.expose_function(preset, source_object, function, args) -> bool
Expose a function in a remote control preset.

Args:
    preset (RemoteControlPreset): the preset to expose the property in.
    source_object (Object): the object that contains the property to expose.
    function (str): the name of the function to expose.
    args (RemoteControlOptionalExposeArgs): optional arguments.

Returns:
    bool: Whether the operation was successful.

<a id="unreal.RemoteControlFunctionLibrary.expose_actor"></a>

#### expose_actor

```python
@classmethod
def expose_actor(cls, preset: RemoteControlPreset, actor: Actor,
                 args: RemoteControlOptionalExposeArgs) -> bool
```

X.expose_actor(preset, actor, args) -> bool
Expose an actor in a remote control preset.

Args:
    preset (RemoteControlPreset): the preset to expose the property in.
    actor (Actor): the actor to expose.
    args (RemoteControlOptionalExposeArgs): optional arguments.

Returns:
    bool: Whether the operation was successful.

<a id="unreal.RemoteControlFunctionLibrary.apply_color_wheel_delta"></a>

#### apply_color_wheel_delta

```python
@classmethod
def apply_color_wheel_delta(cls, target_object: Object, property_name: str,
                            delta_value: ColorWheelColor,
                            reference_color: ColorWheelColor,
                            is_interactive: bool) -> bool
```

X.apply_color_wheel_delta(target_object, property_name, delta_value, reference_color, is_interactive) -> bool
Add/subtract from the value of an FLinearColor property using a delta value based on color wheel coordinates.

Args:
    target_object (Object): the object that contains the property to modify.
    property_name (str): the name of the property to modify.
    delta_value (ColorWheelColor): the amount to change the color by.
    reference_color (ColorWheelColor): if the color's current position on the wheel is ambiguous as calculated from RGB values (e.g. black), use this reference color's position instead.
    is_interactive (bool): if true, this is treated as an interactive change. If false, it will be treated as the final value set change.

Returns:
    bool: Whether the operation was successful.

<a id="unreal.RemoteControlFunctionLibrary.apply_color_grading_wheel_delta"></a>

#### apply_color_grading_wheel_delta

```python
@classmethod
def apply_color_grading_wheel_delta(cls,
                                    target_object: Object,
                                    property_name: str,
                                    delta_value: ColorGradingWheelColor,
                                    reference_color: ColorGradingWheelColor,
                                    is_interactive: bool,
                                    min_value: float = 0.000000,
                                    max_value: float = 2.000000) -> bool
```

X.apply_color_grading_wheel_delta(target_object, property_name, delta_value, reference_color, is_interactive, min_value=0.000000, max_value=2.000000) -> bool
Add/subtract from the value of an FVector4 property interpreted as RGBV using a delta value based on color wheel coordinates.

Args:
    target_object (Object): the object that contains the property to modify.
    property_name (str): the name of the property to modify.
    delta_value (ColorGradingWheelColor): the amount to change the color by.
    reference_color (ColorGradingWheelColor): if the color's current position on the wheel is ambiguous as calculated from RGB values (e.g. black), use this reference color's position instead.
    is_interactive (bool): if true, this is treated as an interactive change. If false, it will be treated as the final value set change.
    min_value (float): 
    max_value (float): 

Returns:
    bool: Whether the operation was successful.

<a id="unreal.RemoteControlInterceptionTestObject"></a>