## MovieJobVariableAssignmentContainer Objects

```python
class MovieJobVariableAssignmentContainer(Object)
```

Holds a group of properties which override variable values on the job's associated graph (if any). Overrides are not
added manually. Instead, UpdateGraphVariableOverrides() should be called which will update, add, or remove overrides
as appropriate. After the update, overrides can have their values retrieved and set.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieJobVariableAssignmentContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (InstancedPropertyBag):  [Read-Write] The properties managed by this object.

<a id="unreal.MovieJobVariableAssignmentContainer.update_graph_variable_overrides"></a>

#### update_graph_variable_overrides

```python
def update_graph_variable_overrides() -> None
```

x.update_graph_variable_overrides() -> None
Updates the stored variable overrides to reflect the graph preset. Existing overrides will be updated to match
the graph variable name, value type, object type, and container type. Additionally, stale overrides that have no
corresponding graph variable will be removed, and overrides will be created for graph variables which do not have
existing overrides.

<a id="unreal.MovieJobVariableAssignmentContainer.set_variable_assignment_enable_state"></a>

#### set_variable_assignment_enable_state

```python
def set_variable_assignment_enable_state(graph_variable: MovieGraphVariable,
                                         is_enabled: bool) -> bool
```

x.set_variable_assignment_enable_state(graph_variable, is_enabled) -> bool
Updates an existing variable assignment for the provided graph variable to a new enable state, or adds a new
assignment and updates its enable state. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    is_enabled (bool): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_text"></a>

#### set_value_text

```python
def set_value_text(graph_variable: MovieGraphVariable, value: Text) -> bool
```

x.set_value_text(graph_variable, value) -> bool
Sets the FText value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (Text): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_string"></a>

#### set_value_string

```python
def set_value_string(graph_variable: MovieGraphVariable, value: str) -> bool
```

x.set_value_string(graph_variable, value) -> bool
Sets the FString value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (str): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_serialized_string"></a>

#### set_value_serialized_string

```python
def set_value_serialized_string(graph_variable: MovieGraphVariable,
                                new_value: str) -> bool
```

x.set_value_serialized_string(graph_variable, new_value) -> bool
Sets the serialized value of this member. The string should be the serialized representation of the value. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    new_value (str): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_object"></a>

#### set_value_object

```python
def set_value_object(graph_variable: MovieGraphVariable,
                     value: Object) -> bool
```

x.set_value_object(graph_variable, value) -> bool
Sets the object value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (Object): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_name"></a>

#### set_value_name

```python
def set_value_name(graph_variable: MovieGraphVariable, value: Name) -> bool
```

x.set_value_name(graph_variable, value) -> bool
Sets the FName value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (Name): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_int64"></a>

#### set_value_int64

```python
def set_value_int64(graph_variable: MovieGraphVariable, value: int) -> bool
```

x.set_value_int64(graph_variable, value) -> bool
Sets the int64 value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (int64): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_int32"></a>

#### set_value_int32

```python
def set_value_int32(graph_variable: MovieGraphVariable, value: int) -> bool
```

x.set_value_int32(graph_variable, value) -> bool
Sets the int32 value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (int32): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_float"></a>

#### set_value_float

```python
def set_value_float(graph_variable: MovieGraphVariable, value: float) -> bool
```

x.set_value_float(graph_variable, value) -> bool
Sets the float value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (float): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_enum"></a>

#### set_value_enum

```python
def set_value_enum(graph_variable: MovieGraphVariable, value: int,
                   enum: Enum) -> bool
```

x.set_value_enum(graph_variable, value, enum) -> bool
Sets the enum value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (uint8): 
    enum (Enum): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_double"></a>

#### set_value_double

```python
def set_value_double(graph_variable: MovieGraphVariable, value: float) -> bool
```

x.set_value_double(graph_variable, value) -> bool
Sets the double value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (double): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_class"></a>

#### set_value_class

```python
def set_value_class(graph_variable: MovieGraphVariable, value: Class) -> bool
```

x.set_value_class(graph_variable, value) -> bool
Sets the class value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (type(Class)): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_byte"></a>

#### set_value_byte

```python
def set_value_byte(graph_variable: MovieGraphVariable, value: int) -> bool
```

x.set_value_byte(graph_variable, value) -> bool
Sets the byte value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (uint8): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_value_bool"></a>

#### set_value_bool

```python
def set_value_bool(graph_variable: MovieGraphVariable, value: bool) -> bool
```

x.set_value_bool(graph_variable, value) -> bool
Sets the bool value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    value (bool): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.set_graph_config"></a>

#### set_graph_config

```python
def set_graph_config(graph_config: MovieGraphConfig) -> None
```

x.set_graph_config(graph_config) -> None
Sets the graph config associated with the variable assignments.

Args:
    graph_config (MovieGraphConfig):

<a id="unreal.MovieJobVariableAssignmentContainer.get_variable_assignment_enable_state"></a>

#### get_variable_assignment_enable_state

```python
def get_variable_assignment_enable_state(
        graph_variable: MovieGraphVariable) -> Optional[bool]
```

x.get_variable_assignment_enable_state(graph_variable) -> bool or None
Gets the enable state of the variable assignment for the provided graph variable. The enable state is provided
via bOutIsEnabled. Returns true if an enable state was set on the variable and bOutIsEnabled was changed, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    bool or None: 

    out_is_enabled (bool):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_type_object"></a>

#### get_value_type_object

```python
def get_value_type_object(graph_variable: MovieGraphVariable) -> Object
```

x.get_value_type_object(graph_variable) -> Object
Gets the object that defines the enum, struct, or class stored in the specified property.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    Object:

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_type"></a>

#### get_value_type

```python
def get_value_type(graph_variable: MovieGraphVariable) -> MovieGraphValueType
```

x.get_value_type(graph_variable) -> MovieGraphValueType
Gets the type of the value stored in the specified property.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    MovieGraphValueType:

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_text"></a>

#### get_value_text

```python
def get_value_text(graph_variable: MovieGraphVariable) -> Optional[Text]
```

x.get_value_text(graph_variable) -> Text or None
Gets the FText value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    Text or None: 

    out_value (Text):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_string"></a>

#### get_value_string

```python
def get_value_string(graph_variable: MovieGraphVariable) -> Optional[str]
```

x.get_value_string(graph_variable) -> str or None
Gets the FString value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    str or None: 

    out_value (str):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_serialized_string"></a>

#### get_value_serialized_string

```python
def get_value_serialized_string(graph_variable: MovieGraphVariable) -> str
```

x.get_value_serialized_string(graph_variable) -> str
Gets the serialized string value of the specified property.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    str:

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_object"></a>

#### get_value_object

```python
def get_value_object(graph_variable: MovieGraphVariable,
                     out_value: Object,
                     requested_class: Class = None) -> bool
```

x.get_value_object(graph_variable, out_value, requested_class=None) -> bool
Gets the object value (for a specific class) of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    out_value (Object): 
    requested_class (type(Class)): 

Returns:
    bool:

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_name"></a>

#### get_value_name

```python
def get_value_name(graph_variable: MovieGraphVariable) -> Optional[Name]
```

x.get_value_name(graph_variable) -> Name or None
Gets the FName value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    Name or None: 

    out_value (Name):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_int64"></a>

#### get_value_int64

```python
def get_value_int64(graph_variable: MovieGraphVariable) -> Optional[int]
```

x.get_value_int64(graph_variable) -> int64 or None
Gets the int64 value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    int64 or None: 

    out_value (int64):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_int32"></a>

#### get_value_int32

```python
def get_value_int32(graph_variable: MovieGraphVariable) -> Optional[int]
```

x.get_value_int32(graph_variable) -> int32 or None
Gets the int32 value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    int32 or None: 

    out_value (int32):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_float"></a>

#### get_value_float

```python
def get_value_float(graph_variable: MovieGraphVariable) -> Optional[float]
```

x.get_value_float(graph_variable) -> float or None
Gets the float value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    float or None: 

    out_value (float):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_enum"></a>

#### get_value_enum

```python
def get_value_enum(graph_variable: MovieGraphVariable,
                   requested_enum: Enum = None) -> Optional[int]
```

x.get_value_enum(graph_variable, requested_enum=None) -> uint8 or None
Gets the enum value (for a specific enum) of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 
    requested_enum (Enum): 

Returns:
    uint8 or None: 

    out_value (uint8):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_double"></a>

#### get_value_double

```python
def get_value_double(graph_variable: MovieGraphVariable) -> Optional[float]
```

x.get_value_double(graph_variable) -> double or None
Gets the double value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    double or None: 

    out_value (double):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_container_type"></a>

#### get_value_container_type

```python
def get_value_container_type(
        graph_variable: MovieGraphVariable) -> MovieGraphContainerType
```

x.get_value_container_type(graph_variable) -> MovieGraphContainerType
Gets the container type of the stored value in the specified property.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    MovieGraphContainerType:

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_class"></a>

#### get_value_class

```python
def get_value_class(graph_variable: MovieGraphVariable) -> Optional[Class]
```

x.get_value_class(graph_variable) -> type(Class) or None
Gets the UClass value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    type(Class) or None: 

    out_value (type(Class)):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_byte"></a>

#### get_value_byte

```python
def get_value_byte(graph_variable: MovieGraphVariable) -> Optional[int]
```

x.get_value_byte(graph_variable) -> uint8 or None
Gets the byte value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    uint8 or None: 

    out_value (uint8):

<a id="unreal.MovieJobVariableAssignmentContainer.get_value_bool"></a>

#### get_value_bool

```python
def get_value_bool(graph_variable: MovieGraphVariable) -> Optional[bool]
```

x.get_value_bool(graph_variable) -> bool or None
Gets the bool value of the specified property. Returns true on success, else false.

Args:
    graph_variable (MovieGraphVariable): 

Returns:
    bool or None: 

    out_value (bool):

<a id="unreal.MoviePipelineGameMode"></a>