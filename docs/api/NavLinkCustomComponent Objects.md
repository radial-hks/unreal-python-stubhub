## NavLinkCustomComponent Objects

```python
class NavLinkCustomComponent(NavRelevantComponent)
```

Encapsulates NavLinkCustomInterface interface, can be used with Actors not relevant for navigation

Additional functionality:
- can be toggled
- can create obstacle area for easier/forced separation of link end points
- can broadcast state changes to nearby agents

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavLinkCustomComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``broadcast_channel`` (CollisionChannel):  [Read-Write] trace channel for state change broadcast
- ``broadcast_interval`` (float):  [Read-Write] interval for state change broadcast (0 = single broadcast)
- ``broadcast_radius`` (float):  [Read-Write] radius of state change broadcast
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``create_box_obstacle`` (bool):  [Read-Write] if set, box obstacle area will be added to generation
- ``disabled_area_class`` (type(Class)):  [Read-Write] area class to use when link is disabled
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enabled_area_class`` (type(Class)):  [Read-Write] area class to use when link is enabled
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``link_direction`` (NavLinkDirection):  [Read-Write] direction of link
- ``link_enabled`` (bool):  [Read-Write] is link currently in enabled state? (area class)
- ``link_relative_end`` (Vector):  [Read-Write] end point, relative to owner
- ``link_relative_start`` (Vector):  [Read-Write] start point, relative to owner
- ``notify_when_disabled`` (bool):  [Read-Write] should link notify nearby agents when it changes state to disabled
- ``notify_when_enabled`` (bool):  [Read-Write] should link notify nearby agents when it changes state to enabled
- ``obstacle_area_class`` (type(Class)):  [Read-Write] area class for simple box obstacle
- ``obstacle_extent`` (Vector):  [Read-Write] extent of simple box obstacle
- ``obstacle_offset`` (Vector):  [Read-Write] offset of simple box obstacle
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``supported_agents`` (NavAgentSelector):  [Read-Write] restrict area only to specified agents

<a id="unreal.SmartNavLinkComponent"></a>