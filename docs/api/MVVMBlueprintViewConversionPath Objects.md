## MVVMBlueprintViewConversionPath Objects

```python
class MVVMBlueprintViewConversionPath(StructBase)
```

MVVMBlueprint View Conversion Path

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destination_to_source_conversion`` (MVVMBlueprintViewConversionFunction):  [Read-Only] The graph that contains the conversion function when converting the value from the destination to the source.
  When the function doesn't need a wrapper.
- ``source_to_destination_conversion`` (MVVMBlueprintViewConversionFunction):  [Read-Only] The graph that contains the conversion function when converting the value from the source to the destination.
  When the function doesn't need a wrapper.

<a id="unreal.MVVMBlueprintViewConversionPath.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMBlueprintViewBinding"></a>