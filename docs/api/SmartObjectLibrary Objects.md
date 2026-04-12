## SmartObjectLibrary Objects

```python
class SmartObjectLibrary(BlueprintFunctionLibrary)
```

Smart Object Blueprint Function Library

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectBlueprintFunctionLibrary.h

<a id="unreal.SmartObjectLibrary.smart_object_claim_handle_invalid"></a>

#### smart\_object\_claim\_handle\_invalid

```python
@classmethod
def smart_object_claim_handle_invalid(cls) -> SmartObjectClaimHandle
```

X.smart_object_claim_handle_invalid() -> SmartObjectClaimHandle
Returns the invalid smart object claim handle.

Returns:
    SmartObjectClaimHandle:

<a id="unreal.SmartObjectLibrary.set_value_as_so_claim_handle"></a>

#### set\_value\_as\_so\_claim\_handle

```python
@classmethod
def set_value_as_so_claim_handle(cls,
                                 blackboard_component: BlackboardComponent,
                                 key_name: Name,
                                 value: SmartObjectClaimHandle) -> None
```

X.set_value_as_so_claim_handle(blackboard_component, key_name, value) -> None
Set Value as SOClaim Handle

Args:
    blackboard_component (BlackboardComponent): 
    key_name (Name): 
    value (SmartObjectClaimHandle):

<a id="unreal.SmartObjectLibrary.set_smart_object_enabled"></a>

#### set\_smart\_object\_enabled

```python
@classmethod
def set_smart_object_enabled(cls, smart_object_actor: Actor,
                             enabled: bool) -> bool
```

X.set_smart_object_enabled(smart_object_actor, enabled) -> bool
Marks all smart objects for an actor as enabled or not according to 'bEnabled'. A smart object marked as Enabled is available for queries.
note: Disabling a smart object will not interrupt active interactions, it will simply mark the object unavailable for new queries and broadcast an event that can be handled by the interacting agent to complete earlier. If the object should not be consider usable anymore and the interactions aborted then consider using one of the Add/RemoveSmartObject functions.
see: AddOrRemoveSmartObject, AddOrRemoveMultipleSmartObjects, AddSmartObject, AddMultipleSmartObjects, RemoveSmartObject, RemoveMultipleSmartObjects

Args:
    smart_object_actor (Actor): The actor containing the smart objects to enable/disable
    enabled (bool): Whether the smart objects should be enabled or not

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.set_multiple_smart_objects_enabled"></a>

#### set\_multiple\_smart\_objects\_enabled

```python
@classmethod
def set_multiple_smart_objects_enabled(cls, smart_object_actors: Array[Actor],
                                       enabled: bool) -> bool
```

X.set_multiple_smart_objects_enabled(smart_object_actors, enabled) -> bool
Marks all smart objects for a list of actors as enabled or not according to 'bEnabled'. A smart object marked as Enabled is available for queries.
note: Disabling a smart object will not interrupt active interactions, it will simply mark the object unavailable for new queries and broadcast an event that can be handled by the interacting agent to complete earlier. If the object should not be consider usable anymore and the interactions aborted then consider using one of the Add/RemoveSmartObject functions.
see: AddOrRemoveSmartObject, AddOrRemoveMultipleSmartObjects, AddSmartObject, AddMultipleSmartObjects, RemoveSmartObject, RemoveMultipleSmartObjects

Args:
    smart_object_actors (Array[Actor]): The actors containing the smart objects to enable/disable
    enabled (bool): Whether the smart objects should be in the simulation (added) or not (removed)

Returns:
    bool: True if all actors were valid and the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.set_blackboard_value_as_so_claim_handle"></a>

#### set\_blackboard\_value\_as\_so\_claim\_handle

```python
@classmethod
def set_blackboard_value_as_so_claim_handle(
        cls, node_owner: BTNode, key: BlackboardKeySelector,
        value: SmartObjectClaimHandle) -> None
```

X.set_blackboard_value_as_so_claim_handle(node_owner, key, value) -> None
Set Blackboard Value as SOClaim Handle

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (SmartObjectClaimHandle):

<a id="unreal.SmartObjectLibrary.remove_smart_object"></a>

#### remove\_smart\_object

```python
@classmethod
def remove_smart_object(cls, smart_object_actor: Actor) -> bool
```

X.remove_smart_object(smart_object_actor) -> bool
Removes from the simulation all smart objects for an actor.
note: Removing a smart object from the simulation will interrupt all active interactions. If you simply need to make the object unavailable for queries consider using one of the SetSmartObjectEnabled functions so active interactions can be gracefully completed.
see: SetSmartObjectEnabled, SetMultipleSmartObjectsEnabled

Args:
    smart_object_actor (Actor): The actor containing the smart objects to add or remove from the simulation

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.remove_multiple_smart_objects"></a>

#### remove\_multiple\_smart\_objects

```python
@classmethod
def remove_multiple_smart_objects(cls,
                                  smart_object_actors: Array[Actor]) -> bool
```

X.remove_multiple_smart_objects(smart_object_actors) -> bool
Removes from the simulation all smart objects for multiple actors.
note: Removing a smart object from the simulation will interrupt all active interactions. If you simply need to make the object unavailable for queries consider using one of the SetSmartObjectEnabled functions so active interactions can be gracefully completed.
see: SetSmartObjectEnabled, SetMultipleSmartObjectsEnabled

Args:
    smart_object_actors (Array[Actor]): The actors containing the smart objects to remove from the simulation

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.not_equal_smart_object_slot_handle_smart_object_slot_handle"></a>

#### not\_equal\_smart\_object\_slot\_handle\_smart\_object\_slot\_handle

```python
@classmethod
def not_equal_smart_object_slot_handle_smart_object_slot_handle(
        cls, a: SmartObjectSlotHandle, b: SmartObjectSlotHandle) -> bool
```

X.not_equal_smart_object_slot_handle_smart_object_slot_handle(a, b) -> bool
Returns true if SmartObjectSlotHandle A is NOT equal to SmartObjectSlotHandle B (A != B)

Args:
    a (SmartObjectSlotHandle): 
    b (SmartObjectSlotHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.not_equal_smart_object_handle_smart_object_handle"></a>

#### not\_equal\_smart\_object\_handle\_smart\_object\_handle

```python
@classmethod
def not_equal_smart_object_handle_smart_object_handle(
        cls, a: SmartObjectHandle, b: SmartObjectHandle) -> bool
```

X.not_equal_smart_object_handle_smart_object_handle(a, b) -> bool
Returns true if SmartObjectHandle A is NOT equal to SmartObjectHandle B (A != B)

Args:
    a (SmartObjectHandle): 
    b (SmartObjectHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.mark_smart_object_slot_as_occupied"></a>

#### mark\_smart\_object\_slot\_as\_occupied

```python
@classmethod
def mark_smart_object_slot_as_occupied(
        cls, world_context_object: Object,
        claim_handle: SmartObjectClaimHandle,
        definition_class: Class) -> SmartObjectBehaviorDefinition
```

X.mark_smart_object_slot_as_occupied(world_context_object, claim_handle, definition_class) -> SmartObjectBehaviorDefinition
Marks a previously claimed smart object slot as occupied.

Args:
    world_context_object (Object): Object used to fetch the SmartObjectSubsystem of its associated world.
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.
    definition_class (type(Class)): The type of behavior definition the user wants to use.

Returns:
    SmartObjectBehaviorDefinition: The base class pointer of the requested behavior definition class associated to the slot

<a id="unreal.SmartObjectLibrary.mark_smart_object_slot_as_free"></a>

#### mark\_smart\_object\_slot\_as\_free

```python
@classmethod
def mark_smart_object_slot_as_free(
        cls, world_context_object: Object,
        claim_handle: SmartObjectClaimHandle) -> bool
```

X.mark_smart_object_slot_as_free(world_context_object, claim_handle) -> bool
Marks a claimed or occupied smart object as free.

Args:
    world_context_object (Object): Object used to fetch the SmartObjectSubsystem of its associated world.
    claim_handle (SmartObjectClaimHandle): Handle to a claimed slot returned by any of the Claim methods.

Returns:
    bool: Whether the claim was successfully released or not

<a id="unreal.SmartObjectLibrary.mark_smart_object_slot_as_claimed"></a>

#### mark\_smart\_object\_slot\_as\_claimed

```python
@classmethod
def mark_smart_object_slot_as_claimed(
    cls,
    world_context_object: Object,
    slot_handle: SmartObjectSlotHandle,
    user_actor: Actor = None,
    claim_priority: SmartObjectClaimPriority = SmartObjectClaimPriority.NORMAL
) -> SmartObjectClaimHandle
```

X.mark_smart_object_slot_as_claimed(world_context_object, slot_handle, user_actor=None, claim_priority=SmartObjectClaimPriority.NORMAL) -> SmartObjectClaimHandle
Marks a smart object slot from a request result as claimed.

Args:
    world_context_object (Object): Object used to fetch the SmartObjectSubsystem of its associated world.
    slot_handle (SmartObjectSlotHandle): Handle to a smart object slot.
    user_actor (Actor): Actor claiming the smart object
    claim_priority (SmartObjectClaimPriority): Claim priority, a slot claimed at lower priority can be claimed by higher priority (unless already in use).

Returns:
    SmartObjectClaimHandle: A handle binding the claimed smart object, its slot and a user id.

<a id="unreal.SmartObjectLibrary.is_valid_smart_object_slot_handle"></a>

#### is\_valid\_smart\_object\_slot\_handle

```python
@classmethod
def is_valid_smart_object_slot_handle(cls,
                                      handle: SmartObjectSlotHandle) -> bool
```

X.is_valid_smart_object_slot_handle(handle) -> bool
Returns true if the given Smart Object Slot Handle is valid.

Args:
    handle (SmartObjectSlotHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.is_valid_smart_object_handle"></a>

#### is\_valid\_smart\_object\_handle

```python
@classmethod
def is_valid_smart_object_handle(cls, handle: SmartObjectHandle) -> bool
```

X.is_valid_smart_object_handle(handle) -> bool
Returns true if the given handle is valid

Args:
    handle (SmartObjectHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.is_valid_smart_object_claim_handle"></a>

#### is\_valid\_smart\_object\_claim\_handle

```python
@classmethod
def is_valid_smart_object_claim_handle(cls,
                                       handle: SmartObjectClaimHandle) -> bool
```

X.is_valid_smart_object_claim_handle(handle) -> bool
Is Valid Smart Object Claim Handle

Args:
    handle (SmartObjectClaimHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.get_value_as_so_claim_handle"></a>

#### get\_value\_as\_so\_claim\_handle

```python
@classmethod
def get_value_as_so_claim_handle(cls,
                                 blackboard_component: BlackboardComponent,
                                 key_name: Name) -> SmartObjectClaimHandle
```

X.get_value_as_so_claim_handle(blackboard_component, key_name) -> SmartObjectClaimHandle
Get Value as SOClaim Handle

Args:
    blackboard_component (BlackboardComponent): 
    key_name (Name): 

Returns:
    SmartObjectClaimHandle:

<a id="unreal.SmartObjectLibrary.get_blackboard_value_as_so_claim_handle"></a>

#### get\_blackboard\_value\_as\_so\_claim\_handle

```python
@classmethod
def get_blackboard_value_as_so_claim_handle(
        cls, node_owner: BTNode,
        key: BlackboardKeySelector) -> SmartObjectClaimHandle
```

X.get_blackboard_value_as_so_claim_handle(node_owner, key) -> SmartObjectClaimHandle
Get Blackboard Value as SOClaim Handle

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    SmartObjectClaimHandle:

<a id="unreal.SmartObjectLibrary.find_smart_objects_in_targeting_request"></a>

#### find\_smart\_objects\_in\_targeting\_request

```python
@classmethod
def find_smart_objects_in_targeting_request(
        cls,
        world_context_object: Object,
        filter: SmartObjectRequestFilter,
        targeting_handle: TargetingRequestHandle,
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

X.find_smart_objects_in_targeting_request(world_context_object, filter, targeting_handle, user_actor=None) -> Array[SmartObjectRequestResult] or None
Search the results of the given targeting handle request for smart objects that match the request criteria

Args:
    world_context_object (Object): Object used to fetch the SmartObjectSubsystem of its associated world.
    filter (SmartObjectRequestFilter): Parameters defining the search area and criteria
    targeting_handle (TargetingRequestHandle): The targeting handle of the request that will have its results searched for smart objects
    user_actor (Actor): Used to create additional data that could be provided to bind values in the conditions evaluation context

Returns:
    Array[SmartObjectRequestResult] or None: True if at least one candidate was found.

    out_results (Array[SmartObjectRequestResult]): List of smart object slot candidates found in range

<a id="unreal.SmartObjectLibrary.find_smart_objects_in_list"></a>

#### find\_smart\_objects\_in\_list

```python
@classmethod
def find_smart_objects_in_list(
        cls,
        world_context_object: Object,
        filter: SmartObjectRequestFilter,
        actor_list: Array[Actor],
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

X.find_smart_objects_in_list(world_context_object, filter, actor_list, user_actor=None) -> Array[SmartObjectRequestResult] or None
Search list of specific actors (often from a physics query) for slot candidates respecting request criteria and selection conditions.

Args:
    world_context_object (Object): Object used to fetch the SmartObjectSubsystem of its associated world.
    filter (SmartObjectRequestFilter): Parameters defining the search area and criteria
    actor_list (Array[Actor]): Ordered list of actors to search
    user_actor (Actor): 

Returns:
    Array[SmartObjectRequestResult] or None: True if at least one candidate was found.

    out_results (Array[SmartObjectRequestResult]): List of smart object slot candidates found in range

<a id="unreal.SmartObjectLibrary.find_smart_objects_in_component"></a>

#### find\_smart\_objects\_in\_component

```python
@classmethod
def find_smart_objects_in_component(
        cls,
        filter: SmartObjectRequestFilter,
        smart_object_component: SmartObjectComponent,
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

X.find_smart_objects_in_component(filter, smart_object_component, user_actor=None) -> Array[SmartObjectRequestResult] or None
Search a given Smart Object Component for slot candidates respecting the request criteria and selection conditions.

Args:
    filter (SmartObjectRequestFilter): Parameters defining the search area and criteria
    smart_object_component (SmartObjectComponent): The component to search
    user_actor (Actor): Used to create additional data that could be provided to bind values in the conditions evaluation context

Returns:
    Array[SmartObjectRequestResult] or None: True if at least one candidate was found.

    out_results (Array[SmartObjectRequestResult]): List of smart object slot candidates found in range

<a id="unreal.SmartObjectLibrary.find_smart_objects_in_actor"></a>

#### find\_smart\_objects\_in\_actor

```python
@classmethod
def find_smart_objects_in_actor(
        cls,
        filter: SmartObjectRequestFilter,
        search_actor: Actor,
        user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
```

X.find_smart_objects_in_actor(filter, search_actor, user_actor=None) -> Array[SmartObjectRequestResult] or None
Search a given Actor for slot candidates respecting the request criteria and selection conditions.

Args:
    filter (SmartObjectRequestFilter): Parameters defining the search area and criteria
    search_actor (Actor): The actor to search
    user_actor (Actor): Used to create additional data that could be provided to bind values in the conditions evaluation context

Returns:
    Array[SmartObjectRequestResult] or None: True if at least one candidate was found.

    out_results (Array[SmartObjectRequestResult]): List of smart object slot candidates found in range

<a id="unreal.SmartObjectLibrary.equal_smart_object_slot_handle_smart_object_slot_handle"></a>

#### equal\_smart\_object\_slot\_handle\_smart\_object\_slot\_handle

```python
@classmethod
def equal_smart_object_slot_handle_smart_object_slot_handle(
        cls, a: SmartObjectSlotHandle, b: SmartObjectSlotHandle) -> bool
```

X.equal_smart_object_slot_handle_smart_object_slot_handle(a, b) -> bool
Returns true if SmartObjectSlotHandle A is equal to SmartObjectSlotHandle B (A == B)

Args:
    a (SmartObjectSlotHandle): 
    b (SmartObjectSlotHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.equal_smart_object_handle_smart_object_handle"></a>

#### equal\_smart\_object\_handle\_smart\_object\_handle

```python
@classmethod
def equal_smart_object_handle_smart_object_handle(
        cls, a: SmartObjectHandle, b: SmartObjectHandle) -> bool
```

X.equal_smart_object_handle_smart_object_handle(a, b) -> bool
Returns true if SmartObjectHandle A is equal to SmartObjectHandle B (A == B)

Args:
    a (SmartObjectHandle): 
    b (SmartObjectHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectLibrary.conv_smart_object_slot_handle_to_string"></a>

#### conv\_smart\_object\_slot\_handle\_to\_string

```python
@classmethod
def conv_smart_object_slot_handle_to_string(
        cls, handle: SmartObjectSlotHandle) -> str
```

X.conv_smart_object_slot_handle_to_string(handle) -> str
Converts a SmartObjectSlotHandle value to a string

Args:
    handle (SmartObjectSlotHandle): 

Returns:
    str:

<a id="unreal.SmartObjectLibrary.conv_smart_object_request_result_to_string"></a>

#### conv\_smart\_object\_request\_result\_to\_string

```python
@classmethod
def conv_smart_object_request_result_to_string(
        cls, result: SmartObjectRequestResult) -> str
```

X.conv_smart_object_request_result_to_string(result) -> str
Converts a SmartObjectRequestResult value to a string

Args:
    result (SmartObjectRequestResult): 

Returns:
    str:

<a id="unreal.SmartObjectLibrary.conv_smart_object_handle_to_string"></a>

#### conv\_smart\_object\_handle\_to\_string

```python
@classmethod
def conv_smart_object_handle_to_string(cls, handle: SmartObjectHandle) -> str
```

X.conv_smart_object_handle_to_string(handle) -> str
Converts a SmartObjectHandle value to a string

Args:
    handle (SmartObjectHandle): 

Returns:
    str:

<a id="unreal.SmartObjectLibrary.conv_smart_object_definition_to_string"></a>

#### conv\_smart\_object\_definition\_to\_string

```python
@classmethod
def conv_smart_object_definition_to_string(
        cls, definition: SmartObjectDefinition) -> str
```

X.conv_smart_object_definition_to_string(definition) -> str
Converts a SmartObjectDefinition value to a string

Args:
    definition (SmartObjectDefinition): 

Returns:
    str:

<a id="unreal.SmartObjectLibrary.conv_smart_object_claim_handle_to_string"></a>

#### conv\_smart\_object\_claim\_handle\_to\_string

```python
@classmethod
def conv_smart_object_claim_handle_to_string(
        cls, result: SmartObjectClaimHandle) -> str
```

X.conv_smart_object_claim_handle_to_string(result) -> str
Converts a SmartObjectClaimHandle value to a string

Args:
    result (SmartObjectClaimHandle): 

Returns:
    str:

<a id="unreal.SmartObjectLibrary.add_smart_object"></a>

#### add\_smart\_object

```python
@classmethod
def add_smart_object(cls, smart_object_actor: Actor) -> bool
```

X.add_smart_object(smart_object_actor) -> bool
Adds to the simulation all smart objects for an actor.

Args:
    smart_object_actor (Actor): The actor containing the smart objects to add to the simulation

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.add_or_remove_smart_object"></a>

#### add\_or\_remove\_smart\_object

```python
@classmethod
def add_or_remove_smart_object(cls, smart_object: Actor,
                               enabled: bool) -> bool
```

X.add_or_remove_smart_object(smart_object, enabled) -> bool
Adds to the simulation all smart objects for an actor or removes them according to 'bAdd'.
note: Removing a smart object from the simulation will interrupt all active interactions. If you simply need to make the object unavailable for queries consider using one of the SetSmartObjectEnabled functions so active interactions can be gracefully completed.
see: SetSmartObjectEnabled, SetMultipleSmartObjectsEnabled

Args:
    smart_object (Actor): 
    enabled (bool): 

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.k2_set_smart_object_enabled"></a>

#### k2\_set\_smart\_object\_enabled

```python
@classmethod
def k2_set_smart_object_enabled(cls, smart_object: Actor,
                                enabled: bool) -> bool
```

deprecated: 'k2_set_smart_object_enabled' was renamed to 'add_or_remove_smart_object'.

<a id="unreal.SmartObjectLibrary.add_or_remove_multiple_smart_objects"></a>

#### add\_or\_remove\_multiple\_smart\_objects

```python
@classmethod
def add_or_remove_multiple_smart_objects(cls,
                                         smart_object_actors: Array[Actor],
                                         add: bool) -> bool
```

X.add_or_remove_multiple_smart_objects(smart_object_actors, add) -> bool
Adds to the simulation all smart objects for multiple actors or removes them according to 'bAdd'.
note: Removing a smart object from the simulation will interrupt all active interactions. If you simply need to make the object unavailable for queries consider using one of the SetSmartObjectEnabled functions so active interactions can be gracefully completed.
see: SetSmartObjectEnabled, SetMultipleSmartObjectsEnabled

Args:
    smart_object_actors (Array[Actor]): The actors containing the smart objects to add or remove from the simulation
    add (bool): Whether the smart objects should be added or removed from the simulation

Returns:
    bool: True if all actors were valid and the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectLibrary.add_multiple_smart_objects"></a>

#### add\_multiple\_smart\_objects

```python
@classmethod
def add_multiple_smart_objects(cls, smart_object_actors: Array[Actor]) -> bool
```

X.add_multiple_smart_objects(smart_object_actors) -> bool
Adds to the simulation all smart objects for multiple actors.

Args:
    smart_object_actors (Array[Actor]): The actors containing the smart objects to add to the simulation

Returns:
    bool: True if the requested operation succeeded; false otherwise

<a id="unreal.SmartObjectCollection"></a>