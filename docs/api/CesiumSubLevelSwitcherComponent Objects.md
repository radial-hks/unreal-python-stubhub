## CesiumSubLevelSwitcherComponent Objects

```python
class CesiumSubLevelSwitcherComponent(ActorComponent)
```

Manages the asynchronous switching between sub-levels, making sure that a
previous sub-level is hidden before the CesiumGeoreference is switched to a
new location and the next sub-level is loaded.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSubLevelSwitcherComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.CesiumSubLevelSwitcherComponent.set_target_sub_level"></a>

#### set\_target\_sub\_level

```python
def set_target_sub_level(level_instance: LevelInstance) -> None
```

x.set_target_sub_level(level_instance) -> None
Sets the sub-level that should be active. The switcher will asynchronously
load and show this sub-level.

Args:
    level_instance (LevelInstance):

<a id="unreal.CesiumSubLevelSwitcherComponent.get_target_sub_level"></a>

#### get\_target\_sub\_level

```python
def get_target_sub_level() -> LevelInstance
```

x.get_target_sub_level() -> LevelInstance
Gets the sub-level that is in the process of becoming active. If nullptr,
the target is a state where no sub-levels are active.

Returns:
    LevelInstance:

<a id="unreal.CesiumSubLevelSwitcherComponent.get_registered_sub_levels"></a>

#### get\_registered\_sub\_levels

```python
def get_registered_sub_levels() -> Array[LevelInstance]
```

x.get_registered_sub_levels() -> Array[LevelInstance]
Gets the list of sub-levels that are currently registered with this
switcher.

Returns:
    Array[LevelInstance]:

<a id="unreal.CesiumSubLevelSwitcherComponent.get_current_sub_level"></a>

#### get\_current\_sub\_level

```python
def get_current_sub_level() -> LevelInstance
```

x.get_current_sub_level() -> LevelInstance
Gets the sub-level that is currently active, or nullptr if none are active.

Returns:
    LevelInstance:

<a id="unreal.CesiumSunSky"></a>