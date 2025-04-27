## InterchangeTestFunction Objects

```python
class InterchangeTestFunction(StructBase)
```

Interchange Test Function

**C++ Source:**

- **Plugin**: InterchangeTests
- **Module**: InterchangeTests
- **File**: InterchangeTestFunction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_class`` (type(Class)):  [Read-Write] Type of the asset being tested
- ``check_function`` (Function):  [Read-Write] A function to be called to determine whether the result is correct
- ``optional_asset_name`` (str):  [Read-Write] Optional name of the asset to test, if there are various contenders
- ``parameters`` (Map[Name, str]):  [Read-Write] Parameters and their bound values as text

<a id="unreal.InterchangeTestFunction.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ImgMediaSourceCustomizationSequenceProxy"></a>