## CullingField Objects

```python
class CullingField(FieldNodeBase)
```

Evaluate the input field according to the result of the culling field

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``culling`` (FieldNodeBase):  [Read-Write] Culling field to be used
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``field`` (FieldNodeBase):  [Read-Write] Input field that will be evaluated according to the culling field result
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``operation`` (FieldCullingOperationType):  [Read-Write] Evaluate the input field if the result of the culling field is equal to 0 (Inside) or different from 0 (Outside)
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.CullingField.culling"></a>

#### culling

```python
@property
def culling() -> FieldNodeBase
```

(FieldNodeBase):  [Read-Write] Culling field to be used

<a id="unreal.CullingField.culling"></a>

#### culling

```python
@culling.setter
def culling(value: FieldNodeBase) -> None
```

<a id="unreal.CullingField.field"></a>

#### field

```python
@property
def field() -> FieldNodeBase
```

(FieldNodeBase):  [Read-Write] Input field that will be evaluated according to the culling field result

<a id="unreal.CullingField.field"></a>

#### field

```python
@field.setter
def field(value: FieldNodeBase) -> None
```

<a id="unreal.CullingField.operation"></a>

#### operation

```python
@property
def operation() -> FieldCullingOperationType
```

(FieldCullingOperationType):  [Read-Write] Evaluate the input field if the result of the culling field is equal to 0 (Inside) or different from 0 (Outside)

<a id="unreal.CullingField.operation"></a>

#### operation

```python
@operation.setter
def operation(value: FieldCullingOperationType) -> None
```

<a id="unreal.CullingField.set_culling_field"></a>

#### set_culling_field

```python
def set_culling_field(culling: FieldNodeBase, field: FieldNodeBase,
                      operation: FieldCullingOperationType) -> CullingField
```

x.set_culling_field(culling, field, operation) -> CullingField
Evaluate the input field according to the result of the culling field.

Args:
    culling (FieldNodeBase): Culling field to be used.
    field (FieldNodeBase): Input field that will be evaluated according to the culling field result.
    operation (FieldCullingOperationType): Evaluate the input field if the result of the culling field is equal to 0 (Inside) or different from 0 (Outside).

Returns:
    CullingField:

<a id="unreal.ReturnResultsTerminal"></a>