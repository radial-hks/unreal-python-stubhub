## MagicGISLineDecalComponent Objects

```python
class MagicGISLineDecalComponent(DecalComponent)
```

Magic GISLine Decal Component

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISLineDecalComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``decal_color`` (LinearColor):  [Read-Write] Decal color, can be accessed using the material Decal Color node.
- ``decal_material`` (MaterialInterface):  [Read-Write] Decal material.
- ``decal_size`` (Vector):  [Read-Write] Decal size in local space (does not include the component scale), technically redundant but there for convenience
- ``destroy_owner_after_fade`` (bool):  [Read-Write] Automatically destroys the owning actor after fully fading out.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``fade_duration`` (float):  [Read-Write] Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game.
- ``fade_in_duration`` (float):  [Read-Write]
- ``fade_in_start_delay`` (float):  [Read-Write]
- ``fade_screen_size`` (float):  [Read-Write]
- ``fade_start_delay`` (float):  [Read-Write] Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent.
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
- ``sort_order`` (int32):  [Read-Write] Controls the order in which decal elements are rendered.  Higher values draw later (on top).
  Setting many different sort orders on many different decals prevents sorting by state and can reduce performance.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.MagicGISLineDecalComponent.init_decal_data_all_in_one"></a>

#### init\_decal\_data\_all\_in\_one

```python
def init_decal_data_all_in_one(
        in_data: Array[GISLineDataForGenerator]) -> bool
```

x.init_decal_data_all_in_one(in_data) -> bool
Init Decal Data All in One

Args:
    in_data (Array[GISLineDataForGenerator]): 

Returns:
    bool:

<a id="unreal.MagicGISLineDecalComponent.init_decal_data"></a>

#### init\_decal\_data

```python
def init_decal_data(in_line_points: Array[Vector], in_line_width: float,
                    in_line_color: Color) -> bool
```

x.init_decal_data(in_line_points, in_line_width, in_line_color) -> bool
Init Decal Data

Args:
    in_line_points (Array[Vector]): 
    in_line_width (float): 
    in_line_color (Color): 

Returns:
    bool:

<a id="unreal.MagicGISMeshComponent"></a>