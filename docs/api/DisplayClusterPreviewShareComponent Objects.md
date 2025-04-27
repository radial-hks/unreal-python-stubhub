## DisplayClusterPreviewShareComponent Objects

```python
class DisplayClusterPreviewShareComponent(ActorComponent)
```

nDisplay Viewport preview share component

It shares using Shared Memory Media the viewport textures of the parent nDisplay Actor.
It should only be added to DisplayClusterRootActor instances, and only one component per instance.
The way it works is that the sender generates a unique name for each viewport and captures its texture
by getting a pointer to it from the corresponding Preview Component.
The receiver will read it using the corresponding media source, and use the Texture Replace functionality
in the nDisplay actor viewports to have them used and displayed.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterPreviewShareComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``icvfx_cameras_sync_type`` (DisplayClusterPreviewShareIcvfxSync):  [Read-Write] Type of Icvfx camera sync to be performed between the Source nDisplay actor and the owner of this component
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mode`` (DisplayClusterPreviewShareMode):  [Read-Write] Current sharing mode of this component
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``source_n_display_actor`` (DisplayClusterRootActor):  [Read-Write] The source nDisplay actor to pull the preview from
- ``unique_name`` (str):  [Read-Write] Current unique name of this component, which should match between sender and receiver of viewport textures

<a id="unreal.DisplayClusterPreviewShareComponent.mode"></a>

#### mode

```python
@property
def mode() -> DisplayClusterPreviewShareMode
```

(DisplayClusterPreviewShareMode):  [Read-Write] Current sharing mode of this component

<a id="unreal.DisplayClusterPreviewShareComponent.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DisplayClusterPreviewShareMode) -> None
```

<a id="unreal.DisplayClusterPreviewShareComponent.unique_name"></a>

#### unique_name

```python
@property
def unique_name() -> str
```

(str):  [Read-Write] Current unique name of this component, which should match between sender and receiver of viewport textures

<a id="unreal.DisplayClusterPreviewShareComponent.unique_name"></a>

#### unique_name

```python
@unique_name.setter
def unique_name(value: str) -> None
```

<a id="unreal.DisplayClusterPreviewShareComponent.set_unique_name"></a>

#### set_unique_name

```python
def set_unique_name(new_unique_name: str) -> None
```

x.set_unique_name(new_unique_name) -> None
Sets the unique name, which should match between sender and receiver of viewport textures

Args:
    new_unique_name (str):

<a id="unreal.DisplayClusterPreviewShareComponent.set_mode"></a>

#### set_mode

```python
def set_mode(new_mode: DisplayClusterPreviewShareMode) -> None
```

x.set_mode(new_mode) -> None
Sets the sharing mode

Args:
    new_mode (DisplayClusterPreviewShareMode):

<a id="unreal.DisplayClusterRootActor"></a>