## ToIntegerField Objects

```python
class ToIntegerField(FieldNodeInt)
```

Convert a scalar field to a integer one

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
- ``float_field`` (FieldNodeFloat):  [Read-Write] Scalar field to be converted to an an integer one
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ToIntegerField.float_field"></a>

#### float_field

```python
@property
def float_field() -> FieldNodeFloat
```

(FieldNodeFloat):  [Read-Write] Scalar field to be converted to an an integer one

<a id="unreal.ToIntegerField.float_field"></a>

#### float_field

```python
@float_field.setter
def float_field(value: FieldNodeFloat) -> None
```

<a id="unreal.ToIntegerField.set_to_integer_field"></a>

#### set_to_integer_field

```python
def set_to_integer_field(float_field: FieldNodeFloat) -> ToIntegerField
```

x.set_to_integer_field(float_field) -> ToIntegerField
Convert a float field to a integer one

Args:
    float_field (FieldNodeFloat): Float field to be converted to an an integer one

Returns:
    ToIntegerField:

<a id="unreal.ToFloatField"></a>