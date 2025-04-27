## NavModifierComponent Objects

```python
class NavModifierComponent(NavRelevantComponent)
```

Nav Modifier Component

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavModifierComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_class`` (type(Class)):  [Read-Write] NavArea to apply inside the defined volume.
- ``area_class_to_replace`` (type(Class)):  [Read-Write] When setting this value, the modifier behavior changes : it will now replace any surface marked by AreaClassToReplace in the volume and replace it with AreaClass.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``failsafe_extent`` (Vector):  [Read-Write] box extent used ONLY when owning actor doesn't have collision component
- ``include_agent_height`` (bool):  [Read-Write] Setting to 'true' will result in expanding lower bounding box of the nav
      modifier by agent's height, before applying to navmesh
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``nav_mesh_resolution`` (NavigationDataResolution):  [Read-Write] Experimental: Indicates which navmesh resolution should be used around the actor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.NavModifierComponent.area_class"></a>

#### area_class

```python
@property
def area_class() -> Class
```

(type(Class)):  [Read-Only] NavArea to apply inside the defined volume.

<a id="unreal.NavModifierComponent.area_class_to_replace"></a>

#### area_class_to_replace

```python
@property
def area_class_to_replace() -> Class
```

(type(Class)):  [Read-Only] When setting this value, the modifier behavior changes : it will now replace any surface marked by AreaClassToReplace in the volume and replace it with AreaClass.

<a id="unreal.NavModifierComponent.set_area_class_to_replace"></a>

#### set_area_class_to_replace

```python
def set_area_class_to_replace(new_area_class_to_replace: Class) -> None
```

x.set_area_class_to_replace(new_area_class_to_replace) -> None
Set Area Class to Replace

Args:
    new_area_class_to_replace (type(Class)):

<a id="unreal.NavModifierComponent.set_area_class"></a>

#### set_area_class

```python
def set_area_class(new_area_class: Class) -> None
```

x.set_area_class(new_area_class) -> None
Set Area Class

Args:
    new_area_class (type(Class)):

<a id="unreal.NavModifierVolume"></a>