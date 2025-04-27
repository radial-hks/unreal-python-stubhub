## RemoteControlInterceptionTestObject Objects

```python
class RemoteControlInterceptionTestObject(Object)
```

Remote Control Interception Test Object

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlInterceptionTestData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_struct`` (RemoteControlInterceptionTestStruct):  [Read-Write]
- ``function_param_struct`` (RemoteControlInterceptionFunctionParamStruct):  [Read-Write]
- ``value_with_setter`` (str):  [Read-Write] Testing private property with a setter.

<a id="unreal.RemoteControlInterceptionTestObject.test_function"></a>

#### test_function

```python
def test_function(
        struct: RemoteControlInterceptionFunctionParamStruct,
        test_factor: int) -> RemoteControlInterceptionFunctionParamStruct
```

x.test_function(struct, test_factor) -> RemoteControlInterceptionFunctionParamStruct
Test Function

Args:
    struct (RemoteControlInterceptionFunctionParamStruct): 
    test_factor (int32): 

Returns:
    RemoteControlInterceptionFunctionParamStruct:

<a id="unreal.RemoteControlPreset"></a>