## SmartObjectSubsystem Objects

```python
class SmartObjectSubsystem(WorldSubsystem)
```

Subsystem that holds all registered smart object instances and offers the API for spatial queries and reservations.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

<a id="unreal.SmartObjectSubsystem.set_slot_enabled"></a>

#### set\_slot\_enabled

```python
def set_slot_enabled(slot_handle: SmartObjectSlotHandle,
                     enabled: bool) -> bool
```

x.set_slot_enabled(slot_handle, enabled) -> bool
Enables or disables the smart object slot represented by the provided handle.

Args:
    slot_handle (SmartObjectSlotHandle): Handle to the smart object slot.
    enabled (bool): If true enables the slot, if false, disables the slot.

Returns:
    bool: Previous enabled state.

<a id="unreal.SmartObjectSubsystem.set_enabled_for_reason"></a>

#### set\_enabled\_for\_reason

```python
def set_enabled_for_reason(handle: SmartObjectHandle, reason_tag: GameplayTag,
                           enabled: bool) -> bool
```

x.set_enabled_for_reason(handle, reason_tag, enabled) -> bool
Enables or disables the entire smart object represented by the provided handle using the specified reason.
Delegate 'OnEvent' is broadcasted with ESmartObjectChangeReason::OnEnabled/ESmartObjectChangeReason::OnDisabled if state changed.

Args:
    handle (SmartObjectHandle): Handle to the smart object.
    reason_tag (GameplayTag): Valid Tag to specify the reason for changing the enabled state of the object. Method will ensure if not valid (i.e. None).
    enabled (bool): If true enables the smart object, disables otherwise.

Returns:
    bool: True when associated smart object is found and set (or already set) to desired state; false otherwise.

<a id="unreal.SmartObjectSubsystem.set_enabled"></a>

#### set\_enabled

```python
def set_enabled(handle: SmartObjectHandle, enabled: bool) -> bool
```

x.set_enabled(handle, enabled) -> bool
Enables or disables the entire smart object represented by the provided handle using the default reason (i.e. Gameplay)..
Delegate 'OnEvent' is broadcasted with ESmartObjectChangeReason::OnEnabled/ESmartObjectChangeReason::OnDisabled if state changed.

Args:
    handle (SmartObjectHandle): Handle to the smart object.
    enabled (bool): If true enables the smart object, disables otherwise.

Returns:
    bool: True when associated smart object is found and set (or already set) to desired state; false otherwise.

<a id="unreal.SmartObjectSubsystem.remove_tag_from_slot"></a>

#### remove\_tag\_from\_slot

```python
def remove_tag_from_slot(slot_handle: SmartObjectSlotHandle,
                         tag: GameplayTag) -> bool
```

x.remove_tag_from_slot(slot_handle, tag) -> bool
Removes a single tag from the smart object slot represented by the provided handle.

Args:
    slot_handle (SmartObjectSlotHandle): Handle to the smart object slot.
    tag (GameplayTag): Tag to remove from the smart object slot.

Returns:
    bool: True if the tag was removed.

<a id="unreal.SmartObjectSubsystem.remove_tag_from_instance"></a>

#### remove\_tag\_from\_instance

```python
def remove_tag_from_instance(handle: SmartObjectHandle,
                             tag: GameplayTag) -> None
```

x.remove_tag_from_instance(handle, tag) -> None
Removes a single tag from the smartobject instance represented by the provided handle.

Args:
    handle (SmartObjectHandle): Handle to the smart object.
    tag (GameplayTag): Tag to remove from the SmartObject instance.

<a id="unreal.SmartObjectSubsystem.release"></a>

#### release

```python
def release(claim_handle: SmartObjectClaimHandle) -> bool
```

x.release(claim_handle) -> bool
Release
deprecated: Use MarkSmartObjectSlotAsFree instead.

Args:
    claim_handle (SmartObjectClaimHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectSubsystem.is_enabled_for_reason"></a>

#### is\_enabled\_for\_reason

```python
def is_enabled_for_reason(handle: SmartObjectHandle,
                          reason_tag: GameplayTag) -> bool
```

x.is_enabled_for_reason(handle, reason_tag) -> bool
Returns the enabled state of the smart object represented by the provided handle based on a specific reason.

Args:
    handle (SmartObjectHandle): Handle to the smart object.
    reason_tag (GameplayTag): Valid Tag to test if enabled for a specific reason. Method will ensure if not valid (i.e. None).

Returns:
    bool: True when associated smart object is found and set to be enabled. False otherwise.

<a id="unreal.SmartObjectSubsystem.is_enabled"></a>

#### is\_enabled

```python
def is_enabled(handle: SmartObjectHandle) -> bool
```

x.is_enabled(handle) -> bool
Returns the enabled state of the smart object represented by the provided handle regardless of the disabled reason.

Args:
    handle (SmartObjectHandle): Handle to the smart object.

Returns:
    bool: True when associated smart object is found and set to be enabled. False otherwise.

<a id="unreal.SmartObjectSubsystem.get_smart_object_component_by_request_result"></a>

#### get\_smart\_object\_component\_by\_request\_result

```python
def get_smart_object_component_by_request_result(
    result: SmartObjectRequestResult,
    try_spawn_actor_if_dehydrated:
    TrySpawnActorIfDehydrated = TrySpawnActorIfDehydrated.NO
) -> SmartObjectComponent
```

x.get_smart_object_component_by_request_result(result, try_spawn_actor_if_dehydrated=TrySpawnActorIfDehydrated.NO) -> SmartObjectComponent
Returns the component associated to the  given request result
In some scenarios the component may no longer exist
but its smart object data could (e.g. streaming)

Args:
    result (SmartObjectRequestResult): A request result returned by any of the Find methods .
    try_spawn_actor_if_dehydrated (TrySpawnActorIfDehydrated): Indicates if the subsystem should try to spawn the actor/component associated to the smartobject if it is currently owned by an instanced actor.

Returns:
    SmartObjectComponent: A pointer to the USmartObjectComponent* associated to the handle.

<a id="unreal.SmartObjectSubsystem.get_smart_object_component"></a>

#### get\_smart\_object\_component

```python
def get_smart_object_component(
    claim_handle: SmartObjectClaimHandle,
    try_spawn_actor_if_dehydrated:
    TrySpawnActorIfDehydrated = TrySpawnActorIfDehydrated.NO
) -> SmartObjectComponent
```

x.get_smart_object_component(claim_handle, try_spawn_actor_if_dehydrated=TrySpawnActorIfDehydrated.NO) -> SmartObjectComponent
Returns the component associated to the claim handle if still
accessible. In some scenarios the component may no longer exist
but its smart object data could (e.g. streaming)

Args:
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.
    try_spawn_actor_if_dehydrated (TrySpawnActorIfDehydrated): Indicates if the subsystem should try to spawn the actor/component associated to the smartobject if it is currently owned by an instanced actor.

Returns:
    SmartObjectComponent: A pointer to the USmartObjectComponent* associated to the handle.

<a id="unreal.SmartObjectSubsystem.get_slot_transform_from_request_result"></a>

#### get\_slot\_transform\_from\_request\_result

```python
def get_slot_transform_from_request_result(
        request_result: SmartObjectRequestResult) -> Optional[Transform]
```

x.get_slot_transform_from_request_result(request_result) -> Transform or None
Returns the transform (in world space) of the slot associated to the given RequestResult.

Args:
    request_result (SmartObjectRequestResult): Result returned by any of the Find Smart Object(s) methods.

Returns:
    Transform or None: Whether the transform was found and assigned to 'OutSlotTransform'

    out_slot_transform (Transform): Transform (in world space) of the slot associated to the RequestResult.

<a id="unreal.SmartObjectSubsystem.get_slot_transform"></a>

#### get\_slot\_transform

```python
def get_slot_transform(
        claim_handle: SmartObjectClaimHandle) -> Optional[Transform]
```

x.get_slot_transform(claim_handle) -> Transform or None
Returns the transform (in world space) of the slot associated to the given claim handle.

Args:
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.

Returns:
    Transform or None: Whether the transform was found and assigned to 'OutSlotTransform'

    out_slot_transform (Transform): Transform (in world space) of the slot associated to ClaimHandle.

<a id="unreal.SmartObjectSubsystem.get_slot_tags"></a>

#### get\_slot\_tags

```python
def get_slot_tags(slot_handle: SmartObjectSlotHandle) -> GameplayTagContainer
```

x.get_slot_tags(slot_handle) -> GameplayTagContainer
Returns the list of tags associated to the smart object slot represented by the provided handle.

Args:
    slot_handle (SmartObjectSlotHandle): Handle to the smart object slot.

Returns:
    GameplayTagContainer: Container of tags associated to the smart object instance, or empty container if slot was not valid.

<a id="unreal.SmartObjectSubsystem.get_slot_state"></a>

#### get\_slot\_state

```python
def get_slot_state(slot_handle: SmartObjectSlotHandle) -> SmartObjectSlotState
```

x.get_slot_state(slot_handle) -> SmartObjectSlotState
Returns the state of the given Smart Object Slot handle.

Args:
    slot_handle (SmartObjectSlotHandle): 

Returns:
    SmartObjectSlotState:

<a id="unreal.SmartObjectSubsystem.get_slot_location"></a>

#### get\_slot\_location

```python
def get_slot_location(
        claim_handle: SmartObjectClaimHandle) -> Optional[Vector]
```

x.get_slot_location(claim_handle) -> Vector or None
Returns the position (in world space) of the slot associated to the given claim handle.

Args:
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.

Returns:
    Vector or None: Whether the location was found and assigned to 'OutSlotLocation'

    out_slot_location (Vector): Position (in world space) of the slot associated to ClaimHandle.

<a id="unreal.SmartObjectSubsystem.get_instance_tags"></a>

#### get\_instance\_tags

```python
def get_instance_tags(handle: SmartObjectHandle) -> GameplayTagContainer
```

x.get_instance_tags(handle) -> GameplayTagContainer
Returns the list of tags associated to the smart object instance represented by the provided handle.

Args:
    handle (SmartObjectHandle): Handle to the smart object.

Returns:
    GameplayTagContainer: Container of tags associated to the smart object instance.

<a id="unreal.SmartObjectSubsystem.get_behavior_definition_by_request_result"></a>

#### get\_behavior\_definition\_by\_request\_result

```python
def get_behavior_definition_by_request_result(
        request_result: SmartObjectRequestResult,
        definition_class: Class) -> SmartObjectBehaviorDefinition
```

x.get_behavior_definition_by_request_result(request_result, definition_class) -> SmartObjectBehaviorDefinition
Return the behavior definition of a given type from a request result.

Args:
    request_result (SmartObjectRequestResult): A request result returned by any of the Find methods.
    definition_class (type(Class)): The type of behavior definition.

Returns:
    SmartObjectBehaviorDefinition: The base class pointer of the requested behavior definition class associated to the request result

<a id="unreal.SmartObjectSubsystem.get_behavior_definition"></a>

#### get\_behavior\_definition

```python
def get_behavior_definition(
        claim_handle: SmartObjectClaimHandle,
        definition_class: Class) -> SmartObjectBehaviorDefinition
```

x.get_behavior_definition(claim_handle, definition_class) -> SmartObjectBehaviorDefinition
Return the behavior definition of a given type from a claimed object.

Args:
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.
    definition_class (type(Class)): The type of behavior definition.

Returns:
    SmartObjectBehaviorDefinition: The base class pointer of the requested behavior definition class associated to the slotClaim handle

<a id="unreal.SmartObjectSubsystem.get_all_slots"></a>

#### get\_all\_slots

```python
def get_all_slots(handle: SmartObjectHandle) -> Array[SmartObjectSlotHandle]
```

x.get_all_slots(handle) -> Array[SmartObjectSlotHandle]
Return all slots of a given smart object.

Args:
    handle (SmartObjectHandle): Handle to the smart object.

Returns:
    Array[SmartObjectSlotHandle]: 

    out_slots (Array[SmartObjectSlotHandle]): All slots of the smart object

<a id="unreal.SmartObjectSubsystem.find_smart_objects_bp"></a>

#### find\_smart\_objects\_bp

```python
def find_smart_objects_bp(
        request: SmartObjectRequest,
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

x.find_smart_objects_bp(request, user_actor=None) -> Array[SmartObjectRequestResult] or None
Blueprint function for spatial lookup for slot candidates respecting request criteria and selection conditions.

Args:
    request (SmartObjectRequest): Parameters defining the search area and criteria
    user_actor (Actor): Actor claiming the smart object

Returns:
    Array[SmartObjectRequestResult] or None: All valid smart objects in range.

    out_results (Array[SmartObjectRequestResult]): List of smart object slot candidates

<a id="unreal.SmartObjectSubsystem.find_smart_objects"></a>

#### find\_smart\_objects

```python
def find_smart_objects(
        request: SmartObjectRequest,
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

x.find_smart_objects(request, user_actor=None) -> Array[SmartObjectRequestResult] or None
Find Smart Objects
deprecated: The pure version is deprecated, place a new Find Smart Objects node and connect the exec pin

Args:
    request (SmartObjectRequest): 
    user_actor (Actor): 

Returns:
    Array[SmartObjectRequestResult] or None: 

    out_results (Array[SmartObjectRequestResult]):

<a id="unreal.SmartObjectSubsystem.find_smart_object"></a>

#### find\_smart\_object

```python
def find_smart_object(request: SmartObjectRequest,
                      user_actor: Actor = None) -> SmartObjectRequestResult
```

x.find_smart_object(request, user_actor=None) -> SmartObjectRequestResult
Spatial lookup for first slot in range respecting request criteria and selection conditions.

Args:
    request (SmartObjectRequest): Parameters defining the search area and criteria
    user_actor (Actor): Actor claiming the smart object used to evaluate selection conditions

Returns:
    SmartObjectRequestResult: First valid smart object in range. Not the closest one, just the one that happens to be retrieved first from space partition

<a id="unreal.SmartObjectSubsystem.add_tag_to_slot"></a>

#### add\_tag\_to\_slot

```python
def add_tag_to_slot(slot_handle: SmartObjectSlotHandle,
                    tag: GameplayTag) -> None
```

x.add_tag_to_slot(slot_handle, tag) -> None
Adds a single tag to the smart object slot represented by the provided handle.

Args:
    slot_handle (SmartObjectSlotHandle): Handle to the smart object slot.
    tag (GameplayTag): Tag to add to the smart object slot.

<a id="unreal.SmartObjectSubsystem.add_tag_to_instance"></a>

#### add\_tag\_to\_instance

```python
def add_tag_to_instance(handle: SmartObjectHandle, tag: GameplayTag) -> None
```

x.add_tag_to_instance(handle, tag) -> None
Adds a single tag to the smart object instance represented by the provided handle.

Args:
    handle (SmartObjectHandle): Handle to the smart object.
    tag (GameplayTag): Tag to add to the smart object instance.

<a id="unreal.SmartObjectSubsystemRenderingComponent"></a>