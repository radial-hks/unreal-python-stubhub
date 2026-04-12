## CesiumPolygonRasterOverlay Objects

```python
class CesiumPolygonRasterOverlay(CesiumRasterOverlay)
```

A raster overlay that rasterizes polygons and drapes them over the tileset.
This is useful for clipping out parts of a tileset, for adding a water effect
in an area, and for many other purposes.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPolygonRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``exclude_selected_tiles`` (bool):  [Read-Write] Whether tiles that fall entirely within the rasterized selection should be
  excluded from loading and rendering. For better performance, this should be
  enabled when this overlay will be used for clipping. But when this overlay
  is used for other effects, this option should be disabled to avoid missing
  tiles.

  Note that if InvertSelection is true, this will cull tiles that are
  outside of all the polygons. If it is false, this will cull tiles that are
  completely inside at least one polygon.
- ``invert_selection`` (bool):  [Read-Write] Whether to invert the selection specified by the polygons.

  If this is true, only the areas outside of all the polygons will be
  rasterized.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``material_layer_key`` (str):  [Read-Write] The key to use to match this overlay to a material layer.

  When using Material Layers, any material layers inside a "Cesium" layer
  stack with a name that matches this name will have their Texture,
  TranslationScale, and TextureCoordinateIndex properties set automatically
  so that a ML_CesiumOverlay layer function (or similar) will correctly
  sample from this overlay.
- ``maximum_screen_space_error`` (double):  [Read-Write] The maximum number of pixels of error when rendering this overlay.
  This is used to select an appropriate level-of-detail.

  When this property has its default value, 2.0, it means that raster overlay
  images will be sized so that, when zoomed in closest, a single pixel in
  the raster overlay maps to approximately 2x2 pixels on the screen.
- ``maximum_simultaneous_tile_loads`` (int32):  [Read-Write] The maximum number of overlay tiles that may simultaneously be in
  the process of loading.
- ``maximum_texture_size`` (int32):  [Read-Write] The maximum texel size of raster overlay textures, in either
  direction.

  Images created by this overlay will be no more than this number of texels
  in either direction. This may result in reduced raster overlay detail in
  some cases.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``polygons`` (Array[CesiumCartographicPolygon]):  [Read-Write] The polygons to rasterize for this overlay.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``renderer_options`` (RasterOverlayRendererOptions):  [Read-Write] Sets the texture filter and texture group of raster tile images. Depending
  on the project settings, the default texture filter, TF_Default, should
  have the best quality.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``show_credits_on_screen`` (bool):  [Read-Write] Whether or not to show credits of this raster overlay on screen.
- ``sub_tile_cache_bytes`` (int64):  [Read-Write] The maximum number of bytes to use to cache sub-tiles in memory.

  This is used by provider types that have an underlying tiling scheme that
  may not align with the tiling scheme of the geometry tiles on which the
  raster overlay tiles are draped. Because a single sub-tile may overlap
  multiple geometry tiles, it is useful to cache loaded sub-tiles in memory
  in case they're needed again soon. This property controls the maximum size
  of that cache.

<a id="unreal.CesiumPolygonRasterOverlay.polygons"></a>

#### polygons

```python
@property
def polygons() -> Array[CesiumCartographicPolygon]
```

(Array[CesiumCartographicPolygon]):  [Read-Write] The polygons to rasterize for this overlay.

<a id="unreal.CesiumPolygonRasterOverlay.polygons"></a>

#### polygons

```python
@polygons.setter
def polygons(value: Array[CesiumCartographicPolygon]) -> None
```

<a id="unreal.CesiumPolygonRasterOverlay.invert_selection"></a>

#### invert\_selection

```python
@property
def invert_selection() -> bool
```

(bool):  [Read-Write] Whether to invert the selection specified by the polygons.

If this is true, only the areas outside of all the polygons will be
rasterized.

<a id="unreal.CesiumPolygonRasterOverlay.invert_selection"></a>

#### invert\_selection

```python
@invert_selection.setter
def invert_selection(value: bool) -> None
```

<a id="unreal.CesiumPolygonRasterOverlay.exclude_selected_tiles"></a>

#### exclude\_selected\_tiles

```python
@property
def exclude_selected_tiles() -> bool
```

(bool):  [Read-Write] Whether tiles that fall entirely within the rasterized selection should be
excluded from loading and rendering. For better performance, this should be
enabled when this overlay will be used for clipping. But when this overlay
is used for other effects, this option should be disabled to avoid missing
tiles.

Note that if InvertSelection is true, this will cull tiles that are
outside of all the polygons. If it is false, this will cull tiles that are
completely inside at least one polygon.

<a id="unreal.CesiumPolygonRasterOverlay.exclude_selected_tiles"></a>

#### exclude\_selected\_tiles

```python
@exclude_selected_tiles.setter
def exclude_selected_tiles(value: bool) -> None
```

<a id="unreal.CesiumPolygonRasterOverlay.exclude_tiles_inside"></a>

#### exclude\_tiles\_inside

```python
@property
def exclude_tiles_inside() -> bool
```

deprecated: 'exclude_tiles_inside' was renamed to 'exclude_selected_tiles'.

<a id="unreal.CesiumPolygonRasterOverlay.exclude_tiles_inside"></a>

#### exclude\_tiles\_inside

```python
@exclude_tiles_inside.setter
def exclude_tiles_inside(value: bool) -> None
```

<a id="unreal.CesiumPrimitiveFeaturesBlueprintLibrary"></a>