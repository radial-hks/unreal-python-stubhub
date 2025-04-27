## UniformInteger Objects

```python
class UniformInteger(FieldNodeInt)
```

Set a uniform integer value independently of the sample position. The output is equal to magnitude

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``magnitude`` (int32):  [Read-Write] The field output will be equal the magnitude
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.UniformInteger.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> int
```

(int32):  [Read-Write] The field output will be equal the magnitude

<a id="unreal.UniformInteger.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: int) -> None
```

<a id="unreal.UniformInteger.set_uniform_integer"></a>

#### set_uniform_integer

```python
def set_uniform_integer(magnitude: int = 0) -> UniformInteger
```

x.set_uniform_integer(magnitude=0) -> UniformInteger
Set a uniform integer value independently of the sample position. The output is equal to magnitude

Args:
    magnitude (int32): The field output will be equal the magnitude

Returns:
    UniformInteger:

<a id="unreal.RadialIntMask"></a>