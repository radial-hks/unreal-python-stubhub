## AvaText3DComponent Objects

```python
class AvaText3DComponent(Text3DComponent)
```

Ava Text 3DComponent

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaText3DComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``alignment`` (AvaTextAlignment):  [Read-Write]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``back_material`` (MaterialInterface):  [Read-Write] Material for the back part
- ``bevel`` (float):  [Read-Write] Size of bevel
- ``bevel_color`` (LinearColor):  [Read-Write]
- ``bevel_material`` (MaterialInterface):  [Read-Write] Material for the bevel part
- ``bevel_segments`` (int32):  [Read-Write] Bevel Segments (Defines the amount of tesselation for the bevel part)
- ``bevel_type`` (Text3DBevelType):  [Read-Write] Bevel Type
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the text glyphs should cast a shadow or not.
- ``color`` (LinearColor):  [Read-Write]
- ``coloring_style`` (AvaTextColoringStyle):  [Read-Write]
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``custom_material`` (MaterialInterface):  [Read-Write]
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enforce_upper_case`` (bool):  [Read-Write]
- ``extrude`` (float):  [Read-Write] Size of the extrude
- ``extrude_color`` (LinearColor):  [Read-Write]
- ``extrude_material`` (MaterialInterface):  [Read-Write] Material for the extruded part
- ``font`` (Font):  [Read-Write] Text font
- ``front_material`` (MaterialInterface):  [Read-Write] Material for the front part
- ``gradient_settings`` (AvaLinearGradientSettings):  [Read-Write]
- ``has_max_height`` (bool):  [Read-Write] Enables a maximum height to the 3D Text
- ``has_max_width`` (bool):  [Read-Write] Enables a maximum width to the 3D Text
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``horizontal_alignment`` (Text3DHorizontalTextAlignment):  [Read-Write] Horizontal text alignment
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_unlit`` (bool):  [Read-Write]
- ``kerning`` (float):  [Read-Write] Text kerning
- ``line_spacing`` (float):  [Read-Write] Extra line spacing
- ``main_texture`` (Texture2D):  [Read-Write]
- ``mask_offset`` (float):  [Read-Write]
- ``mask_orientation`` (AvaMaterialMaskOrientation):  [Read-Write]
- ``mask_rotation`` (float):  [Read-Write]
- ``mask_smoothness`` (float):  [Read-Write]
- ``max_height`` (float):  [Read-Write] Sets a maximum height to the 3D Text
- ``max_width`` (float):  [Read-Write] Sets a maximum width to the 3D Text
- ``max_width_handling`` (Text3DMaxWidthHandling):  [Read-Write] Dictates how to handle the text if it exceeds the max width
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``motion_design_font`` (AvaFont):  [Read-Write]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``opacity`` (float):  [Read-Write]
- ``outline`` (bool):  [Read-Write] Generate Outline
- ``outline_expand`` (float):  [Read-Write] Outline expand/offset amount
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``refresh_on_change`` (bool):  [Read-Write] Whether to allow automatic refresh/mesh generation
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``scale_proportionally`` (bool):  [Read-Write] Should the mesh scale proportionally when Max Width/Height is set
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``text`` (Text):  [Read-Write] The text to generate a 3d mesh
- ``text_generated_delegate`` (TextGenerated):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]
- ``translucency_style`` (AvaTextTranslucency):  [Read-Write]
- ``typeface`` (Name):  [Read-Write]
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``vertical_alignment`` (Text3DVerticalTextAlignment):  [Read-Write] Vertical text alignment
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``word_spacing`` (float):  [Read-Write] Extra word spacing

<a id="unreal.AvaTextActor"></a>