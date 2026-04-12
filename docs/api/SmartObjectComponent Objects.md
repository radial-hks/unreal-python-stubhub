## SmartObjectComponent Objects

```python
class SmartObjectComponent(SceneComponent)
```

Smart Object Component

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``cached_definition_asset_variation`` (SmartObjectDefinition):  [Read-Write] Do not use directly from native code, use GetDefinition() / SetDefinition() instead.
  Also Keeping blueprint accessors for convenience and deprecation purposes.
- ``can_be_part_of_collection`` (bool):  [Read-Write] Controls whether a given SmartObject can be aggregated in SmartObjectPersistentCollections. SOs in collections
  can be queried and reasoned about even while the actual Actor and its components are not streamed in.
  By default SmartObjects are not placed in collections and are active only as long as the owner-actor remains
  loaded and active (i.e. not streamed out).
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``definition_asset`` (SmartObjectDefinition):  [Read-Write]
  deprecated: Property 'DefinitionAsset' is deprecated.
- ``definition_ref`` (SmartObjectDefinitionReference):  [Read-Write] Reference to Smart Object Definition Asset with parameters.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_smart_object_event`` (SmartObjectComponentEventSignature):  [Read-Write]
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``registered_handle`` (SmartObjectHandle):  [Read-Only] RegisteredHandle != FSmartObjectHandle::Invalid when registered into a collection by SmartObjectSubsystem
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SmartObjectComponent.on_smart_object_event"></a>

#### on\_smart\_object\_event

```python
@property
def on_smart_object_event() -> SmartObjectComponentEventSignature
```

(SmartObjectComponentEventSignature):  [Read-Write]

<a id="unreal.SmartObjectComponent.on_smart_object_event"></a>

#### on\_smart\_object\_event

```python
@on_smart_object_event.setter
def on_smart_object_event(value: SmartObjectComponentEventSignature) -> None
```

<a id="unreal.SmartObjectComponent.registered_handle"></a>

#### registered\_handle

```python
@property
def registered_handle() -> SmartObjectHandle
```

(SmartObjectHandle):  [Read-Only] RegisteredHandle != FSmartObjectHandle::Invalid when registered into a collection by SmartObjectSubsystem

<a id="unreal.SmartObjectComponent.registered_id"></a>

#### registered\_id

```python
@property
def registered_id() -> SmartObjectHandle
```

deprecated: 'registered_id' was renamed to 'registered_handle'.

<a id="unreal.SmartObjectComponent.cached_definition_asset_variation"></a>

#### cached\_definition\_asset\_variation

```python
@property
def cached_definition_asset_variation() -> SmartObjectDefinition
```

(SmartObjectDefinition):  [Read-Write] Do not use directly from native code, use GetDefinition() / SetDefinition() instead.
Also Keeping blueprint accessors for convenience and deprecation purposes.

<a id="unreal.SmartObjectComponent.cached_definition_asset_variation"></a>

#### cached\_definition\_asset\_variation

```python
@cached_definition_asset_variation.setter
def cached_definition_asset_variation(value: SmartObjectDefinition) -> None
```

<a id="unreal.SmartObjectComponent.definition_asset"></a>

#### definition\_asset

```python
@property
def definition_asset() -> SmartObjectDefinition
```

(SmartObjectDefinition):  [Read-Write]
deprecated: Property 'DefinitionAsset' is deprecated.

<a id="unreal.SmartObjectComponent.definition_asset"></a>

#### definition\_asset

```python
@definition_asset.setter
def definition_asset(value: SmartObjectDefinition) -> None
```

<a id="unreal.SmartObjectComponent.set_smart_object_enabled_for_reason"></a>

#### set\_smart\_object\_enabled\_for\_reason

```python
def set_smart_object_enabled_for_reason(reason_tag: GameplayTag,
                                        enabled: bool) -> bool
```

x.set_smart_object_enabled_for_reason(reason_tag, enabled) -> bool
Enables or disables the smart object for the specified reason.

Args:
    reason_tag (GameplayTag): Valid Tag to specify the reason for changing the enabled state of the object. Method will ensure if not valid (i.e. None).
    enabled (bool): If true enables the smart object, disables otherwise.

Returns:
    bool: false if it was not possible to change the enabled state (ie. if it's not registered or there is no smart object subsystem).

<a id="unreal.SmartObjectComponent.set_smart_object_enabled"></a>

#### set\_smart\_object\_enabled

```python
def set_smart_object_enabled(enable: bool) -> bool
```

x.set_smart_object_enabled(enable) -> bool
Enables or disables the smart object using the default reason (i.e. Gameplay).

Args:
    enable (bool): 

Returns:
    bool: false if it was not possible to change the enabled state (ie. if it's not registered or there is no smart object subsystem).

<a id="unreal.SmartObjectComponent.receive_on_event"></a>

#### receive\_on\_event

```python
def receive_on_event(event_data: SmartObjectEventData,
                     interactor: Actor) -> None
```

x.receive_on_event(event_data, interactor) -> None
Receive on Event

Args:
    event_data (SmartObjectEventData): 
    interactor (Actor):

<a id="unreal.SmartObjectComponent.is_smart_object_enabled_for_reason"></a>

#### is\_smart\_object\_enabled\_for\_reason

```python
def is_smart_object_enabled_for_reason(reason_tag: GameplayTag) -> bool
```

x.is_smart_object_enabled_for_reason(reason_tag) -> bool
Returns the enabled state of the smart object based on a specific reason.

Args:
    reason_tag (GameplayTag): Valid Tag to test if enabled for a specific reason. Method will ensure if not valid (i.e. None).

Returns:
    bool: True when associated smart object is set to be enabled. False otherwise.

<a id="unreal.SmartObjectComponent.is_smart_object_enabled"></a>

#### is\_smart\_object\_enabled

```python
def is_smart_object_enabled() -> bool
```

x.is_smart_object_enabled() -> bool
Returns the enabled state of the smart object regardless of the disabled reason.

Returns:
    bool: True when associated smart object is set to be enabled. False otherwise.

<a id="unreal.SmartObjectComponent.is_bound_to_simulation"></a>

#### is\_bound\_to\_simulation

```python
def is_bound_to_simulation() -> bool
```

x.is_bound_to_simulation() -> bool
Returns true if the Smart Object component is registered to the Smart Object subsystem. Depending on the update order, sometimes it is possible that the subsystem gets enabled after the component.

Returns:
    bool:

<a id="unreal.SmartObjectContainerRenderingComponent"></a>