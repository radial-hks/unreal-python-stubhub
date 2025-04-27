## LiveLinkComponentController Objects

```python
class LiveLinkComponentController(ActorComponent)
```

Live Link Component Controller

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkComponents
- **File**: LiveLinkComponentController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``controller_map`` (Map[type(Class), LiveLinkControllerBase]):  [Read-Write] Instanced controllers used to control the desired role
- ``disable_evaluate_live_link_when_spawnable`` (bool):  [Read-Write] If true, will not evaluate LiveLink if the attached actor is a spawnable in Sequencer
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``evaluate_live_link`` (bool):  [Read-Write] If false, will not evaluate live link, effectively pausing.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_controller_map_updated_delegate`` (OnControllerMapUpdatedDelegate):  [Read-Write] This Event is triggered any time the controller map is updated
- ``on_live_link_updated`` (LiveLinkTickDelegate):  [Read-Write] This Event is triggered any time new LiveLink data is available, including in the editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``subject_representation`` (LiveLinkSubjectRepresentation):  [Read-Write]
- ``update_in_editor`` (bool):  [Read-Write]
- ``update_in_preview_editor`` (bool):  [Read-Write] If true, will tick when the world is a preview (i.e Blueprint editors)

<a id="unreal.LiveLinkComponentController.subject_representation"></a>

#### subject_representation

```python
@property
def subject_representation() -> LiveLinkSubjectRepresentation
```

(LiveLinkSubjectRepresentation):  [Read-Write]

<a id="unreal.LiveLinkComponentController.subject_representation"></a>

#### subject_representation

```python
@subject_representation.setter
def subject_representation(value: LiveLinkSubjectRepresentation) -> None
```

<a id="unreal.LiveLinkComponentController.controller_map"></a>

#### controller_map

```python
@property
def controller_map() -> Map[Class, LiveLinkControllerBase]
```

(Map[type(Class), LiveLinkControllerBase]):  [Read-Only] Instanced controllers used to control the desired role

<a id="unreal.LiveLinkComponentController.on_live_link_updated"></a>

#### on_live_link_updated

```python
@property
def on_live_link_updated() -> LiveLinkTickDelegate
```

(LiveLinkTickDelegate):  [Read-Write] This Event is triggered any time new LiveLink data is available, including in the editor

<a id="unreal.LiveLinkComponentController.on_live_link_updated"></a>

#### on_live_link_updated

```python
@on_live_link_updated.setter
def on_live_link_updated(value: LiveLinkTickDelegate) -> None
```

<a id="unreal.LiveLinkComponentController.on_controller_map_updated_delegate"></a>

#### on_controller_map_updated_delegate

```python
@property
def on_controller_map_updated_delegate() -> OnControllerMapUpdatedDelegate
```

(OnControllerMapUpdatedDelegate):  [Read-Write] This Event is triggered any time the controller map is updated

<a id="unreal.LiveLinkComponentController.on_controller_map_updated_delegate"></a>

#### on_controller_map_updated_delegate

```python
@on_controller_map_updated_delegate.setter
def on_controller_map_updated_delegate(
        value: OnControllerMapUpdatedDelegate) -> None
```

<a id="unreal.LiveLinkComponentController.disable_evaluate_live_link_when_spawnable"></a>

#### disable_evaluate_live_link_when_spawnable

```python
@property
def disable_evaluate_live_link_when_spawnable() -> bool
```

(bool):  [Read-Write] If true, will not evaluate LiveLink if the attached actor is a spawnable in Sequencer

<a id="unreal.LiveLinkComponentController.disable_evaluate_live_link_when_spawnable"></a>

#### disable_evaluate_live_link_when_spawnable

```python
@disable_evaluate_live_link_when_spawnable.setter
def disable_evaluate_live_link_when_spawnable(value: bool) -> None
```

<a id="unreal.LiveLinkComponentController.evaluate_live_link"></a>

#### evaluate_live_link

```python
@property
def evaluate_live_link() -> bool
```

(bool):  [Read-Write] If false, will not evaluate live link, effectively pausing.

<a id="unreal.LiveLinkComponentController.evaluate_live_link"></a>

#### evaluate_live_link

```python
@evaluate_live_link.setter
def evaluate_live_link(value: bool) -> None
```

<a id="unreal.LiveLinkComponentController.set_controlled_component"></a>

#### set_controlled_component

```python
def set_controlled_component(role_class: Class,
                             component: ActorComponent) -> None
```

x.set_controlled_component(role_class, component) -> None
Set the component to control for the LiveLink controller of the input Role

Args:
    role_class (type(Class)): 
    component (ActorComponent):

<a id="unreal.LiveLinkComponentController.get_controlled_component"></a>

#### get_controlled_component

```python
def get_controlled_component(role_class: Class) -> ActorComponent
```

x.get_controlled_component(role_class) -> ActorComponent
Returns the component controlled by the LiveLink controller of the input Role. Returns null if there is no controller for that Role

Args:
    role_class (type(Class)): 

Returns:
    ActorComponent:

<a id="unreal.VariantManagerLibrary"></a>