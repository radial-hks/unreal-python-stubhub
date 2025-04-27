## PCGBlueprintPinHelpers Objects

```python
class PCGBlueprintPinHelpers(BlueprintFunctionLibrary)
```

PCGBlueprint Pin Helpers

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

<a id="unreal.PCGBlueprintPinHelpers.is_of_type"></a>

#### is_of_type

```python
@classmethod
def is_of_type(cls, allowed_types: int,
               type_to_check: PCGExclusiveDataType) -> bool
```

X.is_of_type(allowed_types, type_to_check) -> bool
Is Of Type

Args:
    allowed_types (int32): 
    type_to_check (PCGExclusiveDataType): 

Returns:
    bool:

<a id="unreal.PCGBlueprintPinHelpers.is_exactly_same_type"></a>

#### is_exactly_same_type

```python
@classmethod
def is_exactly_same_type(cls, allowed_types: int,
                         type_to_check: PCGExclusiveDataType) -> bool
```

X.is_exactly_same_type(allowed_types, type_to_check) -> bool
Is Exactly Same Type

Args:
    allowed_types (int32): 
    type_to_check (PCGExclusiveDataType): 

Returns:
    bool:

<a id="unreal.PCGBlueprintPinHelpers.get_corresponding_data_type"></a>

#### get_corresponding_data_type

```python
@classmethod
def get_corresponding_data_type(
        cls, exclusive_data_type: PCGExclusiveDataType) -> int
```

X.get_corresponding_data_type(exclusive_data_type) -> int32
Get Corresponding Data Type

Args:
    exclusive_data_type (PCGExclusiveDataType): 

Returns:
    int32:

<a id="unreal.PCGPin"></a>