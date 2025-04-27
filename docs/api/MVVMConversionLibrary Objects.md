## MVVMConversionLibrary Objects

```python
class MVVMConversionLibrary(BlueprintFunctionLibrary)
```

MVVMConversion Library

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMConversionLibrary.h

<a id="unreal.MVVMConversionLibrary.conv_bool_to_slate_visibility"></a>

#### conv_bool_to_slate_visibility

```python
@classmethod
def conv_bool_to_slate_visibility(
    cls,
    is_visible: bool,
    true_visibility: SlateVisibility = SlateVisibility.VISIBLE,
    false_visibility: SlateVisibility = SlateVisibility.COLLAPSED
) -> SlateVisibility
```

X.conv_bool_to_slate_visibility(is_visible, true_visibility=SlateVisibility.VISIBLE, false_visibility=SlateVisibility.COLLAPSED) -> SlateVisibility
Converts a bool to a slate visibility.

Args:
    is_visible (bool): 
    true_visibility (SlateVisibility): 
    false_visibility (SlateVisibility): 

Returns:
    SlateVisibility:

<a id="unreal.MVVMSlateBrushConversionLibrary"></a>