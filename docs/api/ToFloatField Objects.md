## ToFloatField Objects

```python
class ToFloatField(FieldNodeFloat)
```

Convert an integer field to a scalar one

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
- ``int_field`` (FieldNodeInt):  [Read-Write] Integer field to be converted to an a scalar one
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ToFloatField.int_field"></a>

#### int_field

```python
@property
def int_field() -> FieldNodeInt
```

(FieldNodeInt):  [Read-Write] Integer field to be converted to an a scalar one

<a id="unreal.ToFloatField.int_field"></a>

#### int_field

```python
@int_field.setter
def int_field(value: FieldNodeInt) -> None
```

<a id="unreal.ToFloatField.set_to_float_field"></a>

#### set_to_float_field

```python
def set_to_float_field(integer_field: FieldNodeInt) -> ToFloatField
```

x.set_to_float_field(integer_field) -> ToFloatField
Convert an integer field to a float one

Args:
    integer_field (FieldNodeInt): Integer field to be converted to an a float one

Returns:
    ToFloatField:

<a id="unreal.CullingField"></a>