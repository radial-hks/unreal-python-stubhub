## RadialIntMask Objects

```python
class RadialIntMask(FieldNodeInt)
```

This function first defines a radial integer field equal to Interior-value inside a sphere / Exterior-value outside. This field will be used alongside the particle input value and the mask condition to compute the particle output value.

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
- ``exterior_value`` (int32):  [Read-Write] If the sample distance from the center is greater than radius, the intermediate value will be set the exterior value
- ``interior_value`` (int32):  [Read-Write] If the sample distance from the center is less than radius, the intermediate value will be set the interior value
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``position`` (Vector):  [Read-Write] Center position of the radial mask field
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``radius`` (float):  [Read-Write] Radius of the radial mask field
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``set_mask_condition`` (SetMaskConditionType):  [Read-Write] If the mask condition is set to always the output value will be the intermediate one. If set to not interior/exterior the output value will be the intermediate one if the input is different from the interior/exterior value

<a id="unreal.RadialIntMask.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Radius of the radial mask field

<a id="unreal.RadialIntMask.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RadialIntMask.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Center position of the radial mask field

<a id="unreal.RadialIntMask.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.RadialIntMask.interior_value"></a>

#### interior_value

```python
@property
def interior_value() -> int
```

(int32):  [Read-Write] If the sample distance from the center is less than radius, the intermediate value will be set the interior value

<a id="unreal.RadialIntMask.interior_value"></a>

#### interior_value

```python
@interior_value.setter
def interior_value(value: int) -> None
```

<a id="unreal.RadialIntMask.exterior_value"></a>

#### exterior_value

```python
@property
def exterior_value() -> int
```

(int32):  [Read-Write] If the sample distance from the center is greater than radius, the intermediate value will be set the exterior value

<a id="unreal.RadialIntMask.exterior_value"></a>

#### exterior_value

```python
@exterior_value.setter
def exterior_value(value: int) -> None
```

<a id="unreal.RadialIntMask.set_mask_condition"></a>

#### set_mask_condition

```python
@property
def set_mask_condition() -> SetMaskConditionType
```

(SetMaskConditionType):  [Read-Write] If the mask condition is set to always the output value will be the intermediate one. If set to not interior/exterior the output value will be the intermediate one if the input is different from the interior/exterior value

<a id="unreal.RadialIntMask.set_mask_condition"></a>

#### set_mask_condition

```python
@set_mask_condition.setter
def set_mask_condition(value: SetMaskConditionType) -> None
```

<a id="unreal.RadialIntMask.set_radial_int_mask"></a>

#### set_radial_int_mask

```python
def set_radial_int_mask(
        radius: float,
        position: Vector,
        interior_value: int = 1,
        exterior_value: int = ...,
        set_mask_condition_in: SetMaskConditionType = ...) -> RadialIntMask
```

x.set_radial_int_mask(radius, position, interior_value=1, exterior_value, set_mask_condition_in) -> RadialIntMask
This function first defines a radial integer field equal to Interior-value inside a sphere / Exterior-value outside. This field will be used alongside the particle input value and the mask condition to compute the particle output value.
- If Mask-condition = set-always : the particle output value will be equal to Interior-value if the particle position is inside a sphere / Exterior-value otherwise.
- If Mask-condition = merge-interior : the particle output value will be equal to Interior-value if the particle position is inside the sphere or if the particle input value is already Interior-Value / Exterior-value otherwise.
- If Mask-condition = merge-exterior : the particle output value will be equal to Exterior-value if the particle position is outside the sphere or if the particle input value is already Exterior-Value / Interior-value otherwise.

Args:
    radius (float): Radius of the radial field
    position (Vector): Center position of the radial field"
    interior_value (int32): If the sample distance from the center is less than radius, the intermediate value will be set the interior value
    exterior_value (int32): If the sample distance from the center is greater than radius, the intermediate value will be set the exterior value
    set_mask_condition_in (SetMaskConditionType): If the mask condition is set to always the output value will be the intermediate one. If set to not interior/exterior the output value will be the intermediate one if the input is different from the interior/exterior value

Returns:
    RadialIntMask:

<a id="unreal.UniformScalar"></a>