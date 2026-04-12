## CesiumWebMapServiceRasterOverlay Objects

```python
class CesiumWebMapServiceRasterOverlay(CesiumRasterOverlay)
```

A raster overlay that directly accesses a Web Map Service (WMS) server.
https://www.ogc.org/standards/wms

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumWebMapServiceRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``base_url`` (str):  [Read-Write] The base url of the Web Map Service (WMS).
  e.g.
  https://services.ga.gov.au/gis/services/NM_Culture_and_Infrastructure/MapServer/WMSServer
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``layers`` (str):  [Read-Write] Comma-separated layer names to request from the server.
- ``material_layer_key`` (str):  [Read-Write] The key to use to match this overlay to a material layer.

  When using Material Layers, any material layers inside a "Cesium" layer
  stack with a name that matches this name will have their Texture,
  TranslationScale, and TextureCoordinateIndex properties set automatically
  so that a ML_CesiumOverlay layer function (or similar) will correctly
  sample from this overlay.
- ``maximum_level`` (int32):  [Read-Write] Maximum zoom level.
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
- ``minimum_level`` (int32):  [Read-Write] Minimum zoom level.

  Take care when specifying this that the number of tiles at the minimum
  level is small, such as four or less. A larger number is likely to
  result in rendering problems.
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
- ``tile_height`` (int32):  [Read-Write] Image height
- ``tile_width`` (int32):  [Read-Write] Image width

<a id="unreal.CesiumWebMapServiceRasterOverlay.base_url"></a>

#### base\_url

```python
@property
def base_url() -> str
```

(str):  [Read-Write] The base url of the Web Map Service (WMS).
e.g.
https://services.ga.gov.au/gis/services/NM_Culture_and_Infrastructure/MapServer/WMSServer

<a id="unreal.CesiumWebMapServiceRasterOverlay.base_url"></a>

#### base\_url

```python
@base_url.setter
def base_url(value: str) -> None
```

<a id="unreal.CesiumWebMapServiceRasterOverlay.layers"></a>

#### layers

```python
@property
def layers() -> str
```

(str):  [Read-Write] Comma-separated layer names to request from the server.

<a id="unreal.CesiumWebMapServiceRasterOverlay.layers"></a>

#### layers

```python
@layers.setter
def layers(value: str) -> None
```

<a id="unreal.CesiumWebMapServiceRasterOverlay.tile_width"></a>

#### tile\_width

```python
@property
def tile_width() -> int
```

(int32):  [Read-Write] Image width

<a id="unreal.CesiumWebMapServiceRasterOverlay.tile_width"></a>

#### tile\_width

```python
@tile_width.setter
def tile_width(value: int) -> None
```

<a id="unreal.CesiumWebMapServiceRasterOverlay.tile_height"></a>

#### tile\_height

```python
@property
def tile_height() -> int
```

(int32):  [Read-Write] Image height

<a id="unreal.CesiumWebMapServiceRasterOverlay.tile_height"></a>

#### tile\_height

```python
@tile_height.setter
def tile_height(value: int) -> None
```

<a id="unreal.CesiumWebMapServiceRasterOverlay.minimum_level"></a>

#### minimum\_level

```python
@property
def minimum_level() -> int
```

(int32):  [Read-Write] Minimum zoom level.

Take care when specifying this that the number of tiles at the minimum
level is small, such as four or less. A larger number is likely to
result in rendering problems.

<a id="unreal.CesiumWebMapServiceRasterOverlay.minimum_level"></a>

#### minimum\_level

```python
@minimum_level.setter
def minimum_level(value: int) -> None
```

<a id="unreal.CesiumWebMapServiceRasterOverlay.maximum_level"></a>

#### maximum\_level

```python
@property
def maximum_level() -> int
```

(int32):  [Read-Write] Maximum zoom level.

<a id="unreal.CesiumWebMapServiceRasterOverlay.maximum_level"></a>

#### maximum\_level

```python
@maximum_level.setter
def maximum_level(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay"></a>