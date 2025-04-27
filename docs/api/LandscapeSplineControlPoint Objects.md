## LandscapeSplineControlPoint Objects

```python
class LandscapeSplineControlPoint(Object)
```

Landscape Spline Control Point

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeSplineControlPoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``body_instance`` (BodyInstance):  [Read-Write] Mesh Collision Settings
- ``cast_shadow`` (bool):  [Read-Write] Whether the Control Point Mesh should cast a shadow.
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``end_falloff`` (float):  [Read-Write] Falloff at the start/end of the spline (if this point is a start or end point, otherwise ignored).
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the mesh in game
- ``layer_name`` (Name):  [Read-Write] Name of blend layer to paint when applying spline to landscape
  If "none", no layer is painted
- ``layer_width_ratio`` (float):  [Read-Write] Layer Width ratio of the spline at this point.
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance for the mesh used on this control point
- ``left_side_falloff_factor`` (float):  [Read-Write]
- ``left_side_layer_falloff_factor`` (float):  [Read-Write]
- ``location`` (Vector):  [Read-Write] Location in Landscape-space
- ``lower_terrain`` (bool):  [Read-Write] If the spline is below the terrain, whether to lower the terrain down to the level of the spline when applying it to the landscape.
- ``material_overrides`` (Array[MaterialInterface]):  [Read-Write] Overrides mesh's materials
- ``mesh`` (StaticMesh):  [Read-Write] Mesh to use on the control point
- ``mesh_scale`` (Vector):  [Read-Write] Scale of the control point mesh
- ``place_spline_meshes_in_streaming_levels`` (bool):  [Read-Write] Whether control point mesh should be placed in landscape proxy streaming level (true) or the spline's level (false)
- ``raise_terrain`` (bool):  [Read-Write] If the spline is above the terrain, whether to raise the terrain up to the level of the spline when applying it to the landscape.
- ``render_custom_depth`` (bool):  [Read-Write] If true, this component will be rendered in the CustomDepth pass (usually used for outlines)
- ``right_side_falloff_factor`` (float):  [Read-Write]
- ``right_side_layer_falloff_factor`` (float):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write] Rotation of tangent vector at this point (in landscape-space)
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the spline segment.
  The material also needs to be set up to output to a virtual texture.
- ``segment_mesh_offset`` (float):  [Read-Write] Vertical offset of the spline segment mesh. Useful for a river's surface, among other things.
- ``side_falloff`` (float):  [Read-Write] Falloff at the sides of the spline at this point.
- ``translucency_sort_priority`` (int32):  [Read-Write] Translucent objects with a lower sort priority draw behind objects with a higher priority.
  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
  This setting is also used to sort objects being drawn into a runtime virtual texture.

  Ignored if the object is not translucent.  The default priority is zero.
  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.
- ``virtual_texture_cull_mips`` (int32):  [Read-Write] Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
  Larger values reduce the effective draw distance in the runtime virtual texture.
  This culling method doesn't take into account primitive size or virtual texture size.
- ``virtual_texture_lod_bias`` (int32):  [Read-Write] Lod bias for rendering to runtime virtual texture.
- ``virtual_texture_main_pass_max_draw_distance`` (float):  [Read-Write] Desired cull distance in the main pass if we are rendering to both the virtual texture AND the main pass. A value of 0 has no effect.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``width`` (float):  [Read-Write] Half-Width of the spline at this point.

<a id="unreal.LandscapeSplineControlPoint.body_instance"></a>

#### body_instance

```python
@property
def body_instance() -> BodyInstance
```

(BodyInstance):  [Read-Only] Mesh Collision Settings

<a id="unreal.LandscapeSplineSegment"></a>