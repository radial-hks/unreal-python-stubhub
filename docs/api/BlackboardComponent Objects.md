## BlackboardComponent Objects

```python
class BlackboardComponent(ActorComponent)
```

Blackboard Component

**C++ Source:**

- **Module**: AIModule
- **File**: BlackboardComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``default_blackboard_asset`` (BlackboardData):  [Read-Write] data asset defining entries. Will be used as part of InitializeComponent
      call provided BlackboardAsset hasn't been already set (via a InitializeBlackboard
      call).
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.BlackboardComponent.set_value_as_vector"></a>

#### set_value_as_vector

```python
def set_value_as_vector(key_name: Name, vector_value: Vector) -> None
```

x.set_value_as_vector(key_name, vector_value) -> None
Set Value as Vector

Args:
    key_name (Name): 
    vector_value (Vector):

<a id="unreal.BlackboardComponent.set_value_as_string"></a>

#### set_value_as_string

```python
def set_value_as_string(key_name: Name, string_value: str) -> None
```

x.set_value_as_string(key_name, string_value) -> None
Set Value as String

Args:
    key_name (Name): 
    string_value (str):

<a id="unreal.BlackboardComponent.set_value_as_rotator"></a>

#### set_value_as_rotator

```python
def set_value_as_rotator(key_name: Name, vector_value: Rotator) -> None
```

x.set_value_as_rotator(key_name, vector_value) -> None
Set Value as Rotator

Args:
    key_name (Name): 
    vector_value (Rotator):

<a id="unreal.BlackboardComponent.set_value_as_object"></a>

#### set_value_as_object

```python
def set_value_as_object(key_name: Name, object_value: Object) -> None
```

x.set_value_as_object(key_name, object_value) -> None
Set Value as Object

Args:
    key_name (Name): 
    object_value (Object):

<a id="unreal.BlackboardComponent.set_value_as_name"></a>

#### set_value_as_name

```python
def set_value_as_name(key_name: Name, name_value: Name) -> None
```

x.set_value_as_name(key_name, name_value) -> None
Set Value as Name

Args:
    key_name (Name): 
    name_value (Name):

<a id="unreal.BlackboardComponent.set_value_as_int"></a>

#### set_value_as_int

```python
def set_value_as_int(key_name: Name, int_value: int) -> None
```

x.set_value_as_int(key_name, int_value) -> None
Set Value as Int

Args:
    key_name (Name): 
    int_value (int32):

<a id="unreal.BlackboardComponent.set_value_as_float"></a>

#### set_value_as_float

```python
def set_value_as_float(key_name: Name, float_value: float) -> None
```

x.set_value_as_float(key_name, float_value) -> None
Set Value as Float

Args:
    key_name (Name): 
    float_value (float):

<a id="unreal.BlackboardComponent.set_value_as_enum"></a>

#### set_value_as_enum

```python
def set_value_as_enum(key_name: Name, enum_value: int) -> None
```

x.set_value_as_enum(key_name, enum_value) -> None
Set Value as Enum

Args:
    key_name (Name): 
    enum_value (uint8):

<a id="unreal.BlackboardComponent.set_value_as_class"></a>

#### set_value_as_class

```python
def set_value_as_class(key_name: Name, class_value: Class) -> None
```

x.set_value_as_class(key_name, class_value) -> None
Set Value as Class

Args:
    key_name (Name): 
    class_value (type(Class)):

<a id="unreal.BlackboardComponent.set_value_as_bool"></a>

#### set_value_as_bool

```python
def set_value_as_bool(key_name: Name, bool_value: bool) -> None
```

x.set_value_as_bool(key_name, bool_value) -> None
Set Value as Bool

Args:
    key_name (Name): 
    bool_value (bool):

<a id="unreal.BlackboardComponent.is_vector_value_set"></a>

#### is_vector_value_set

```python
def is_vector_value_set(key_name: Name) -> bool
```

x.is_vector_value_set(key_name) -> bool
If the vector value has been set (and not cleared), this function returns true (indicating that the value should be valid).  If it's not set, the vector value is invalid and this function will return false.  (Also returns false if the key specified does not hold a vector.)

Args:
    key_name (Name): 

Returns:
    bool:

<a id="unreal.BlackboardComponent.get_value_as_vector"></a>

#### get_value_as_vector

```python
def get_value_as_vector(key_name: Name) -> Vector
```

x.get_value_as_vector(key_name) -> Vector
Get Value as Vector

Args:
    key_name (Name): 

Returns:
    Vector:

<a id="unreal.BlackboardComponent.get_value_as_string"></a>

#### get_value_as_string

```python
def get_value_as_string(key_name: Name) -> str
```

x.get_value_as_string(key_name) -> str
Get Value as String

Args:
    key_name (Name): 

Returns:
    str:

<a id="unreal.BlackboardComponent.get_value_as_rotator"></a>

#### get_value_as_rotator

```python
def get_value_as_rotator(key_name: Name) -> Rotator
```

x.get_value_as_rotator(key_name) -> Rotator
Get Value as Rotator

Args:
    key_name (Name): 

Returns:
    Rotator:

<a id="unreal.BlackboardComponent.get_value_as_object"></a>

#### get_value_as_object

```python
def get_value_as_object(key_name: Name) -> Object
```

x.get_value_as_object(key_name) -> Object
Get Value as Object

Args:
    key_name (Name): 

Returns:
    Object:

<a id="unreal.BlackboardComponent.get_value_as_name"></a>

#### get_value_as_name

```python
def get_value_as_name(key_name: Name) -> Name
```

x.get_value_as_name(key_name) -> Name
Get Value as Name

Args:
    key_name (Name): 

Returns:
    Name:

<a id="unreal.BlackboardComponent.get_value_as_int"></a>

#### get_value_as_int

```python
def get_value_as_int(key_name: Name) -> int
```

x.get_value_as_int(key_name) -> int32
Get Value as Int

Args:
    key_name (Name): 

Returns:
    int32:

<a id="unreal.BlackboardComponent.get_value_as_float"></a>

#### get_value_as_float

```python
def get_value_as_float(key_name: Name) -> float
```

x.get_value_as_float(key_name) -> float
Get Value as Float

Args:
    key_name (Name): 

Returns:
    float:

<a id="unreal.BlackboardComponent.get_value_as_enum"></a>

#### get_value_as_enum

```python
def get_value_as_enum(key_name: Name) -> int
```

x.get_value_as_enum(key_name) -> uint8
Get Value as Enum

Args:
    key_name (Name): 

Returns:
    uint8:

<a id="unreal.BlackboardComponent.get_value_as_class"></a>

#### get_value_as_class

```python
def get_value_as_class(key_name: Name) -> Class
```

x.get_value_as_class(key_name) -> type(Class)
Get Value as Class

Args:
    key_name (Name): 

Returns:
    type(Class):

<a id="unreal.BlackboardComponent.get_value_as_bool"></a>

#### get_value_as_bool

```python
def get_value_as_bool(key_name: Name) -> bool
```

x.get_value_as_bool(key_name) -> bool
Get Value as Bool

Args:
    key_name (Name): 

Returns:
    bool:

<a id="unreal.BlackboardComponent.get_rotation_from_entry"></a>

#### get_rotation_from_entry

```python
def get_rotation_from_entry(key_name: Name) -> Optional[Rotator]
```

x.get_rotation_from_entry(key_name) -> Rotator or None
return false if call failed (most probably no such entry in BB)

Args:
    key_name (Name): 

Returns:
    Rotator or None: 

    result_rotation (Rotator):

<a id="unreal.BlackboardComponent.get_location_from_entry"></a>

#### get_location_from_entry

```python
def get_location_from_entry(key_name: Name) -> Optional[Vector]
```

x.get_location_from_entry(key_name) -> Vector or None
return false if call failed (most probably no such entry in BB)

Args:
    key_name (Name): 

Returns:
    Vector or None: 

    result_location (Vector):

<a id="unreal.BlackboardComponent.clear_value"></a>

#### clear_value

```python
def clear_value(key_name: Name) -> None
```

x.clear_value(key_name) -> None
Clear Value

Args:
    key_name (Name):

<a id="unreal.DataAsset"></a>