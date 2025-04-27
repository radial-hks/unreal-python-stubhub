## BuiltInAttributesExtensions Objects

```python
class BuiltInAttributesExtensions(BlueprintFunctionLibrary)
```

Built in Attributes Extensions

**C++ Source:**

- **Module**: Engine
- **File**: BuiltInAttributeTypes.h

<a id="unreal.BuiltInAttributesExtensions.add_transform_attribute"></a>

#### add_transform_attribute

```python
@classmethod
def add_transform_attribute(cls, anim_sequence_base: AnimSequenceBase,
                            attribute_name: Name, bone_name: Name,
                            keys: Array[float],
                            values: Array[Transform]) -> bool
```

X.add_transform_attribute(anim_sequence_base, attribute_name, bone_name, keys, values) -> bool
Add Transform Attribute

Args:
    anim_sequence_base (AnimSequenceBase): 
    attribute_name (Name): 
    bone_name (Name): 
    keys (Array[float]): 
    values (Array[Transform]): 

Returns:
    bool:

<a id="unreal.ChaosBlueprintLibrary"></a>