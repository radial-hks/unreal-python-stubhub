## RigHierarchy Objects

```python
class RigHierarchy(Object)
```

Rig Hierarchy

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modified_event`` (RigHierarchyModifiedDynamicEvent):  [Read-Write]

<a id="unreal.RigHierarchy.modified_event"></a>

#### modified_event

```python
@property
def modified_event() -> RigHierarchyModifiedDynamicEvent
```

(RigHierarchyModifiedDynamicEvent):  [Read-Only]

<a id="unreal.RigHierarchy.unset_curve_value_by_index"></a>

#### unset_curve_value_by_index

```python
def unset_curve_value_by_index(element_index: int,
                               setup_undo: bool = False) -> None
```

x.unset_curve_value_by_index(element_index, setup_undo=False) -> None
Sets a curve's value given its index

Args:
    element_index (int32): The index of the element to set the value for
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.unset_curve_value"></a>

#### unset_curve_value

```python
def unset_curve_value(key: RigElementKey, setup_undo: bool = False) -> None
```

x.unset_curve_value(key, setup_undo=False) -> None
Sets a curve's value given its key

Args:
    key (RigElementKey): The key of the element to set the value for
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.switch_to_world_space"></a>

#### switch_to_world_space

```python
def switch_to_world_space(child: RigElementKey,
                          initial: bool = False,
                          affect_children: bool = True) -> bool
```

x.switch_to_world_space(child, initial=False, affect_children=True) -> bool
Switches a multi parent element to world space.
This injects a world space reference.

Args:
    child (RigElementKey): The key of the multi parented element
    initial (bool): If true the initial weights will be used
    affect_children (bool): If set to false children will not move (maintain global).

Returns:
    bool: Returns true if changing the weight was successful

<a id="unreal.RigHierarchy.switch_to_parent"></a>

#### switch_to_parent

```python
def switch_to_parent(child: RigElementKey,
                     parent: RigElementKey,
                     initial: bool = False,
                     affect_children: bool = True) -> bool
```

x.switch_to_parent(child, parent, initial=False, affect_children=True) -> bool
Switches a multi parent element to a single parent.
This sets the new parent's weight to 1.0 and disables
weights for all other potential parents.

Args:
    child (RigElementKey): The key of the multi parented element
    parent (RigElementKey): The key of the parent to look up the weight for
    initial (bool): If true the initial weights will be used
    affect_children (bool): If set to false children will not move (maintain global).

Returns:
    bool: Returns true if changing the weight was successful

<a id="unreal.RigHierarchy.switch_to_default_parent"></a>

#### switch_to_default_parent

```python
def switch_to_default_parent(child: RigElementKey,
                             initial: bool = False,
                             affect_children: bool = True) -> bool
```

x.switch_to_default_parent(child, initial=False, affect_children=True) -> bool
Switches a multi parent element to its first parent

Args:
    child (RigElementKey): The key of the multi parented element
    initial (bool): If true the initial weights will be used
    affect_children (bool): If set to false children will not move (maintain global).

Returns:
    bool: Returns true if changing the weight was successful

<a id="unreal.RigHierarchy.sort_keys"></a>

#### sort_keys

```python
def sort_keys(keys: Array[RigElementKey]) -> Array[RigElementKey]
```

x.sort_keys(keys) -> Array[RigElementKey]
Sorts the input key list by traversing the hierarchy

Args:
    keys (Array[RigElementKey]): The keys to sort

Returns:
    Array[RigElementKey]: The sorted keys

<a id="unreal.RigHierarchy.set_vector_metadata"></a>

#### set_vector_metadata

```python
def set_vector_metadata(item: RigElementKey, metadata_name: Name,
                        value: Vector) -> bool
```

x.set_vector_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FVector value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Vector): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_vector_array_metadata"></a>

#### set_vector_array_metadata

```python
def set_vector_array_metadata(item: RigElementKey, metadata_name: Name,
                              value: Array[Vector]) -> bool
```

x.set_vector_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FVector array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[Vector]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_transform_metadata"></a>

#### set_transform_metadata

```python
def set_transform_metadata(item: RigElementKey, metadata_name: Name,
                           value: Transform) -> bool
```

x.set_transform_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FTransform value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Transform): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_transform_array_metadata"></a>

#### set_transform_array_metadata

```python
def set_transform_array_metadata(item: RigElementKey, metadata_name: Name,
                                 value: Array[Transform]) -> bool
```

x.set_transform_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FTransform array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[Transform]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_tag"></a>

#### set_tag

```python
def set_tag(item: RigElementKey, tag: Name) -> bool
```

x.set_tag(item, tag) -> bool
* Sets a tag on an element in the hierarchy
*

Args:
    item (RigElementKey): The item to set the tag for *
    tag (Name): The tag to set

Returns:
    bool:

<a id="unreal.RigHierarchy.set_rotator_metadata"></a>

#### set_rotator_metadata

```python
def set_rotator_metadata(item: RigElementKey, metadata_name: Name,
                         value: Rotator) -> bool
```

x.set_rotator_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FRotator value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Rotator): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_rotator_array_metadata"></a>

#### set_rotator_array_metadata

```python
def set_rotator_array_metadata(item: RigElementKey, metadata_name: Name,
                               value: Array[Rotator]) -> bool
```

x.set_rotator_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FRotator array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[Rotator]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_rig_element_key_metadata"></a>

#### set_rig_element_key_metadata

```python
def set_rig_element_key_metadata(item: RigElementKey, metadata_name: Name,
                                 value: RigElementKey) -> bool
```

x.set_rig_element_key_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FRigElementKey value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (RigElementKey): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_rig_element_key_array_metadata"></a>

#### set_rig_element_key_array_metadata

```python
def set_rig_element_key_array_metadata(item: RigElementKey,
                                       metadata_name: Name,
                                       value: Array[RigElementKey]) -> bool
```

x.set_rig_element_key_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FRigElementKey array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[RigElementKey]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_quat_metadata"></a>

#### set_quat_metadata

```python
def set_quat_metadata(item: RigElementKey, metadata_name: Name,
                      value: Quat) -> bool
```

x.set_quat_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FQuat value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Quat): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_quat_array_metadata"></a>

#### set_quat_array_metadata

```python
def set_quat_array_metadata(item: RigElementKey, metadata_name: Name,
                            value: Array[Quat]) -> bool
```

x.set_quat_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FQuat array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[Quat]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_pose"></a>

#### set_pose

```python
def set_pose(pose: RigPose) -> None
```

x.set_pose(pose) -> None
Sets the current / initial pose of the hierarchy

Args:
    pose (RigPose): The pose to set on the hierarchy

<a id="unreal.RigHierarchy.set_parent_weight_array"></a>

#### set_parent_weight_array

```python
def set_parent_weight_array(child: RigElementKey,
                            weights: Array[RigElementWeight],
                            initial: bool = False,
                            affect_children: bool = True) -> bool
```

x.set_parent_weight_array(child, weights, initial=False, affect_children=True) -> bool
Sets the all of the weights of the parents of a multi parent element

Args:
    child (RigElementKey): The key of the multi parented element
    weights (Array[RigElementWeight]): The new weights to set for the parents
    initial (bool): If true the initial weights will be used
    affect_children (bool): If set to false children will not move (maintain global).

Returns:
    bool: Returns true if changing the weight was successful

<a id="unreal.RigHierarchy.set_parent_weight"></a>

#### set_parent_weight

```python
def set_parent_weight(child: RigElementKey,
                      parent: RigElementKey,
                      weight: RigElementWeight,
                      initial: bool = False,
                      affect_children: bool = True) -> bool
```

x.set_parent_weight(child, parent, weight, initial=False, affect_children=True) -> bool
Sets the weight of a parent below a multi parent element

Args:
    child (RigElementKey): The key of the multi parented element
    parent (RigElementKey): The key of the parent to look up the weight for
    weight (RigElementWeight): The new weight to set for the parent
    initial (bool): If true the initial weights will be used
    affect_children (bool): If set to false children will not move (maintain global).

Returns:
    bool: Returns true if changing the weight was successful

<a id="unreal.RigHierarchy.set_name_metadata"></a>

#### set_name_metadata

```python
def set_name_metadata(item: RigElementKey, metadata_name: Name,
                      value: Name) -> bool
```

x.set_name_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FName value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Name): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_name_array_metadata"></a>

#### set_name_array_metadata

```python
def set_name_array_metadata(item: RigElementKey, metadata_name: Name,
                            value: Array[Name]) -> bool
```

x.set_name_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FName array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[Name]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_local_transform_by_index"></a>

#### set_local_transform_by_index

```python
def set_local_transform_by_index(element_index: int,
                                 transform: Transform,
                                 initial: bool = False,
                                 affect_children: bool = True,
                                 setup_undo: bool = False,
                                 print_python_commands: bool = False) -> None
```

x.set_local_transform_by_index(element_index, transform, initial=False, affect_children=True, setup_undo=False, print_python_commands=False) -> None
Sets the local current or initial transform for a given element index.

Args:
    element_index (int32): The index of the element to set the transform for
    transform (Transform): The new transform value to set
    initial (bool): If true the initial transform will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_local_transform"></a>

#### set_local_transform

```python
def set_local_transform(key: RigElementKey,
                        transform: Transform,
                        initial: bool = False,
                        affect_children: bool = True,
                        setup_undo: bool = False,
                        print_python_commands: bool = False) -> None
```

x.set_local_transform(key, transform, initial=False, affect_children=True, setup_undo=False, print_python_commands=False) -> None
Sets the local current or initial transform for a given key.

Args:
    key (RigElementKey): The key to set the transform for
    transform (Transform): The new transform value to set
    initial (bool): If true the initial transform will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_linear_color_metadata"></a>

#### set_linear_color_metadata

```python
def set_linear_color_metadata(item: RigElementKey, metadata_name: Name,
                              value: LinearColor) -> bool
```

x.set_linear_color_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FLinearColor value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (LinearColor): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_linear_color_array_metadata"></a>

#### set_linear_color_array_metadata

```python
def set_linear_color_array_metadata(item: RigElementKey, metadata_name: Name,
                                    value: Array[LinearColor]) -> bool
```

x.set_linear_color_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a FLinearColor array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[LinearColor]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_int32_metadata"></a>

#### set_int32_metadata

```python
def set_int32_metadata(item: RigElementKey, metadata_name: Name,
                       value: int) -> bool
```

x.set_int32_metadata(item, metadata_name, value) -> bool
Sets the metadata to a int32 value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (int32): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_int32_array_metadata"></a>

#### set_int32_array_metadata

```python
def set_int32_array_metadata(item: RigElementKey, metadata_name: Name,
                             value: Array[int]) -> bool
```

x.set_int32_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a int32 array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[int32]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_global_transform_by_index"></a>

#### set_global_transform_by_index

```python
def set_global_transform_by_index(element_index: int,
                                  transform: Transform,
                                  initial: bool = False,
                                  affect_children: bool = True,
                                  setup_undo: bool = False,
                                  print_python_command: bool = False) -> None
```

x.set_global_transform_by_index(element_index, transform, initial=False, affect_children=True, setup_undo=False, print_python_command=False) -> None
Sets the global current or initial transform for a given element index.

Args:
    element_index (int32): The index of the element to set the transform for
    transform (Transform): The new transform value to set
    initial (bool): If true the initial transform will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_command (bool):

<a id="unreal.RigHierarchy.set_global_transform"></a>

#### set_global_transform

```python
def set_global_transform(key: RigElementKey,
                         transform: Transform,
                         initial: bool = False,
                         affect_children: bool = True,
                         setup_undo: bool = False,
                         print_python_command: bool = False) -> None
```

x.set_global_transform(key, transform, initial=False, affect_children=True, setup_undo=False, print_python_command=False) -> None
Sets the global current or initial transform for a given key.

Args:
    key (RigElementKey): The key to set the transform for
    transform (Transform): The new transform value to set
    initial (bool): If true the initial transform will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_command (bool):

<a id="unreal.RigHierarchy.set_float_metadata"></a>

#### set_float_metadata

```python
def set_float_metadata(item: RigElementKey, metadata_name: Name,
                       value: float) -> bool
```

x.set_float_metadata(item, metadata_name, value) -> bool
Sets the metadata to a float value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (float): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_float_array_metadata"></a>

#### set_float_array_metadata

```python
def set_float_array_metadata(item: RigElementKey, metadata_name: Name,
                             value: Array[float]) -> bool
```

x.set_float_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a float array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[float]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_curve_value_by_index"></a>

#### set_curve_value_by_index

```python
def set_curve_value_by_index(element_index: int,
                             value: float,
                             setup_undo: bool = False) -> None
```

x.set_curve_value_by_index(element_index, value, setup_undo=False) -> None
Sets a curve's value given its index

Args:
    element_index (int32): The index of the element to set the value for
    value (float): The value to set on the curve
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.set_curve_value"></a>

#### set_curve_value

```python
def set_curve_value(key: RigElementKey,
                    value: float,
                    setup_undo: bool = False) -> None
```

x.set_curve_value(key, value, setup_undo=False) -> None
Sets a curve's value given its key

Args:
    key (RigElementKey): The key of the element to set the value for
    value (float): The value to set on the curve
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.set_control_visibility_by_index"></a>

#### set_control_visibility_by_index

```python
def set_control_visibility_by_index(element_index: int,
                                    visibility: bool) -> None
```

x.set_control_visibility_by_index(element_index, visibility) -> None
Sets a control's current visibility based on a key

Args:
    element_index (int32): The index of the element to set the visibility for
    visibility (bool): The visibility to set on the control

<a id="unreal.RigHierarchy.set_control_visibility"></a>

#### set_control_visibility

```python
def set_control_visibility(key: RigElementKey, visibility: bool) -> None
```

x.set_control_visibility(key, visibility) -> None
Sets a control's current visibility based on a key

Args:
    key (RigElementKey): The key of the element to set the visibility for
    visibility (bool): The visibility to set on the control

<a id="unreal.RigHierarchy.set_control_value_by_index"></a>

#### set_control_value_by_index

```python
def set_control_value_by_index(
        element_index: int,
        value: RigControlValue,
        value_type: RigControlValueType = RigControlValueType.CURRENT,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> None
```

x.set_control_value_by_index(element_index, value, value_type=RigControlValueType.CURRENT, setup_undo=False, print_python_commands=False) -> None
Sets a control's current value given its index

Args:
    element_index (int32): The index of the element to set the current value for
    value (RigControlValue): The value to set on the control
    value_type (RigControlValueType): The type of value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_control_value"></a>

#### set_control_value

```python
def set_control_value(
        key: RigElementKey,
        value: RigControlValue,
        value_type: RigControlValueType = RigControlValueType.CURRENT,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> None
```

x.set_control_value(key, value, value_type=RigControlValueType.CURRENT, setup_undo=False, print_python_commands=False) -> None
Sets a control's current value given its key

Args:
    key (RigElementKey): The key of the element to set the current value for
    value (RigControlValue): The value to set on the control
    value_type (RigControlValueType): The type of value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_control_shape_transform_by_index"></a>

#### set_control_shape_transform_by_index

```python
def set_control_shape_transform_by_index(element_index: int,
                                         transform: Transform,
                                         initial: bool = False,
                                         setup_undo: bool = False) -> None
```

x.set_control_shape_transform_by_index(element_index, transform, initial=False, setup_undo=False) -> None
Sets the local shape transform for a given control element by index

Args:
    element_index (int32): The index of the control element to set the shape transform for
    transform (Transform): The new local shape transform value to set
    initial (bool): If true the initial value will be used
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.set_control_shape_transform"></a>

#### set_control_shape_transform

```python
def set_control_shape_transform(key: RigElementKey,
                                transform: Transform,
                                initial: bool = False,
                                setup_undo: bool = False) -> None
```

x.set_control_shape_transform(key, transform, initial=False, setup_undo=False) -> None
Sets the shape transform for a given control element by key

Args:
    key (RigElementKey): The key of the control element to set the shape transform for
    transform (Transform): The new shape transform value to set
    initial (bool): If true the initial value will be used
    setup_undo (bool): If true the transform stack will be setup for undo / redo

<a id="unreal.RigHierarchy.set_control_settings_by_index"></a>

#### set_control_settings_by_index

```python
def set_control_settings_by_index(element_index: int,
                                  settings: RigControlSettings,
                                  setup_undo: bool = False,
                                  force: bool = False,
                                  print_python_commands: bool = False) -> None
```

x.set_control_settings_by_index(element_index, settings, setup_undo=False, force=False, print_python_commands=False) -> None
Sets the control settings for a given control element by index

Args:
    element_index (int32): The index of the control element to set the settings for
    settings (RigControlSettings): The new control settings value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    force (bool): 
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_control_settings"></a>

#### set_control_settings

```python
def set_control_settings(key: RigElementKey,
                         settings: RigControlSettings,
                         setup_undo: bool = False,
                         force: bool = False,
                         print_python_commands: bool = False) -> None
```

x.set_control_settings(key, settings, setup_undo=False, force=False, print_python_commands=False) -> None
Sets the control settings for a given control element by key

Args:
    key (RigElementKey): The key of the control element to set the settings for
    settings (RigControlSettings): The new control settings value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    force (bool): 
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_control_preferred_rotator_by_index"></a>

#### set_control_preferred_rotator_by_index

```python
def set_control_preferred_rotator_by_index(
        element_index: int,
        rotator: Rotator,
        initial: bool = False,
        fix_euler_flips: bool = False) -> None
```

x.set_control_preferred_rotator_by_index(element_index, rotator, initial=False, fix_euler_flips=False) -> None
Sets a control's preferred rotator (local transform rotation)

Args:
    element_index (int32): The element index to look up
    rotator (Rotator): The new preferred rotator to set
    initial (bool): If true we'll return the preferred rotator for the initial - otherwise current transform
    fix_euler_flips (bool): If true the new rotator value will use the shortest path

<a id="unreal.RigHierarchy.set_control_preferred_rotator"></a>

#### set_control_preferred_rotator

```python
def set_control_preferred_rotator(key: RigElementKey,
                                  rotator: Rotator,
                                  initial: bool = False,
                                  fix_euler_flips: bool = False) -> None
```

x.set_control_preferred_rotator(key, rotator, initial=False, fix_euler_flips=False) -> None
Sets a control's preferred rotator (local transform rotation)

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    rotator (Rotator): The new preferred rotator to set
    initial (bool): If true we'll return the preferred rotator for the initial - otherwise current transform
    fix_euler_flips (bool): If true the new rotator value will use the shortest path

<a id="unreal.RigHierarchy.set_control_preferred_rotation_order_by_index"></a>

#### set_control_preferred_rotation_order_by_index

```python
def set_control_preferred_rotation_order_by_index(
        element_index: int, rotation_order: EulerRotationOrder) -> None
```

x.set_control_preferred_rotation_order_by_index(element_index, rotation_order) -> None
Sets a control's preferred euler rotation order

Args:
    element_index (int32): The element index to look up
    rotation_order (EulerRotationOrder): The rotation order to use when setting the euler angles

<a id="unreal.RigHierarchy.set_control_preferred_rotation_order"></a>

#### set_control_preferred_rotation_order

```python
def set_control_preferred_rotation_order(
        key: RigElementKey, rotation_order: EulerRotationOrder) -> None
```

x.set_control_preferred_rotation_order(key, rotation_order) -> None
Sets a control's preferred euler rotation order

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    rotation_order (EulerRotationOrder): The rotation order to use when setting the euler angles

<a id="unreal.RigHierarchy.set_control_preferred_euler_angles_by_index"></a>

#### set_control_preferred_euler_angles_by_index

```python
def set_control_preferred_euler_angles_by_index(
        element_index: int,
        euler_angles: Vector,
        rotation_order: EulerRotationOrder,
        initial: bool = False,
        fix_euler_flips: bool = False) -> None
```

x.set_control_preferred_euler_angles_by_index(element_index, euler_angles, rotation_order, initial=False, fix_euler_flips=False) -> None
Sets a control's preferred euler angles (local transform rotation)

Args:
    element_index (int32): The element index to look up
    euler_angles (Vector): The new preferred euler angles to set
    rotation_order (EulerRotationOrder): The rotation order to use when setting the euler angles
    initial (bool): If true we'll return the preferred euler angles for the initial - otherwise current transform
    fix_euler_flips (bool): If true the new euler angles value will use the shortest path

<a id="unreal.RigHierarchy.set_control_preferred_euler_angles"></a>

#### set_control_preferred_euler_angles

```python
def set_control_preferred_euler_angles(key: RigElementKey,
                                       euler_angles: Vector,
                                       rotation_order: EulerRotationOrder,
                                       initial: bool = False,
                                       fix_euler_flips: bool = False) -> None
```

x.set_control_preferred_euler_angles(key, euler_angles, rotation_order, initial=False, fix_euler_flips=False) -> None
Sets a control's preferred euler angles (local transform rotation)

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    euler_angles (Vector): The new preferred euler angles to set
    rotation_order (EulerRotationOrder): The rotation order to use when setting the euler angles
    initial (bool): If true we'll return the preferred euler angles for the initial - otherwise current transform
    fix_euler_flips (bool): If true the new euler angles value will use the shortest path

<a id="unreal.RigHierarchy.set_control_offset_transform_by_index"></a>

#### set_control_offset_transform_by_index

```python
def set_control_offset_transform_by_index(
        element_index: int,
        transform: Transform,
        initial: bool = False,
        affect_children: bool = True,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> None
```

x.set_control_offset_transform_by_index(element_index, transform, initial=False, affect_children=True, setup_undo=False, print_python_commands=False) -> None
Sets the local offset transform for a given control element by index

Args:
    element_index (int32): The index of the control element to set the offset transform for
    transform (Transform): The new local offset transform value to set
    initial (bool): If true the initial value will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_control_offset_transform"></a>

#### set_control_offset_transform

```python
def set_control_offset_transform(key: RigElementKey,
                                 transform: Transform,
                                 initial: bool = False,
                                 affect_children: bool = True,
                                 setup_undo: bool = False,
                                 print_python_commands: bool = False) -> None
```

x.set_control_offset_transform(key, transform, initial=False, affect_children=True, setup_undo=False, print_python_commands=False) -> None
Sets the offset transform for a given control element by key

Args:
    key (RigElementKey): The key of the control element to set the offset transform for
    transform (Transform): The new offset transform value to set
    initial (bool): If true the initial value will be used
    affect_children (bool): If set to false children will not move (maintain global).
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_connector_settings_by_index"></a>

#### set_connector_settings_by_index

```python
def set_connector_settings_by_index(
        element_index: int,
        settings: RigConnectorSettings,
        setup_undo: bool = False,
        force: bool = False,
        print_python_commands: bool = False) -> None
```

x.set_connector_settings_by_index(element_index, settings, setup_undo=False, force=False, print_python_commands=False) -> None
Sets the connector settings for a given connector element by index

Args:
    element_index (int32): The index of the connector element to set the settings for
    settings (RigConnectorSettings): The new connector settings value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    force (bool): 
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_connector_settings"></a>

#### set_connector_settings

```python
def set_connector_settings(key: RigElementKey,
                           settings: RigConnectorSettings,
                           setup_undo: bool = False,
                           force: bool = False,
                           print_python_commands: bool = False) -> None
```

x.set_connector_settings(key, settings, setup_undo=False, force=False, print_python_commands=False) -> None
Sets the connector settings for a given connector element by key

Args:
    key (RigElementKey): The key of the connector element to set the settings for
    settings (RigConnectorSettings): The new connector settings value to set
    setup_undo (bool): If true the transform stack will be setup for undo / redo
    force (bool): 
    print_python_commands (bool):

<a id="unreal.RigHierarchy.set_bool_metadata"></a>

#### set_bool_metadata

```python
def set_bool_metadata(item: RigElementKey, metadata_name: Name,
                      value: bool) -> bool
```

x.set_bool_metadata(item, metadata_name, value) -> bool
Sets the metadata to a bool value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (bool): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.set_bool_array_metadata"></a>

#### set_bool_array_metadata

```python
def set_bool_array_metadata(item: RigElementKey, metadata_name: Name,
                            value: Array[bool]) -> bool
```

x.set_bool_array_metadata(item, metadata_name, value) -> bool
Sets the metadata to a bool array value

Args:
    item (RigElementKey): The element key to set the metadata for
    metadata_name (Name): The name of the metadata to set
    value (Array[bool]): The value to set

Returns:
    bool: Returns true if setting the metadata was successful

<a id="unreal.RigHierarchy.send_auto_key_event"></a>

#### send_auto_key_event

```python
def send_auto_key_event(element: RigElementKey,
                        offset_in_seconds: float = 0.000000,
                        asynchronous: bool = True) -> None
```

x.send_auto_key_event(element, offset_in_seconds=0.000000, asynchronous=True) -> None
Sends an autokey event from the hierarchy to the world

Args:
    element (RigElementKey): The element to send the autokey for
    offset_in_seconds (float): The time offset in seconds
    asynchronous (bool): If set to true the event will go on a thread safe queue

<a id="unreal.RigHierarchy.restore_sockets_from_states"></a>

#### restore_sockets_from_states

```python
def restore_sockets_from_states(
        states: Array[RigSocketState],
        setup_undo_redo: bool = False) -> Array[RigElementKey]
```

x.restore_sockets_from_states(states, setup_undo_redo=False) -> Array[RigElementKey]
Try to restore the sockets from the state structs

Args:
    states (Array[RigSocketState]): 
    setup_undo_redo (bool): 

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.restore_connectors_from_states"></a>

#### restore_connectors_from_states

```python
def restore_connectors_from_states(
        states: Array[RigConnectorState],
        setup_undo_redo: bool = False) -> Array[RigElementKey]
```

x.restore_connectors_from_states(states, setup_undo_redo=False) -> Array[RigElementKey]
Try to restore the connectors from the state structs

Args:
    states (Array[RigConnectorState]): 
    setup_undo_redo (bool): 

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Resets the hierarchy to the state of its default. This refers to the
hierarchy on the default object.

<a id="unreal.RigHierarchy.reset_pose_to_initial"></a>

#### reset_pose_to_initial

```python
def reset_pose_to_initial(type_filter: RigElementType) -> None
```

x.reset_pose_to_initial(type_filter) -> None
Resets the current pose of a filtered list of elements to the initial / ref pose.

Args:
    type_filter (RigElementType):

<a id="unreal.RigHierarchy.reset_curve_values"></a>

#### reset_curve_values

```python
def reset_curve_values() -> None
```

x.reset_curve_values() -> None
Resets all curves to 0.0

<a id="unreal.RigHierarchy.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Clears the whole hierarchy and removes all elements.

<a id="unreal.RigHierarchy.remove_metadata"></a>

#### remove_metadata

```python
def remove_metadata(item: RigElementKey, metadata_name: Name) -> bool
```

x.remove_metadata(item, metadata_name) -> bool
Removes the metadata under a given element

Args:
    item (RigElementKey): The element key to search under
    metadata_name (Name): The name of the metadata to remove

Returns:
    bool:

<a id="unreal.RigHierarchy.remove_all_metadata"></a>

#### remove_all_metadata

```python
def remove_all_metadata(item: RigElementKey) -> bool
```

x.remove_all_metadata(item) -> bool
Removes all of the metadata under a given item

Args:
    item (RigElementKey): The element key to search under

Returns:
    bool:

<a id="unreal.RigHierarchy.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Returns the number of elements in the Hierarchy.

Returns:
    int32: The number of elements in the Hierarchy

<a id="unreal.RigHierarchy.make_control_value_from_vector2d"></a>

#### make_control_value_from_vector2d

```python
@classmethod
def make_control_value_from_vector2d(cls, value: Vector2D) -> RigControlValue
```

X.make_control_value_from_vector2d(value) -> RigControlValue
Creates a rig control value from a FVector2D value

Args:
    value (Vector2D): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_vector"></a>

#### make_control_value_from_vector

```python
@classmethod
def make_control_value_from_vector(cls, value: Vector) -> RigControlValue
```

X.make_control_value_from_vector(value) -> RigControlValue
Creates a rig control value from a FVector value

Args:
    value (Vector): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_transform_no_scale"></a>

#### make_control_value_from_transform_no_scale

```python
@classmethod
def make_control_value_from_transform_no_scale(
        cls, value: TransformNoScale) -> RigControlValue
```

X.make_control_value_from_transform_no_scale(value) -> RigControlValue
Creates a rig control value from a FTransformNoScale value

Args:
    value (TransformNoScale): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_transform"></a>

#### make_control_value_from_transform

```python
@classmethod
def make_control_value_from_transform(cls,
                                      value: Transform) -> RigControlValue
```

X.make_control_value_from_transform(value) -> RigControlValue
Creates a rig control value from a FTransform value

Args:
    value (Transform): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_rotator"></a>

#### make_control_value_from_rotator

```python
@classmethod
def make_control_value_from_rotator(cls, value: Rotator) -> RigControlValue
```

X.make_control_value_from_rotator(value) -> RigControlValue
Creates a rig control value from a FRotator value

Args:
    value (Rotator): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_int"></a>

#### make_control_value_from_int

```python
@classmethod
def make_control_value_from_int(cls, value: int) -> RigControlValue
```

X.make_control_value_from_int(value) -> RigControlValue
Creates a rig control value from a int32 value

Args:
    value (int32): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_float"></a>

#### make_control_value_from_float

```python
@classmethod
def make_control_value_from_float(cls, value: float) -> RigControlValue
```

X.make_control_value_from_float(value) -> RigControlValue
Creates a rig control value from a float value

Args:
    value (float): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_euler_transform"></a>

#### make_control_value_from_euler_transform

```python
@classmethod
def make_control_value_from_euler_transform(
        cls, value: EulerTransform) -> RigControlValue
```

X.make_control_value_from_euler_transform(value) -> RigControlValue
Creates a rig control value from a FEulerTransform value

Args:
    value (EulerTransform): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.make_control_value_from_bool"></a>

#### make_control_value_from_bool

```python
@classmethod
def make_control_value_from_bool(cls, value: bool) -> RigControlValue
```

X.make_control_value_from_bool(value) -> RigControlValue
Creates a rig control value from a bool value

Args:
    value (bool): The value to create the rig control value from

Returns:
    RigControlValue: The converted control rig val ue

<a id="unreal.RigHierarchy.is_valid_index"></a>

#### is_valid_index

```python
def is_valid_index(element_index: int) -> bool
```

x.is_valid_index(element_index) -> bool
Returns true if the provided element index is valid

Args:
    element_index (int32): The index to validate

Returns:
    bool: Returns true if the provided element index is valid

<a id="unreal.RigHierarchy.is_selected_by_index"></a>

#### is_selected_by_index

```python
def is_selected_by_index(index: int) -> bool
```

x.is_selected_by_index(index) -> bool
Returns true if a given element is selected

Args:
    index (int32): The index to check

Returns:
    bool: true if a given element is selected

<a id="unreal.RigHierarchy.is_selected"></a>

#### is_selected

```python
def is_selected(key: RigElementKey) -> bool
```

x.is_selected(key) -> bool
Returns true if a given element is selected

Args:
    key (RigElementKey): The key to check

Returns:
    bool: true if a given element is selected

<a id="unreal.RigHierarchy.is_procedural"></a>

#### is_procedural

```python
def is_procedural(key: RigElementKey) -> bool
```

x.is_procedural(key) -> bool
Returns true if the provided element is procedural.

Args:
    key (RigElementKey): The key to validate

Returns:
    bool: Returns true if the element is procedural

<a id="unreal.RigHierarchy.is_parented_to"></a>

#### is_parented_to

```python
def is_parented_to(child: RigElementKey, parent: RigElementKey) -> bool
```

x.is_parented_to(child, parent) -> bool
Returns true if an element is parented to another element

Args:
    child (RigElementKey): The key of the child element to check for a parent
    parent (RigElementKey): The key of the parent element to check for

Returns:
    bool: True if the given parent and given child have a parent-child relationship

<a id="unreal.RigHierarchy.is_curve_value_set_by_index"></a>

#### is_curve_value_set_by_index

```python
def is_curve_value_set_by_index(element_index: int) -> bool
```

x.is_curve_value_set_by_index(element_index) -> bool
Returns a curve's value given its index

Args:
    element_index (int32): The index of the element to retrieve the value for

Returns:
    bool: Returns true if the value is set, false otherwise.

<a id="unreal.RigHierarchy.is_curve_value_set"></a>

#### is_curve_value_set

```python
def is_curve_value_set(key: RigElementKey) -> bool
```

x.is_curve_value_set(key) -> bool
Returns whether a curve's value is set, given its key

Args:
    key (RigElementKey): The key of the element to retrieve the value for

Returns:
    bool: Returns true if the value is set, false otherwise.

<a id="unreal.RigHierarchy.is_controller_available"></a>

#### is_controller_available

```python
def is_controller_available() -> bool
```

x.is_controller_available() -> bool
Returns true if the hierarchy controller is currently available
The controller may not be available during certain events.
If the controller is not available then GetController() will return nullptr.

Returns:
    bool:

<a id="unreal.RigHierarchy.has_tag"></a>

#### has_tag

```python
def has_tag(item: RigElementKey, tag: Name) -> bool
```

x.has_tag(item, tag) -> bool
* Returns true if a given item has a certain tag
*

Args:
    item (RigElementKey): The item to return the tags for *
    tag (Name): The tag to check

Returns:
    bool:

<a id="unreal.RigHierarchy.get_vector_metadata"></a>

#### get_vector_metadata

```python
def get_vector_metadata(item: RigElementKey, metadata_name: Name,
                        default_value: Vector) -> Vector
```

x.get_vector_metadata(item, metadata_name, default_value) -> Vector
Queries and returns the value of FVector metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (Vector): The default value to fall back on

Returns:
    Vector:

<a id="unreal.RigHierarchy.get_vector_from_control_value"></a>

#### get_vector_from_control_value

```python
@classmethod
def get_vector_from_control_value(cls, value: RigControlValue) -> Vector
```

X.get_vector_from_control_value(value) -> Vector
Returns the contained FVector value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    Vector: The converted FVector value

<a id="unreal.RigHierarchy.get_vector_array_metadata"></a>

#### get_vector_array_metadata

```python
def get_vector_array_metadata(item: RigElementKey,
                              metadata_name: Name) -> Array[Vector]
```

x.get_vector_array_metadata(item, metadata_name) -> Array[Vector]
Queries and returns the value of FVector array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[Vector]:

<a id="unreal.RigHierarchy.get_vector2d_from_control_value"></a>

#### get_vector2d_from_control_value

```python
@classmethod
def get_vector2d_from_control_value(cls, value: RigControlValue) -> Vector2D
```

X.get_vector2d_from_control_value(value) -> Vector2D
Returns the contained FVector2D value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    Vector2D: The converted FVector2D value

<a id="unreal.RigHierarchy.get_transform_no_scale_from_control_value"></a>

#### get_transform_no_scale_from_control_value

```python
@classmethod
def get_transform_no_scale_from_control_value(
        cls, value: RigControlValue) -> TransformNoScale
```

X.get_transform_no_scale_from_control_value(value) -> TransformNoScale
Returns the contained FTransformNoScale value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    TransformNoScale: The converted FTransformNoScale value

<a id="unreal.RigHierarchy.get_transform_metadata"></a>

#### get_transform_metadata

```python
def get_transform_metadata(item: RigElementKey, metadata_name: Name,
                           default_value: Transform) -> Transform
```

x.get_transform_metadata(item, metadata_name, default_value) -> Transform
Queries and returns the value of FTransform metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (Transform): The default value to fall back on

Returns:
    Transform:

<a id="unreal.RigHierarchy.get_transform_from_control_value"></a>

#### get_transform_from_control_value

```python
@classmethod
def get_transform_from_control_value(cls, value: RigControlValue) -> Transform
```

X.get_transform_from_control_value(value) -> Transform
Returns the contained FTransform value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    Transform: The converted FTransform value

<a id="unreal.RigHierarchy.get_transform_array_metadata"></a>

#### get_transform_array_metadata

```python
def get_transform_array_metadata(item: RigElementKey,
                                 metadata_name: Name) -> Array[Transform]
```

x.get_transform_array_metadata(item, metadata_name) -> Array[Transform]
Queries and returns the value of FTransform array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[Transform]:

<a id="unreal.RigHierarchy.get_tags"></a>

#### get_tags

```python
def get_tags(item: RigElementKey) -> Array[Name]
```

x.get_tags(item) -> Array[Name]
* Returns the tags for a given item
*

Args:
    item (RigElementKey): The item to return the tags for

Returns:
    Array[Name]:

<a id="unreal.RigHierarchy.get_socket_states"></a>

#### get_socket_states

```python
def get_socket_states() -> Array[RigSocketState]
```

x.get_socket_states() -> Array[RigSocketState]
Returns all of the sockets' state

Returns:
    Array[RigSocketState]:

<a id="unreal.RigHierarchy.get_sockets"></a>

#### get_sockets

```python
def get_sockets(traverse: bool = True) -> Array[RigElementKey]
```

x.get_sockets(traverse=True) -> Array[RigElementKey]
Returns all Socket elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_selected_keys"></a>

#### get_selected_keys

```python
def get_selected_keys(
        type_filter: RigElementType = RigElementType.ALL
) -> Array[RigElementKey]
```

x.get_selected_keys(type_filter=RigElementType.ALL) -> Array[RigElementKey]
Returns the keys of selected elements
InTypeFilter: The types to retrieve the selection for

Args:
    type_filter (RigElementType): 

Returns:
    Array[RigElementKey]: An array of the currently selected elements

<a id="unreal.RigHierarchy.get_rule_manager"></a>

#### get_rule_manager

```python
def get_rule_manager(create_if_needed: bool = True) -> ModularRigRuleManager
```

x.get_rule_manager(create_if_needed=True) -> ModularRigRuleManager
Returns a rule manager for this hierarchy
Note: If the manager is not available this will return nullptr
even if the bCreateIfNeeded flag is set to true.

Args:
    create_if_needed (bool): Creates a controller if needed

Returns:
    ModularRigRuleManager: The Controller for this hierarchy

<a id="unreal.RigHierarchy.get_rotator_metadata"></a>

#### get_rotator_metadata

```python
def get_rotator_metadata(item: RigElementKey, metadata_name: Name,
                         default_value: Rotator) -> Rotator
```

x.get_rotator_metadata(item, metadata_name, default_value) -> Rotator
Queries and returns the value of FRotator metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (Rotator): The default value to fall back on

Returns:
    Rotator:

<a id="unreal.RigHierarchy.get_rotator_from_control_value"></a>

#### get_rotator_from_control_value

```python
@classmethod
def get_rotator_from_control_value(cls, value: RigControlValue) -> Rotator
```

X.get_rotator_from_control_value(value) -> Rotator
Returns the contained FRotator value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    Rotator: The converted FRotator value

<a id="unreal.RigHierarchy.get_rotator_array_metadata"></a>

#### get_rotator_array_metadata

```python
def get_rotator_array_metadata(item: RigElementKey,
                               metadata_name: Name) -> Array[Rotator]
```

x.get_rotator_array_metadata(item, metadata_name) -> Array[Rotator]
Queries and returns the value of FRotator array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[Rotator]:

<a id="unreal.RigHierarchy.get_root_elements"></a>

#### get_root_elements

```python
def get_root_elements() -> Array[RigElementKey]
```

x.get_root_elements() -> Array[RigElementKey]
Returns all root element keys

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_rig_element_key_metadata"></a>

#### get_rig_element_key_metadata

```python
def get_rig_element_key_metadata(
        item: RigElementKey, metadata_name: Name,
        default_value: RigElementKey) -> RigElementKey
```

x.get_rig_element_key_metadata(item, metadata_name, default_value) -> RigElementKey
Queries and returns the value of FRigElementKey metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (RigElementKey): The default value to fall back on

Returns:
    RigElementKey:

<a id="unreal.RigHierarchy.get_rig_element_key_array_metadata"></a>

#### get_rig_element_key_array_metadata

```python
def get_rig_element_key_array_metadata(
        item: RigElementKey, metadata_name: Name) -> Array[RigElementKey]
```

x.get_rig_element_key_array_metadata(item, metadata_name) -> Array[RigElementKey]
Queries and returns the value of FRigElementKey array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_references"></a>

#### get_references

```python
def get_references(traverse: bool = True) -> Array[RigElementKey]
```

x.get_references(traverse=True) -> Array[RigElementKey]
Returns all references

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_quat_metadata"></a>

#### get_quat_metadata

```python
def get_quat_metadata(item: RigElementKey, metadata_name: Name,
                      default_value: Quat) -> Quat
```

x.get_quat_metadata(item, metadata_name, default_value) -> Quat
Queries and returns the value of FQuat metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (Quat): The default value to fall back on

Returns:
    Quat:

<a id="unreal.RigHierarchy.get_quat_array_metadata"></a>

#### get_quat_array_metadata

```python
def get_quat_array_metadata(item: RigElementKey,
                            metadata_name: Name) -> Array[Quat]
```

x.get_quat_array_metadata(item, metadata_name) -> Array[Quat]
Queries and returns the value of FQuat array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[Quat]:

<a id="unreal.RigHierarchy.get_previous_parent"></a>

#### get_previous_parent

```python
def get_previous_parent(key: RigElementKey) -> RigElementKey
```

x.get_previous_parent(key) -> RigElementKey
Returns the previous parent of an element prior to a reparent operation

Args:
    key (RigElementKey): The key of the element to request the old parent  for

Returns:
    RigElementKey:

<a id="unreal.RigHierarchy.get_previous_name"></a>

#### get_previous_name

```python
def get_previous_name(key: RigElementKey) -> Name
```

x.get_previous_name(key) -> Name
Returns the previous name of an element prior to a rename operation

Args:
    key (RigElementKey): The key of the element to request the old name for

Returns:
    Name:

<a id="unreal.RigHierarchy.get_pose"></a>

#### get_pose

```python
def get_pose(initial: bool = False,
             include_transient_controls: bool = True) -> RigPose
```

x.get_pose(initial=False, include_transient_controls=True) -> RigPose
Returns the current / initial pose of the hierarchy

Args:
    initial (bool): If set to true the initial pose will be returned
    include_transient_controls (bool): If true the transient controls will be included in the pose

Returns:
    RigPose: The pose of the hierarchy

<a id="unreal.RigHierarchy.get_physics_keys"></a>

#### get_physics_keys

```python
def get_physics_keys(traverse: bool = True) -> Array[RigElementKey]
```

x.get_physics_keys(traverse=True) -> Array[RigElementKey]
Returns all Physics elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_parent_weight_array"></a>

#### get_parent_weight_array

```python
def get_parent_weight_array(child: RigElementKey,
                            initial: bool = False) -> Array[RigElementWeight]
```

x.get_parent_weight_array(child, initial=False) -> Array[RigElementWeight]
Returns the weights of all parents below a multi parent element

Args:
    child (RigElementKey): The key of the multi parented element
    initial (bool): If true the initial weights will be used

Returns:
    Array[RigElementWeight]: Returns the weight of a parent below a multi parent element, or FLT_MAX if the parent is invalid

<a id="unreal.RigHierarchy.get_parent_weight"></a>

#### get_parent_weight

```python
def get_parent_weight(child: RigElementKey,
                      parent: RigElementKey,
                      initial: bool = False) -> RigElementWeight
```

x.get_parent_weight(child, parent, initial=False) -> RigElementWeight
Returns the weight of a parent below a multi parent element

Args:
    child (RigElementKey): The key of the multi parented element
    parent (RigElementKey): The key of the parent to look up the weight for
    initial (bool): If true the initial weights will be used

Returns:
    RigElementWeight: Returns the weight of a parent below a multi parent element, or FLT_MAX if the parent is invalid

<a id="unreal.RigHierarchy.get_parent_transform_by_index"></a>

#### get_parent_transform_by_index

```python
def get_parent_transform_by_index(element_index: int,
                                  initial: bool = False) -> Transform
```

x.get_parent_transform_by_index(element_index, initial=False) -> Transform
Returns the global current or initial value for a given element index.
If the element does not have a parent FTransform::Identity will be returned.

Args:
    element_index (int32): The index of the element to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The element's parent's global current or initial transform's value.

<a id="unreal.RigHierarchy.get_parent_transform"></a>

#### get_parent_transform

```python
def get_parent_transform(key: RigElementKey,
                         initial: bool = False) -> Transform
```

x.get_parent_transform(key, initial=False) -> Transform
Returns the global current or initial value for a given key.
If the element does not have a parent FTransform::Identity will be returned.

Args:
    key (RigElementKey): The key of the element to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The element's parent's global current or initial transform's value.

<a id="unreal.RigHierarchy.get_parents"></a>

#### get_parents

```python
def get_parents(key: RigElementKey,
                recursive: bool = False) -> Array[RigElementKey]
```

x.get_parents(key, recursive=False) -> Array[RigElementKey]
Returns the parent elements of a given element key

Args:
    key (RigElementKey): The key of the element to retrieve the parents for
    recursive (bool): If set to true parents of parents will also be returned

Returns:
    Array[RigElementKey]: Returns the parent elements

<a id="unreal.RigHierarchy.get_number_of_parents"></a>

#### get_number_of_parents

```python
def get_number_of_parents(key: RigElementKey) -> int
```

x.get_number_of_parents(key) -> int32
Returns the number of parents of an element

Args:
    key (RigElementKey): The key of the element to retrieve the number of parents for

Returns:
    int32: Returns the number of parents of an element

<a id="unreal.RigHierarchy.get_nulls"></a>

#### get_nulls

```python
def get_nulls(traverse: bool = True) -> Array[RigElementKey]
```

x.get_nulls(traverse=True) -> Array[RigElementKey]
Returns all Null elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_name_space_f_name"></a>

#### get_name_space_f_name

```python
def get_name_space_f_name(item: RigElementKey) -> Name
```

x.get_name_space_f_name(item) -> Name
Returns the namespace of an element belong to (or NAME_None in case the element doesn't belong to a module / namespace)

Args:
    item (RigElementKey): 

Returns:
    Name: The namespace the element belongs to (or NAME_None)

<a id="unreal.RigHierarchy.get_name_space"></a>

#### get_name_space

```python
def get_name_space(item: RigElementKey) -> str
```

x.get_name_space(item) -> str
Returns the namespace of an element belong to (or an empty string in case the element doesn't belong to a module / namespace)

Args:
    item (RigElementKey): 

Returns:
    str: The namespace the element belongs to (or empty string)

<a id="unreal.RigHierarchy.get_name_metadata"></a>

#### get_name_metadata

```python
def get_name_metadata(item: RigElementKey, metadata_name: Name,
                      default_value: Name) -> Name
```

x.get_name_metadata(item, metadata_name, default_value) -> Name
Queries and returns the value of FName metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (Name): The default value to fall back on

Returns:
    Name:

<a id="unreal.RigHierarchy.get_name_array_metadata"></a>

#### get_name_array_metadata

```python
def get_name_array_metadata(item: RigElementKey,
                            metadata_name: Name) -> Array[Name]
```

x.get_name_array_metadata(item, metadata_name) -> Array[Name]
Queries and returns the value of FName array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[Name]:

<a id="unreal.RigHierarchy.get_module_path_f_name"></a>

#### get_module_path_f_name

```python
def get_module_path_f_name(item: RigElementKey) -> Name
```

x.get_module_path_f_name(item) -> Name
Returns the path of the module an element belong to (or NAME_None in case the element doesn't belong to a module)

Args:
    item (RigElementKey): 

Returns:
    Name: The path the element belongs to (or NAME_None)

<a id="unreal.RigHierarchy.get_module_path"></a>

#### get_module_path

```python
def get_module_path(item: RigElementKey) -> str
```

x.get_module_path(item) -> str
Returns the path of the module an element belong to (or an empty string in case the element doesn't belong to a module)

Args:
    item (RigElementKey): 

Returns:
    str: The path the element belongs to (or empty string)

<a id="unreal.RigHierarchy.get_metadata_type"></a>

#### get_metadata_type

```python
def get_metadata_type(item: RigElementKey,
                      metadata_name: Name) -> RigMetadataType
```

x.get_metadata_type(item, metadata_name) -> RigMetadataType
Returns the type of metadata given its name the item it is stored under

Args:
    item (RigElementKey): The element key to return the metadata type for
    metadata_name (Name): The name of the metadata to return the type for

Returns:
    RigMetadataType:

<a id="unreal.RigHierarchy.get_metadata_names"></a>

#### get_metadata_names

```python
def get_metadata_names(item: RigElementKey) -> Array[Name]
```

x.get_metadata_names(item) -> Array[Name]
Returns the name of metadata for a given element

Args:
    item (RigElementKey): The element key to return the metadata keys for

Returns:
    Array[Name]:

<a id="unreal.RigHierarchy.get_local_transform_by_index"></a>

#### get_local_transform_by_index

```python
def get_local_transform_by_index(element_index: int,
                                 initial: bool = False) -> Transform
```

x.get_local_transform_by_index(element_index, initial=False) -> Transform
Returns the local current or initial value for a element index.
If the index is invalid FTransform::Identity will be returned.

Args:
    element_index (int32): The index to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The local current or initial transform's value.

<a id="unreal.RigHierarchy.get_local_transform"></a>

#### get_local_transform

```python
def get_local_transform(key: RigElementKey,
                        initial: bool = False) -> Transform
```

x.get_local_transform(key, initial=False) -> Transform
Returns the local current or initial value for a given key.
If the key is invalid FTransform::Identity will be returned.

Args:
    key (RigElementKey): The key to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The local current or initial transform's value.

<a id="unreal.RigHierarchy.get_local_index"></a>

#### get_local_index

```python
def get_local_index(key: RigElementKey) -> int
```

x.get_local_index(key) -> int32
Returns the index of an element given its key within its default parent (or root)

Args:
    key (RigElementKey): The key of the element to retrieve the index for

Returns:
    int32: The index of the element or INDEX_NONE

<a id="unreal.RigHierarchy.get_local_control_shape_transform_by_index"></a>

#### get_local_control_shape_transform_by_index

```python
def get_local_control_shape_transform_by_index(element_index: int,
                                               initial: bool = False
                                               ) -> Transform
```

x.get_local_control_shape_transform_by_index(element_index, initial=False) -> Transform
Returns the local shape transform for a given control element.

Args:
    element_index (int32): The index of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The local shape transform

<a id="unreal.RigHierarchy.get_local_control_shape_transform"></a>

#### get_local_control_shape_transform

```python
def get_local_control_shape_transform(key: RigElementKey,
                                      initial: bool = False) -> Transform
```

x.get_local_control_shape_transform(key, initial=False) -> Transform
Returns the local shape transform for a given control element.

Args:
    key (RigElementKey): The key of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The local shape transform

<a id="unreal.RigHierarchy.get_linear_color_metadata"></a>

#### get_linear_color_metadata

```python
def get_linear_color_metadata(item: RigElementKey, metadata_name: Name,
                              default_value: LinearColor) -> LinearColor
```

x.get_linear_color_metadata(item, metadata_name, default_value) -> LinearColor
Queries and returns the value of FLinearColor metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (LinearColor): The default value to fall back on

Returns:
    LinearColor:

<a id="unreal.RigHierarchy.get_linear_color_array_metadata"></a>

#### get_linear_color_array_metadata

```python
def get_linear_color_array_metadata(item: RigElementKey,
                                    metadata_name: Name) -> Array[LinearColor]
```

x.get_linear_color_array_metadata(item, metadata_name) -> Array[LinearColor]
Queries and returns the value of FLinearColor array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[LinearColor]:

<a id="unreal.RigHierarchy.get_keys"></a>

#### get_keys

```python
def get_keys(element_indices: Array[int]) -> Array[RigElementKey]
```

x.get_keys(element_indices) -> Array[RigElementKey]
Returns the keys of an array of indices

Args:
    element_indices (Array[int32]): The indices to retrieve the keys for

Returns:
    Array[RigElementKey]: The keys of the elements given the indices

<a id="unreal.RigHierarchy.get_key"></a>

#### get_key

```python
def get_key(element_index: int) -> RigElementKey
```

x.get_key(element_index) -> RigElementKey
Returns the key of an element given its index

Args:
    element_index (int32): The index of the element to retrieve the key for

Returns:
    RigElementKey: The key of an element given its index

<a id="unreal.RigHierarchy.get_int_from_control_value"></a>

#### get_int_from_control_value

```python
@classmethod
def get_int_from_control_value(cls, value: RigControlValue) -> int
```

X.get_int_from_control_value(value) -> int32
Returns the contained int32 value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    int32: The converted int32 value

<a id="unreal.RigHierarchy.get_int32_metadata"></a>

#### get_int32_metadata

```python
def get_int32_metadata(item: RigElementKey, metadata_name: Name,
                       default_value: int) -> int
```

x.get_int32_metadata(item, metadata_name, default_value) -> int32
Queries and returns the value of int32 metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (int32): The default value to fall back on

Returns:
    int32:

<a id="unreal.RigHierarchy.get_int32_array_metadata"></a>

#### get_int32_array_metadata

```python
def get_int32_array_metadata(item: RigElementKey,
                             metadata_name: Name) -> Array[int]
```

x.get_int32_array_metadata(item, metadata_name) -> Array[int32]
Queries and returns the value of int32 array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[int32]:

<a id="unreal.RigHierarchy.get_index"></a>

#### get_index

```python
def get_index(key: RigElementKey) -> int
```

x.get_index(key) -> int32
Returns the index of an element given its key

Args:
    key (RigElementKey): The key of the element to retrieve the index for

Returns:
    int32: The index of the element or INDEX_NONE

<a id="unreal.RigHierarchy.get_global_transform_by_index"></a>

#### get_global_transform_by_index

```python
def get_global_transform_by_index(element_index: int,
                                  initial: bool = False) -> Transform
```

x.get_global_transform_by_index(element_index, initial=False) -> Transform
Returns the global current or initial value for a element index.
If the index is invalid FTransform::Identity will be returned.

Args:
    element_index (int32): The index to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global current or initial transform's value.

<a id="unreal.RigHierarchy.get_global_transform"></a>

#### get_global_transform

```python
def get_global_transform(key: RigElementKey,
                         initial: bool = False) -> Transform
```

x.get_global_transform(key, initial=False) -> Transform
Returns the global current or initial value for a given key.
If the key is invalid FTransform::Identity will be returned.

Args:
    key (RigElementKey): The key to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global current or initial transform's value.

<a id="unreal.RigHierarchy.get_global_control_shape_transform_by_index"></a>

#### get_global_control_shape_transform_by_index

```python
def get_global_control_shape_transform_by_index(element_index: int,
                                                initial: bool = False
                                                ) -> Transform
```

x.get_global_control_shape_transform_by_index(element_index, initial=False) -> Transform
Returns the global shape transform for a given control element.

Args:
    element_index (int32): The index of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global shape transform

<a id="unreal.RigHierarchy.get_global_control_shape_transform"></a>

#### get_global_control_shape_transform

```python
def get_global_control_shape_transform(key: RigElementKey,
                                       initial: bool = False) -> Transform
```

x.get_global_control_shape_transform(key, initial=False) -> Transform
Returns the global shape transform for a given control element.

Args:
    key (RigElementKey): The key of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global shape transform

<a id="unreal.RigHierarchy.get_global_control_offset_transform_by_index"></a>

#### get_global_control_offset_transform_by_index

```python
def get_global_control_offset_transform_by_index(element_index: int,
                                                 initial: bool = False
                                                 ) -> Transform
```

x.get_global_control_offset_transform_by_index(element_index, initial=False) -> Transform
Returns the global offset transform for a given control element.

Args:
    element_index (int32): The index of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global offset transform

<a id="unreal.RigHierarchy.get_global_control_offset_transform"></a>

#### get_global_control_offset_transform

```python
def get_global_control_offset_transform(key: RigElementKey,
                                        initial: bool = False) -> Transform
```

x.get_global_control_offset_transform(key, initial=False) -> Transform
Returns the global offset transform for a given control element.

Args:
    key (RigElementKey): The key of the control to retrieve the transform for
    initial (bool): If true the initial transform will be used

Returns:
    Transform: The global offset transform

<a id="unreal.RigHierarchy.get_float_metadata"></a>

#### get_float_metadata

```python
def get_float_metadata(item: RigElementKey, metadata_name: Name,
                       default_value: float) -> float
```

x.get_float_metadata(item, metadata_name, default_value) -> float
Queries and returns the value of float metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (float): The default value to fall back on

Returns:
    float:

<a id="unreal.RigHierarchy.get_float_from_control_value"></a>

#### get_float_from_control_value

```python
@classmethod
def get_float_from_control_value(cls, value: RigControlValue) -> float
```

X.get_float_from_control_value(value) -> float
Returns the contained float value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    float: The converted float value

<a id="unreal.RigHierarchy.get_float_array_metadata"></a>

#### get_float_array_metadata

```python
def get_float_array_metadata(item: RigElementKey,
                             metadata_name: Name) -> Array[float]
```

x.get_float_array_metadata(item, metadata_name) -> Array[float]
Queries and returns the value of float array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[float]:

<a id="unreal.RigHierarchy.get_first_parent"></a>

#### get_first_parent

```python
def get_first_parent(key: RigElementKey) -> RigElementKey
```

x.get_first_parent(key) -> RigElementKey
Returns the first parent element of a given element key

Args:
    key (RigElementKey): The key of the element to retrieve the parents for

Returns:
    RigElementKey: Returns the first parent element

<a id="unreal.RigHierarchy.get_euler_transform_from_control_value"></a>

#### get_euler_transform_from_control_value

```python
@classmethod
def get_euler_transform_from_control_value(
        cls, value: RigControlValue) -> EulerTransform
```

X.get_euler_transform_from_control_value(value) -> EulerTransform
Returns the contained FEulerTransform value from a a Rig Control Value

Args:
    value (RigControlValue): The Rig Control value to convert from

Returns:
    EulerTransform: The converted FEulerTransform value

<a id="unreal.RigHierarchy.get_default_parent"></a>

#### get_default_parent

```python
def get_default_parent(key: RigElementKey) -> RigElementKey
```

x.get_default_parent(key) -> RigElementKey
Returns the default parent element's key of a given child key

Args:
    key (RigElementKey): The key of the element to retrieve the parent for

Returns:
    RigElementKey: Returns the default parent element key

<a id="unreal.RigHierarchy.get_curve_value_by_index"></a>

#### get_curve_value_by_index

```python
def get_curve_value_by_index(element_index: int) -> float
```

x.get_curve_value_by_index(element_index) -> float
Returns a curve's value given its index

Args:
    element_index (int32): The index of the element to retrieve the value for

Returns:
    float: Returns the value of the curve

<a id="unreal.RigHierarchy.get_curve_value"></a>

#### get_curve_value

```python
def get_curve_value(key: RigElementKey) -> float
```

x.get_curve_value(key) -> float
Returns a curve's value given its key

Args:
    key (RigElementKey): The key of the element to retrieve the value for

Returns:
    float: Returns the value of the curve

<a id="unreal.RigHierarchy.get_curves"></a>

#### get_curves

```python
def get_curves() -> Array[RigElementKey]
```

x.get_curves() -> Array[RigElementKey]
Returns all Curve elements

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_control_value_by_index"></a>

#### get_control_value_by_index

```python
def get_control_value_by_index(
    element_index: int,
    value_type: RigControlValueType = RigControlValueType.CURRENT
) -> RigControlValue
```

x.get_control_value_by_index(element_index, value_type=RigControlValueType.CURRENT) -> RigControlValue
Returns a control's current value given its index

Args:
    element_index (int32): The index of the element to retrieve the current value for
    value_type (RigControlValueType): The type of value to return

Returns:
    RigControlValue: Returns the current value of the control

<a id="unreal.RigHierarchy.get_control_value"></a>

#### get_control_value

```python
def get_control_value(
    key: RigElementKey,
    value_type: RigControlValueType = RigControlValueType.CURRENT
) -> RigControlValue
```

x.get_control_value(key, value_type=RigControlValueType.CURRENT) -> RigControlValue
Returns a control's current value given its key

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    value_type (RigControlValueType): The type of value to return

Returns:
    RigControlValue: Returns the current value of the control

<a id="unreal.RigHierarchy.get_control_preferred_rotator_by_index"></a>

#### get_control_preferred_rotator_by_index

```python
def get_control_preferred_rotator_by_index(element_index: int,
                                           initial: bool = False) -> Rotator
```

x.get_control_preferred_rotator_by_index(element_index, initial=False) -> Rotator
Returns a control's preferred rotator (local transform rotation)

Args:
    element_index (int32): The element index to look up
    initial (bool): If true we'll return the preferred rotator for the initial - otherwise current transform

Returns:
    Rotator: Returns the current preferred rotator

<a id="unreal.RigHierarchy.get_control_preferred_rotator"></a>

#### get_control_preferred_rotator

```python
def get_control_preferred_rotator(key: RigElementKey,
                                  initial: bool = False) -> Rotator
```

x.get_control_preferred_rotator(key, initial=False) -> Rotator
Returns a control's preferred rotator (local transform rotation)

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    initial (bool): If true we'll return the preferred rotator for the initial - otherwise current transform

Returns:
    Rotator: Returns the current preferred rotator

<a id="unreal.RigHierarchy.get_control_preferred_euler_rotation_order_by_index"></a>

#### get_control_preferred_euler_rotation_order_by_index

```python
def get_control_preferred_euler_rotation_order_by_index(
        element_index: int, from_settings: bool = True) -> EulerRotationOrder
```

x.get_control_preferred_euler_rotation_order_by_index(element_index, from_settings=True) -> EulerRotationOrder
Returns a control's preferred euler rotation order

Args:
    element_index (int32): The element index to look up
    from_settings (bool): If true the rotation order will be looked up from the control's settings, otherwise from the currently set animation value

Returns:
    EulerRotationOrder: Returns the current preferred euler rotation order

<a id="unreal.RigHierarchy.get_control_preferred_euler_rotation_order"></a>

#### get_control_preferred_euler_rotation_order

```python
def get_control_preferred_euler_rotation_order(key: RigElementKey,
                                               from_settings: bool = True
                                               ) -> EulerRotationOrder
```

x.get_control_preferred_euler_rotation_order(key, from_settings=True) -> EulerRotationOrder
Returns a control's preferred euler rotation order

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    from_settings (bool): If true the rotation order will be looked up from the control's settings, otherwise from the currently set animation value

Returns:
    EulerRotationOrder: Returns the current preferred euler rotation order

<a id="unreal.RigHierarchy.get_control_preferred_euler_angles_by_index"></a>

#### get_control_preferred_euler_angles_by_index

```python
def get_control_preferred_euler_angles_by_index(
        element_index: int,
        rotation_order: EulerRotationOrder,
        initial: bool = False) -> Vector
```

x.get_control_preferred_euler_angles_by_index(element_index, rotation_order, initial=False) -> Vector
Returns a control's preferred euler angles (local transform rotation)

Args:
    element_index (int32): The element index to look up
    rotation_order (EulerRotationOrder): The rotation order to use when retrieving the euler angles
    initial (bool): If true we'll return the preferred euler angles for the initial - otherwise current transform

Returns:
    Vector: Returns the current preferred euler angles

<a id="unreal.RigHierarchy.get_control_preferred_euler_angles"></a>

#### get_control_preferred_euler_angles

```python
def get_control_preferred_euler_angles(key: RigElementKey,
                                       rotation_order: EulerRotationOrder,
                                       initial: bool = False) -> Vector
```

x.get_control_preferred_euler_angles(key, rotation_order, initial=False) -> Vector
Returns a control's preferred euler angles (local transform rotation)

Args:
    key (RigElementKey): The key of the element to retrieve the current value for
    rotation_order (EulerRotationOrder): The rotation order to use when retrieving the euler angles
    initial (bool): If true we'll return the preferred euler angles for the initial - otherwise current transform

Returns:
    Vector: Returns the current preferred euler angles

<a id="unreal.RigHierarchy.get_controller"></a>

#### get_controller

```python
def get_controller(create_if_needed: bool = True) -> RigHierarchyController
```

x.get_controller(create_if_needed=True) -> RigHierarchyController
Returns a controller for this hierarchy.
Note: If the controller is not available this will return nullptr
even if the bCreateIfNeeded flag is set to true. You can check the
controller's availability with IsControllerAvailable().

Args:
    create_if_needed (bool): Creates a controller if needed

Returns:
    RigHierarchyController: The Controller for this hierarchy

<a id="unreal.RigHierarchy.get_controls"></a>

#### get_controls

```python
def get_controls(traverse: bool = True) -> Array[RigElementKey]
```

x.get_controls(traverse=True) -> Array[RigElementKey]
Returns all Control elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_connector_states"></a>

#### get_connector_states

```python
def get_connector_states() -> Array[RigConnectorState]
```

x.get_connector_states() -> Array[RigConnectorState]
Returns all of the connectors' state

Returns:
    Array[RigConnectorState]:

<a id="unreal.RigHierarchy.get_connectors"></a>

#### get_connectors

```python
def get_connectors(traverse: bool = True) -> Array[RigElementKey]
```

x.get_connectors(traverse=True) -> Array[RigElementKey]
Returns all Connector elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_children"></a>

#### get_children

```python
def get_children(key: RigElementKey,
                 recursive: bool = False) -> Array[RigElementKey]
```

x.get_children(key, recursive=False) -> Array[RigElementKey]
Returns the child elements of a given element key

Args:
    key (RigElementKey): The key of the element to retrieve the children for
    recursive (bool): If set to true grand-children will also be returned etc

Returns:
    Array[RigElementKey]: Returns the child elements

<a id="unreal.RigHierarchy.get_bool_metadata"></a>

#### get_bool_metadata

```python
def get_bool_metadata(item: RigElementKey, metadata_name: Name,
                      default_value: bool) -> bool
```

x.get_bool_metadata(item, metadata_name, default_value) -> bool
Queries and returns the value of bool metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query
    default_value (bool): The default value to fall back on

Returns:
    bool:

<a id="unreal.RigHierarchy.get_bool_array_metadata"></a>

#### get_bool_array_metadata

```python
def get_bool_array_metadata(item: RigElementKey,
                            metadata_name: Name) -> Array[bool]
```

x.get_bool_array_metadata(item, metadata_name) -> Array[bool]
Queries and returns the value of bool array metadata

Args:
    item (RigElementKey): The element key to return the metadata for
    metadata_name (Name): The name of the metadata to query

Returns:
    Array[bool]:

<a id="unreal.RigHierarchy.get_bones"></a>

#### get_bones

```python
def get_bones(traverse: bool = True) -> Array[RigElementKey]
```

x.get_bones(traverse=True) -> Array[RigElementKey]
Returns all Bone elements

Args:
    traverse (bool): Returns the elements in order of a depth first traversal

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchy.get_all_keys"></a>

#### get_all_keys

```python
def get_all_keys(traverse: bool = True) -> Array[RigElementKey]
```

x.get_all_keys(traverse=True) -> Array[RigElementKey]
Returns all element keys of this hierarchy

Args:
    traverse (bool): If set to true the keys will be returned by depth first traversal

Returns:
    Array[RigElementKey]: The keys of all elements

<a id="unreal.RigHierarchy.find_null"></a>

#### find_null

```python
def find_null(key: RigElementKey) -> RigNullElement
```

x.find_null(key) -> RigNullElement
Returns null element for a given key, for scripting purpose only, for cpp usage, use Find<FRigControlElement>()

Args:
    key (RigElementKey): The key of the null element to retrieve.

Returns:
    RigNullElement:

<a id="unreal.RigHierarchy.find_control"></a>

#### find_control

```python
def find_control(key: RigElementKey) -> RigControlElement
```

x.find_control(key) -> RigControlElement
Returns control element for a given key, for scripting purpose only, for cpp usage, use Find<FRigControlElement>()

Args:
    key (RigElementKey): The key of the control element to retrieve.

Returns:
    RigControlElement:

<a id="unreal.RigHierarchy.find_bone"></a>

#### find_bone

```python
def find_bone(key: RigElementKey) -> RigBoneElement
```

x.find_bone(key) -> RigBoneElement
Returns bone element for a given key, for scripting purpose only, for cpp usage, use Find<FRigBoneElement>()

Args:
    key (RigElementKey): The key of the bone element to retrieve.

Returns:
    RigBoneElement:

<a id="unreal.RigHierarchy.copy_pose"></a>

#### copy_pose

```python
def copy_pose(hierarchy: RigHierarchy,
              current: bool,
              initial: bool,
              weights: bool,
              match_pose_in_global_if_needed: bool = False) -> None
```

x.copy_pose(hierarchy, current, initial, weights, match_pose_in_global_if_needed=False) -> None
Copies the contents of a hierarchy onto this one

Args:
    hierarchy (RigHierarchy): 
    current (bool): 
    initial (bool): 
    weights (bool): 
    match_pose_in_global_if_needed (bool):

<a id="unreal.RigHierarchy.copy_hierarchy"></a>

#### copy_hierarchy

```python
def copy_hierarchy(hierarchy: RigHierarchy) -> None
```

x.copy_hierarchy(hierarchy) -> None
Copies the contents of a hierarchy onto this one

Args:
    hierarchy (RigHierarchy):

<a id="unreal.RigHierarchy.contains"></a>

#### contains

```python
def contains(key: RigElementKey) -> bool
```

x.contains(key) -> bool
Returns true if the provided element key is valid

Args:
    key (RigElementKey): The key to validate

Returns:
    bool: Returns true if the provided element key is valid

<a id="unreal.AnimNodeControlRigLibrary"></a>