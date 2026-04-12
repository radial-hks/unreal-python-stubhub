## DataRegistrySubsystem Objects

```python
class DataRegistrySubsystem(EngineSubsystem)
```

Singleton manager that provides synchronous and asynchronous access to data registries

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: DataRegistrySubsystem.h

<a id="unreal.DataRegistrySubsystem.not_equal_data_registry_type"></a>

#### not\_equal\_data\_registry\_type

```python
@classmethod
def not_equal_data_registry_type(cls, a: DataRegistryType,
                                 b: DataRegistryType) -> bool
```

X.not_equal_data_registry_type(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (DataRegistryType): 
    b (DataRegistryType): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.not_equal_data_registry_id"></a>

#### not\_equal\_data\_registry\_id

```python
@classmethod
def not_equal_data_registry_id(cls, a: DataRegistryId,
                               b: DataRegistryId) -> bool
```

X.not_equal_data_registry_id(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (DataRegistryId): 
    b (DataRegistryId): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.is_valid_data_registry_type"></a>

#### is\_valid\_data\_registry\_type

```python
@classmethod
def is_valid_data_registry_type(cls,
                                data_registry_type: DataRegistryType) -> bool
```

X.is_valid_data_registry_type(data_registry_type) -> bool
Returns true if this is a non-empty type, does not check if it is currently registered

Args:
    data_registry_type (DataRegistryType): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.is_valid_data_registry_id"></a>

#### is\_valid\_data\_registry\_id

```python
@classmethod
def is_valid_data_registry_id(cls, data_registry_id: DataRegistryId) -> bool
```

X.is_valid_data_registry_id(data_registry_id) -> bool
Returns true if this is a non-empty item identifier, does not check if it is currently registered

Args:
    data_registry_id (DataRegistryId): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.get_possible_data_registry_id_list"></a>

#### get\_possible\_data\_registry\_id\_list

```python
@classmethod
def get_possible_data_registry_id_list(
        cls, registry_type: DataRegistryType) -> Array[DataRegistryId]
```

X.get_possible_data_registry_id_list(registry_type) -> Array[DataRegistryId]
Returns the list of known identifiers for an active data registry so they can be iterated with Find or Acquire.
Depending on how the registry is setup, this could be a large number of identifiers and they may not all be available.

Args:
    registry_type (DataRegistryType): The type of data registry to query

Returns:
    Array[DataRegistryId]: 

    out_id_list (Array[DataRegistryId]): The list of known identifiers for the type, which will be empty if the type is not registered

<a id="unreal.DataRegistrySubsystem.evaluate_data_registry_curve"></a>

#### evaluate\_data\_registry\_curve

```python
@classmethod
def evaluate_data_registry_curve(
        cls, item_id: DataRegistryId, input_value: float, default_value: float
) -> Tuple[DataRegistrySubsystemGetItemResult, float]
```

X.evaluate_data_registry_curve(item_id, input_value, default_value) -> (out_result=DataRegistrySubsystemGetItemResult, out_value=float)
Attempts to evaluate a curve stored in a DataRegistry cache using a specific input value

Args:
    item_id (DataRegistryId): Item identifier to lookup in cache
    input_value (float): Time/level/parameter input value used to evaluate curve at certain position
    default_value (float): Value to use if no curve found or input is outside acceptable range

Returns:
    tuple: 

    out_result (DataRegistrySubsystemGetItemResult): 

    out_value (float): Result will be replaced with evaluated value, or default if that fails

<a id="unreal.DataRegistrySubsystem.equal_equal_data_registry_type"></a>

#### equal\_equal\_data\_registry\_type

```python
@classmethod
def equal_equal_data_registry_type(cls, a: DataRegistryType,
                                   b: DataRegistryType) -> bool
```

X.equal_equal_data_registry_type(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (DataRegistryType): 
    b (DataRegistryType): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.equal_equal_data_registry_id"></a>

#### equal\_equal\_data\_registry\_id

```python
@classmethod
def equal_equal_data_registry_id(cls, a: DataRegistryId,
                                 b: DataRegistryId) -> bool
```

X.equal_equal_data_registry_id(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (DataRegistryId): 
    b (DataRegistryId): 

Returns:
    bool:

<a id="unreal.DataRegistrySubsystem.conv_data_registry_type_to_string"></a>

#### conv\_data\_registry\_type\_to\_string

```python
@classmethod
def conv_data_registry_type_to_string(
        cls, data_registry_type: DataRegistryType) -> str
```

X.conv_data_registry_type_to_string(data_registry_type) -> str
Converts a Data Registry Type to a string. The other direction is not provided because it cannot be validated

Args:
    data_registry_type (DataRegistryType): 

Returns:
    str:

<a id="unreal.DataRegistrySubsystem.conv_data_registry_id_to_string"></a>

#### conv\_data\_registry\_id\_to\_string

```python
@classmethod
def conv_data_registry_id_to_string(cls,
                                    data_registry_id: DataRegistryId) -> str
```

X.conv_data_registry_id_to_string(data_registry_id) -> str
Converts a Data Registry Id to a string. The other direction is not provided because it cannot be validated

Args:
    data_registry_id (DataRegistryId): 

Returns:
    str:

<a id="unreal.DataRegistrySubsystem.acquire_item_bp"></a>

#### acquire\_item\_bp

```python
@classmethod
def acquire_item_bp(
        cls, item_id: DataRegistryId,
        acquire_callback: DataRegistryItemAcquiredBPCallback) -> bool
```

X.acquire_item_bp(item_id, acquire_callback) -> bool
Starts an asynchronous acquire of a data registry item that may not yet be cached, and then accessed with Get Data Registry Item From Lookup
This function will only work properly if the data registry is set up for asynchronous querying.

Args:
    item_id (DataRegistryId): Item identifier to lookup in cache
    acquire_callback (DataRegistryItemAcquiredBPCallback): Delegate that will be called after acquire succeeds or failed

Returns:
    bool: Returns true if request was started, false on unrecoverable error

<a id="unreal.DataRegistryFactory"></a>