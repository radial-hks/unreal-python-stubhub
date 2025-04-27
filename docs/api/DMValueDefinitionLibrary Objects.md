## DMValueDefinitionLibrary Objects

```python
class DMValueDefinitionLibrary(BlueprintFunctionLibrary)
```

DMValue Definition Library

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMValueDefinition.h

<a id="unreal.DMValueDefinitionLibrary.get_value_types"></a>

#### get_value_types

```python
@classmethod
def get_value_types(cls) -> Array[DMValueType]
```

X.get_value_types() -> Array[DMValueType]
Returns the array of available Value Types, excluding generics like None or Max.

Returns:
    Array[DMValueType]:

<a id="unreal.DMValueDefinitionLibrary.get_value_definition"></a>

#### get_value_definition

```python
@classmethod
def get_value_definition(cls, value_type: DMValueType) -> DMValueDefinition
```

X.get_value_definition(value_type) -> DMValueDefinition
Returns a value definition for the given value type.

Args:
    value_type (DMValueType): 

Returns:
    DMValueDefinition:

<a id="unreal.DMValueDefinitionLibrary.get_type_for_float_count"></a>

#### get_type_for_float_count

```python
@classmethod
def get_type_for_float_count(cls, float_count: int) -> DMValueDefinition
```

X.get_type_for_float_count(float_count) -> DMValueDefinition
Converts a number of floats into the value type

Args:
    float_count (int32): 

Returns:
    DMValueDefinition:

<a id="unreal.DMValueDefinitionLibrary.bp_are_types_compatible"></a>

#### bp_are_types_compatible

```python
@classmethod
def bp_are_types_compatible(cls, a: DMValueType, b: DMValueType,
                            a_channel: int, b_channel: int) -> bool
```

X.bp_are_types_compatible(a, b, a_channel, b_channel) -> bool
Returns whether the given types can be connected together as input/output.

Args:
    a (DMValueType): 
    b (DMValueType): 
    a_channel (int32): 
    b_channel (int32): 

Returns:
    bool:

<a id="unreal.DynamicMaterialInstance"></a>