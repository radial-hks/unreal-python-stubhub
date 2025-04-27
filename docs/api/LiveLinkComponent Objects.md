## LiveLinkComponent Objects

```python
class LiveLinkComponent(ActorComponent)
```

An actor component to enable accessing LiveLink data in Blueprints.
Data can be accessed in Editor through the "OnLiveLinkUpdated" event.
Any Skeletal Mesh Components on the parent will be set to animate in editor causing their AnimBPs to run.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkComponent.h

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
- ``on_live_link_updated`` (LiveLinkTickSignature):  [Read-Write] This Event is triggered any time new LiveLink data is available, including in the editor
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.LiveLinkComponent.on_live_link_updated"></a>

#### on_live_link_updated

```python
@property
def on_live_link_updated() -> LiveLinkTickSignature
```

(LiveLinkTickSignature):  [Read-Write] This Event is triggered any time new LiveLink data is available, including in the editor

<a id="unreal.LiveLinkComponent.on_live_link_updated"></a>

#### on_live_link_updated

```python
@on_live_link_updated.setter
def on_live_link_updated(value: LiveLinkTickSignature) -> None
```

<a id="unreal.LiveLinkComponent.get_subject_data_at_world_time"></a>

#### get_subject_data_at_world_time

```python
def get_subject_data_at_world_time(
        subject_name: Name,
        world_time: float) -> Tuple[bool, SubjectFrameHandle]
```

x.get_subject_data_at_world_time(subject_name, world_time) -> (success=bool, subject_frame_handle=SubjectFrameHandle)
Get Subject Data at World Time
deprecated: GetSubjectDataAtWorldTime is deprecated, use EvaluateLiveLinkFrameAtWorldTime.

Args:
    subject_name (Name): 
    world_time (float): 

Returns:
    tuple: 

    success (bool): 

    subject_frame_handle (SubjectFrameHandle):

<a id="unreal.LiveLinkComponent.get_subject_data_at_scene_time"></a>

#### get_subject_data_at_scene_time

```python
def get_subject_data_at_scene_time(
        subject_name: Name,
        scene_time: Timecode) -> Tuple[bool, SubjectFrameHandle]
```

x.get_subject_data_at_scene_time(subject_name, scene_time) -> (success=bool, subject_frame_handle=SubjectFrameHandle)
Get Subject Data at Scene Time
deprecated: GetSubjectDataAtSceneTime is deprecated, use EvaluateLiveLinkFrameAtSceneTime.

Args:
    subject_name (Name): 
    scene_time (Timecode): 

Returns:
    tuple: 

    success (bool): 

    subject_frame_handle (SubjectFrameHandle):

<a id="unreal.LiveLinkComponent.get_subject_data"></a>

#### get_subject_data

```python
def get_subject_data(subject_name: Name) -> Tuple[bool, SubjectFrameHandle]
```

x.get_subject_data(subject_name) -> (success=bool, subject_frame_handle=SubjectFrameHandle)
Get Subject Data
deprecated: GetSubjectData is deprecated, EvaluateLiveLinkFrame.

Args:
    subject_name (Name): 

Returns:
    tuple: 

    success (bool): 

    subject_frame_handle (SubjectFrameHandle):

<a id="unreal.LiveLinkComponent.get_available_subject_names"></a>

#### get_available_subject_names

```python
def get_available_subject_names() -> Array[Name]
```

x.get_available_subject_names() -> Array[Name]
Get Available Subject Names
deprecated: GetAvailableSubjectNames is deprecated, use GetLiveLinkEnabledSubjectNames.

Returns:
    Array[Name]: 

    subject_names (Array[Name]):

<a id="unreal.LiveLinkDrivenComponent"></a>