## LandscapeLayerInfoObject Objects

```python
class LandscapeLayerInfoObject(Object)
```

Landscape Layer Info Object

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeLayerInfoObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hardness`` (float):  [Read-Write] Defines how much 'resistance' areas painted with this layer will offer to the Erosion tool. A hardness of 0 means the layer is fully affected by erosion, while 1 means fully unaffected.
- ``layer_name`` (Name):  [Read-Only]
- ``layer_usage_debug_color`` (LinearColor):  [Read-Write] The color to use for layer usage debug
- ``minimum_collision_relevance_weight`` (float):  [Read-Write] The minimum weight that needs to be painted for that layer to be picked up as the dominant physical layer.
- ``no_weight_blend`` (bool):  [Read-Write] Prevents this layer to be weight-blended with others.
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use when this layer is the predominant one at a given location. Note: this is ignored if the Landscape Physical Material node is used in the landscape material.
- ``spline_falloff_modulation_bias`` (float):  [Read-Write] Defines the offset to use when sampling the Spline Falloff Modulation Texture.
- ``spline_falloff_modulation_color_mask`` (SplineModulationColorMask):  [Read-Write] Defines which channel of the Spline Falloff Modulation Texture to use.
- ``spline_falloff_modulation_scale`` (float):  [Read-Write] Allows to scale the value sampled from the Spline Falloff Modulation Texture.
- ``spline_falloff_modulation_texture`` (Texture2D):  [Read-Write] Texture to modulate the Splines Falloff Layer Alpha
- ``spline_falloff_modulation_tiling`` (float):  [Read-Write] Defines the tiling to use when sampling the Spline Falloff Modulation Texture.

<a id="unreal.MaterialInstance"></a>