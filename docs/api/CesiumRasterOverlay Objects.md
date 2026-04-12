## CesiumRasterOverlay Objects

```python
class CesiumRasterOverlay(ActorComponent)
```

A quadtree pyramid of 2D raster images meant to be draped over a Cesium 3D
Tileset. Raster overlays are commonly used for satellite imagery, street
maps, and more.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
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

<a id="unreal.CesiumRasterOverlay.material_layer_key"></a>

#### material\_layer\_key

```python
@property
def material_layer_key() -> str
```

(str):  [Read-Write] The key to use to match this overlay to a material layer.

When using Material Layers, any material layers inside a "Cesium" layer
stack with a name that matches this name will have their Texture,
TranslationScale, and TextureCoordinateIndex properties set automatically
so that a ML_CesiumOverlay layer function (or similar) will correctly
sample from this overlay.

<a id="unreal.CesiumRasterOverlay.material_layer_key"></a>

#### material\_layer\_key

```python
@material_layer_key.setter
def material_layer_key(value: str) -> None
```

<a id="unreal.CesiumRasterOverlay.renderer_options"></a>

#### renderer\_options

```python
@property
def renderer_options() -> RasterOverlayRendererOptions
```

(RasterOverlayRendererOptions):  [Read-Write] Sets the texture filter and texture group of raster tile images. Depending
on the project settings, the default texture filter, TF_Default, should
have the best quality.

<a id="unreal.CesiumRasterOverlay.renderer_options"></a>

#### renderer\_options

```python
@renderer_options.setter
def renderer_options(value: RasterOverlayRendererOptions) -> None
```

<a id="unreal.CesiumRasterOverlay.maximum_screen_space_error"></a>

#### maximum\_screen\_space\_error

```python
@property
def maximum_screen_space_error() -> float
```

(double):  [Read-Write] The maximum number of pixels of error when rendering this overlay.
This is used to select an appropriate level-of-detail.

When this property has its default value, 2.0, it means that raster overlay
images will be sized so that, when zoomed in closest, a single pixel in
the raster overlay maps to approximately 2x2 pixels on the screen.

<a id="unreal.CesiumRasterOverlay.maximum_screen_space_error"></a>

#### maximum\_screen\_space\_error

```python
@maximum_screen_space_error.setter
def maximum_screen_space_error(value: float) -> None
```

<a id="unreal.CesiumRasterOverlay.maximum_texture_size"></a>

#### maximum\_texture\_size

```python
@property
def maximum_texture_size() -> int
```

(int32):  [Read-Write] The maximum texel size of raster overlay textures, in either
direction.

Images created by this overlay will be no more than this number of texels
in either direction. This may result in reduced raster overlay detail in
some cases.

<a id="unreal.CesiumRasterOverlay.maximum_texture_size"></a>

#### maximum\_texture\_size

```python
@maximum_texture_size.setter
def maximum_texture_size(value: int) -> None
```

<a id="unreal.CesiumRasterOverlay.maximum_simultaneous_tile_loads"></a>

#### maximum\_simultaneous\_tile\_loads

```python
@property
def maximum_simultaneous_tile_loads() -> int
```

(int32):  [Read-Write] The maximum number of overlay tiles that may simultaneously be in
the process of loading.

<a id="unreal.CesiumRasterOverlay.maximum_simultaneous_tile_loads"></a>

#### maximum\_simultaneous\_tile\_loads

```python
@maximum_simultaneous_tile_loads.setter
def maximum_simultaneous_tile_loads(value: int) -> None
```

<a id="unreal.CesiumRasterOverlay.sub_tile_cache_bytes"></a>

#### sub\_tile\_cache\_bytes

```python
@property
def sub_tile_cache_bytes() -> int
```

(int64):  [Read-Write] The maximum number of bytes to use to cache sub-tiles in memory.

This is used by provider types that have an underlying tiling scheme that
may not align with the tiling scheme of the geometry tiles on which the
raster overlay tiles are draped. Because a single sub-tile may overlap
multiple geometry tiles, it is useful to cache loaded sub-tiles in memory
in case they're needed again soon. This property controls the maximum size
of that cache.

<a id="unreal.CesiumRasterOverlay.sub_tile_cache_bytes"></a>

#### sub\_tile\_cache\_bytes

```python
@sub_tile_cache_bytes.setter
def sub_tile_cache_bytes(value: int) -> None
```

<a id="unreal.CesiumRasterOverlay.show_credits_on_screen"></a>

#### show\_credits\_on\_screen

```python
@property
def show_credits_on_screen() -> bool
```

(bool):  [Read-Write] Whether or not to show credits of this raster overlay on screen.

<a id="unreal.CesiumRasterOverlay.show_credits_on_screen"></a>

#### show\_credits\_on\_screen

```python
@show_credits_on_screen.setter
def show_credits_on_screen(value: bool) -> None
```

<a id="unreal.CesiumRasterOverlay.set_sub_tile_cache_bytes"></a>

#### set\_sub\_tile\_cache\_bytes

```python
def set_sub_tile_cache_bytes(value: int) -> None
```

x.set_sub_tile_cache_bytes(value) -> None
Set Sub Tile Cache Bytes

Args:
    value (int64):

<a id="unreal.CesiumRasterOverlay.set_maximum_texture_size"></a>

#### set\_maximum\_texture\_size

```python
def set_maximum_texture_size(value: int) -> None
```

x.set_maximum_texture_size(value) -> None
Set Maximum Texture Size

Args:
    value (int32):

<a id="unreal.CesiumRasterOverlay.set_maximum_simultaneous_tile_loads"></a>

#### set\_maximum\_simultaneous\_tile\_loads

```python
def set_maximum_simultaneous_tile_loads(value: int) -> None
```

x.set_maximum_simultaneous_tile_loads(value) -> None
Set Maximum Simultaneous Tile Loads

Args:
    value (int32):

<a id="unreal.CesiumRasterOverlay.set_maximum_screen_space_error"></a>

#### set\_maximum\_screen\_space\_error

```python
def set_maximum_screen_space_error(value: float) -> None
```

x.set_maximum_screen_space_error(value) -> None
Set Maximum Screen Space Error

Args:
    value (double):

<a id="unreal.CesiumRasterOverlay.remove_from_tileset"></a>

#### remove\_from\_tileset

```python
def remove_from_tileset() -> None
```

x.remove_from_tileset() -> None
Stops displaying this raster overlay on its owning Cesium 3D Tileset Actor.
It is usually better to call Deactivate rather than this function, in order
to ensure that the component is also deactivated. Otherwise, if the
component remains active and the Cesium3DTileset is reloaded for any
reason, this overlay will reappear.

If the overlay is not yet added or if this component's Owner is not a
Cesium 3D Tileset, this method does nothing.

<a id="unreal.CesiumRasterOverlay.refresh"></a>

#### refresh

```python
def refresh() -> None
```

x.refresh() -> None
Refreshes this overlay by removing from its owning Cesium 3D Tileset Actor
and re-adding it. If this component's Owner is not a Cesium 3D Tileset
Actor, this method does nothing. If this component is not active, the
overlay will be removed from the Cesium3DTileset if already present but not
re-added.

<a id="unreal.CesiumRasterOverlay.get_sub_tile_cache_bytes"></a>

#### get\_sub\_tile\_cache\_bytes

```python
def get_sub_tile_cache_bytes() -> int
```

x.get_sub_tile_cache_bytes() -> int64
Get Sub Tile Cache Bytes

Returns:
    int64:

<a id="unreal.CesiumRasterOverlay.get_maximum_texture_size"></a>

#### get\_maximum\_texture\_size

```python
def get_maximum_texture_size() -> int
```

x.get_maximum_texture_size() -> int32
Get Maximum Texture Size

Returns:
    int32:

<a id="unreal.CesiumRasterOverlay.get_maximum_simultaneous_tile_loads"></a>

#### get\_maximum\_simultaneous\_tile\_loads

```python
def get_maximum_simultaneous_tile_loads() -> int
```

x.get_maximum_simultaneous_tile_loads() -> int32
Get Maximum Simultaneous Tile Loads

Returns:
    int32:

<a id="unreal.CesiumRasterOverlay.get_maximum_screen_space_error"></a>

#### get\_maximum\_screen\_space\_error

```python
def get_maximum_screen_space_error() -> float
```

x.get_maximum_screen_space_error() -> double
Get Maximum Screen Space Error

Returns:
    double:

<a id="unreal.CesiumRasterOverlay.add_to_tileset"></a>

#### add\_to\_tileset

```python
def add_to_tileset() -> None
```

x.add_to_tileset() -> None
Displays this raster overlay on its owning Cesium 3D Tileset Actor, without
changing its activation state. It is usually better to call Activate
rather than this function, in order to ensure that the component is also
activated. Otherwise, if the Cesium3DTileset is reloaded for any reason,
this overlay will no longer be shown.

If the overlay is already added or if this component's Owner is not a
Cesium 3D Tileset, this method does nothing.

<a id="unreal.CesiumBingMapsRasterOverlay"></a>