## EnhancedInputPlatformData Objects

```python
class EnhancedInputPlatformData(Object)
```

A base class that can be used to store platform specific data for Enhanced Input.

Make a subclass of this to add some additional options for per-platform settings

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputPlatformSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mapping_context_redirects`` (Map[InputMappingContext, InputMappingContext]):  [Read-Write] Maps one Input Mapping Context to another. This can be used to replace
  specific Input Mapping Contexts with another on a per-platform basis.

<a id="unreal.EnhancedInputPlatformData.mapping_context_redirects"></a>

#### mapping_context_redirects

```python
@property
def mapping_context_redirects(
) -> Map[InputMappingContext, InputMappingContext]
```

(Map[InputMappingContext, InputMappingContext]):  [Read-Only] Maps one Input Mapping Context to another. This can be used to replace
specific Input Mapping Contexts with another on a per-platform basis.

<a id="unreal.EnhancedInputPlatformData.get_context_redirect"></a>

#### get_context_redirect

```python
def get_context_redirect(context: InputMappingContext) -> InputMappingContext
```

x.get_context_redirect(context) -> InputMappingContext
Returns a pointer to the desired redirect mapping context. If there isn't one, then this returns InContext.

Args:
    context (InputMappingContext): 

Returns:
    InputMappingContext:

<a id="unreal.EnhancedInputSubsystemInterface"></a>