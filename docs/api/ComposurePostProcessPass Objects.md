## ComposurePostProcessPass Objects

```python
class ComposurePostProcessPass(SceneComponent)
```

In engine post process based pass.

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposurePostProcessPass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
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

<a id="unreal.ComposurePostProcessPass.set_setup_material"></a>

#### set_setup_material

```python
def set_setup_material(material: MaterialInterface) -> None
```

x.set_setup_material(material) -> None
Sets a custom setup post process material. The material location must be set at BeforeTranslucency.

Args:
    material (MaterialInterface):

<a id="unreal.ComposurePostProcessPass.set_output_render_target"></a>

#### set_output_render_target

```python
def set_output_render_target(render_target: TextureRenderTarget2D) -> None
```

x.set_output_render_target(render_target) -> None
Sets current output render target.

Args:
    render_target (TextureRenderTarget2D):

<a id="unreal.ComposurePostProcessPass.get_setup_material"></a>

#### get_setup_material

```python
def get_setup_material() -> MaterialInterface
```

x.get_setup_material() -> MaterialInterface
Gets current setup material.

Returns:
    MaterialInterface:

<a id="unreal.ComposurePostProcessPass.get_output_render_target"></a>

#### get_output_render_target

```python
def get_output_render_target() -> TextureRenderTarget2D
```

x.get_output_render_target() -> TextureRenderTarget2D
Gets current output render target.

Returns:
    TextureRenderTarget2D:

<a id="unreal.ComposureLensBloomPass"></a>