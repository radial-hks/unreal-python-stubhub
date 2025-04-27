## ComposureCompositingTargetComponent Objects

```python
class ComposureCompositingTargetComponent(ActorComponent)
```

Component intended to replace UComposurePlayerCompositingTarget - a object to bind to a APlayerCameraManager
with a UTextureRenderTarget2D to be used as a player's render target.
Made into a component so we can hook into preview rendering in editor.

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposurePlayerCompositingTarget.h

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

<a id="unreal.ComposureCompositingTargetComponent.set_display_texture"></a>

#### set_display_texture

```python
def set_display_texture(display_texture: Texture) -> None
```

x.set_display_texture(display_texture) -> None
Set Display Texture

Args:
    display_texture (Texture):

<a id="unreal.ComposureCompositingTargetComponent.get_display_texture"></a>

#### get_display_texture

```python
def get_display_texture() -> Texture
```

x.get_display_texture() -> Texture
Get Display Texture

Returns:
    Texture:

<a id="unreal.ComposurePostProcessingPassProxy"></a>