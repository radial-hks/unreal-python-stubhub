## OperatorField Objects

```python
class OperatorField(FieldNodeBase)
```

Compute an operation between 2 incoming fields

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
- ``left_field`` (FieldNodeBase):  [Read-Write] Left field to be processed
- ``magnitude`` (float):  [Read-Write] Magnitude of the operator field
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``operation`` (FieldOperationType):  [Read-Write] Type of operation you want to perform between the 2 fields
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``right_field`` (FieldNodeBase):  [Read-Write] Right field to be processed

<a id="unreal.OperatorField.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write] Magnitude of the operator field

<a id="unreal.OperatorField.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.OperatorField.right_field"></a>

#### right_field

```python
@property
def right_field() -> FieldNodeBase
```

(FieldNodeBase):  [Read-Write] Right field to be processed

<a id="unreal.OperatorField.right_field"></a>

#### right_field

```python
@right_field.setter
def right_field(value: FieldNodeBase) -> None
```

<a id="unreal.OperatorField.left_field"></a>

#### left_field

```python
@property
def left_field() -> FieldNodeBase
```

(FieldNodeBase):  [Read-Write] Left field to be processed

<a id="unreal.OperatorField.left_field"></a>

#### left_field

```python
@left_field.setter
def left_field(value: FieldNodeBase) -> None
```

<a id="unreal.OperatorField.operation"></a>

#### operation

```python
@property
def operation() -> FieldOperationType
```

(FieldOperationType):  [Read-Write] Type of operation you want to perform between the 2 fields

<a id="unreal.OperatorField.operation"></a>

#### operation

```python
@operation.setter
def operation(value: FieldOperationType) -> None
```

<a id="unreal.OperatorField.set_operator_field"></a>

#### set_operator_field

```python
def set_operator_field(magnitude: float = 1.000000,
                       left_field: FieldNodeBase = ...,
                       right_field: FieldNodeBase = ...,
                       operation: FieldOperationType = ...) -> OperatorField
```

x.set_operator_field(magnitude=1.000000, left_field, right_field, operation) -> OperatorField
Compute an operation between 2 incoming fields

Args:
    magnitude (float): Magnitude of the operator field
    left_field (FieldNodeBase): Input field A to be processed
    right_field (FieldNodeBase): Input field B to be processed
    operation (FieldOperationType): Type of math operation you want to perform between the 2 fields

Returns:
    OperatorField:

<a id="unreal.ToIntegerField"></a>