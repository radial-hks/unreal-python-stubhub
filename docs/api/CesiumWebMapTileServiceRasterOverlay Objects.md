## CesiumWebMapTileServiceRasterOverlay Objects

```python
class CesiumWebMapTileServiceRasterOverlay(CesiumRasterOverlay)
```

A raster overlay that directly accesses a Web Map Tile Service (WMTS) server.
If you're using a Web Map Tile Service via Cesium ion, use the "Cesium ion
Raster Overlay" component instead.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumWebMapTileServiceRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``base_url`` (str):  [Read-Write] The base URL of the Web Map Tile Service (WMTS).
  This URL should not include query parameters. For example:
  https://tile.openstreetmap.org/{TileMatrix}/{TileCol}/{TileRow}.png
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``format`` (str):  [Read-Write] The MIME type for images to retrieve from the server.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``layer`` (str):  [Read-Write] The layer name for WMTS requests.
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
  level is small, such as four or less. A larger number is likely to result
  in rendering problems.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``projection`` (CesiumWebMapTileServiceRasterOverlayProjection):  [Read-Write] The type of projection used to project the WMTS imagery onto the globe.
  For instance, EPSG:4326 uses geographic projection and EPSG:3857 uses Web
  Mercator.
- ``rectangle_east`` (double):  [Read-Write] The east boundary of the bounding rectangle used for the quadtree tiling
  scheme. Specified in longitude degrees in the range [-180, 180].

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``rectangle_north`` (double):  [Read-Write] The north boundary of the bounding rectangle used for the quadtree tiling
  scheme. Specified in latitude degrees in the range [-90, 90].

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``rectangle_south`` (double):  [Read-Write] The south boundary of the bounding rectangle used for the quadtree tiling
  scheme. Specified in latitude degrees in the range [-90, 90].

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``rectangle_west`` (double):  [Read-Write] The west boundary of the bounding rectangle used for the quadtree tiling
  scheme. Specified in longitude degrees in the range [-180, 180].

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``renderer_options`` (RasterOverlayRendererOptions):  [Read-Write] Sets the texture filter and texture group of raster tile images. Depending
  on the project settings, the default texture filter, TF_Default, should
  have the best quality.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``root_tiles_x`` (int32):  [Read-Write] The number of tiles corresponding to TileCol, also known as
  TileMatrixWidth. If specified, this determines the number of tiles at the
  root of the quadtree tiling scheme in the X direction.

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``root_tiles_y`` (int32):  [Read-Write] The number of tiles corresponding to TileRow, also known as
  TileMatrixHeight. If specified, this determines the number of tiles at the
  root of the quadtree tiling scheme in the Y direction.

  Only applicable if "Specify Tiling Scheme" is set to true.
- ``show_credits_on_screen`` (bool):  [Read-Write] Whether or not to show credits of this raster overlay on screen.
- ``specify_tile_matrix_set_labels`` (bool):  [Read-Write] Set this to true to specify tile matrix set labels manually. If false, the
  labels will be constructed from the specified levels and prefix (if one is
  specified).
- ``specify_tiling_scheme`` (bool):  [Read-Write] Set this to true to specify the quadtree tiling scheme according to the
  specified root tile numbers and projected bounding rectangle. If false, the
  tiling scheme will be deduced from the projection.
- ``specify_zoom_levels`` (bool):  [Read-Write] Set this to true to directly specify the minimum and maximum zoom levels
  available from the server. If false, the minimum and maximum zoom levels
  will be retrieved from the server's tilemapresource.xml file.
- ``style`` (str):  [Read-Write] The style name for WMTS requests.
- ``sub_tile_cache_bytes`` (int64):  [Read-Write] The maximum number of bytes to use to cache sub-tiles in memory.

  This is used by provider types that have an underlying tiling scheme that
  may not align with the tiling scheme of the geometry tiles on which the
  raster overlay tiles are draped. Because a single sub-tile may overlap
  multiple geometry tiles, it is useful to cache loaded sub-tiles in memory
  in case they're needed again soon. This property controls the maximum size
  of that cache.
- ``tile_height`` (int32):  [Read-Write] The pixel height of the image tiles.
- ``tile_matrix_set_id`` (str):  [Read-Write] The tile matrix set identifier for WMTS requests.
- ``tile_matrix_set_label_prefix`` (str):  [Read-Write] The prefix to use for the tile matrix set labels. For instance, setting
  "EPSG:4326:" as prefix generates label list ["EPSG:4326:0", "EPSG:4326:1",
  "EPSG:4326:2", ...]
  Only applicable when "Specify Tile Matrix Set Labels" is false.
- ``tile_matrix_set_labels`` (Array[str]):  [Read-Write] The manually specified tile matrix set labels.

  Only applicable when "Specify Tile Matrix Set Labels" is true.
- ``tile_width`` (int32):  [Read-Write] The pixel width of the image tiles.
- ``use_web_mercator_projection`` (bool):  [Read-Write]
  deprecated: Use Projection instead.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.base_url"></a>

#### base\_url

```python
@property
def base_url() -> str
```

(str):  [Read-Write] The base URL of the Web Map Tile Service (WMTS).
This URL should not include query parameters. For example:
https://tile.openstreetmap.org/{TileMatrix}/{TileCol}/{TileRow}.png

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.base_url"></a>

#### base\_url

```python
@base_url.setter
def base_url(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.url"></a>

#### url

```python
@property
def url() -> str
```

deprecated: 'url' was renamed to 'base_url'.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.layer"></a>

#### layer

```python
@property
def layer() -> str
```

(str):  [Read-Write] The layer name for WMTS requests.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.layer"></a>

#### layer

```python
@layer.setter
def layer(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.style"></a>

#### style

```python
@property
def style() -> str
```

(str):  [Read-Write] The style name for WMTS requests.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.style"></a>

#### style

```python
@style.setter
def style(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.format"></a>

#### format

```python
@property
def format() -> str
```

(str):  [Read-Write] The MIME type for images to retrieve from the server.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.format"></a>

#### format

```python
@format.setter
def format(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_id"></a>

#### tile\_matrix\_set\_id

```python
@property
def tile_matrix_set_id() -> str
```

(str):  [Read-Write] The tile matrix set identifier for WMTS requests.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_id"></a>

#### tile\_matrix\_set\_id

```python
@tile_matrix_set_id.setter
def tile_matrix_set_id(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_label_prefix"></a>

#### tile\_matrix\_set\_label\_prefix

```python
@property
def tile_matrix_set_label_prefix() -> str
```

(str):  [Read-Write] The prefix to use for the tile matrix set labels. For instance, setting
"EPSG:4326:" as prefix generates label list ["EPSG:4326:0", "EPSG:4326:1",
"EPSG:4326:2", ...]
Only applicable when "Specify Tile Matrix Set Labels" is false.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_label_prefix"></a>

#### tile\_matrix\_set\_label\_prefix

```python
@tile_matrix_set_label_prefix.setter
def tile_matrix_set_label_prefix(value: str) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_tile_matrix_set_labels"></a>

#### specify\_tile\_matrix\_set\_labels

```python
@property
def specify_tile_matrix_set_labels() -> bool
```

(bool):  [Read-Write] Set this to true to specify tile matrix set labels manually. If false, the
labels will be constructed from the specified levels and prefix (if one is
specified).

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_tile_matrix_set_labels"></a>

#### specify\_tile\_matrix\_set\_labels

```python
@specify_tile_matrix_set_labels.setter
def specify_tile_matrix_set_labels(value: bool) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_labels"></a>

#### tile\_matrix\_set\_labels

```python
@property
def tile_matrix_set_labels() -> Array[str]
```

(Array[str]):  [Read-Write] The manually specified tile matrix set labels.

Only applicable when "Specify Tile Matrix Set Labels" is true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_matrix_set_labels"></a>

#### tile\_matrix\_set\_labels

```python
@tile_matrix_set_labels.setter
def tile_matrix_set_labels(value: Array[str]) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.use_web_mercator_projection"></a>

#### use\_web\_mercator\_projection

```python
@property
def use_web_mercator_projection() -> bool
```

(bool):  [Read-Write]
deprecated: Use Projection instead.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.use_web_mercator_projection"></a>

#### use\_web\_mercator\_projection

```python
@use_web_mercator_projection.setter
def use_web_mercator_projection(value: bool) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.projection"></a>

#### projection

```python
@property
def projection() -> CesiumWebMapTileServiceRasterOverlayProjection
```

(CesiumWebMapTileServiceRasterOverlayProjection):  [Read-Write] The type of projection used to project the WMTS imagery onto the globe.
For instance, EPSG:4326 uses geographic projection and EPSG:3857 uses Web
Mercator.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.projection"></a>

#### projection

```python
@projection.setter
def projection(value: CesiumWebMapTileServiceRasterOverlayProjection) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_tiling_scheme"></a>

#### specify\_tiling\_scheme

```python
@property
def specify_tiling_scheme() -> bool
```

(bool):  [Read-Write] Set this to true to specify the quadtree tiling scheme according to the
specified root tile numbers and projected bounding rectangle. If false, the
tiling scheme will be deduced from the projection.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_tiling_scheme"></a>

#### specify\_tiling\_scheme

```python
@specify_tiling_scheme.setter
def specify_tiling_scheme(value: bool) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.root_tiles_x"></a>

#### root\_tiles\_x

```python
@property
def root_tiles_x() -> int
```

(int32):  [Read-Write] The number of tiles corresponding to TileCol, also known as
TileMatrixWidth. If specified, this determines the number of tiles at the
root of the quadtree tiling scheme in the X direction.

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.root_tiles_x"></a>

#### root\_tiles\_x

```python
@root_tiles_x.setter
def root_tiles_x(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.root_tiles_y"></a>

#### root\_tiles\_y

```python
@property
def root_tiles_y() -> int
```

(int32):  [Read-Write] The number of tiles corresponding to TileRow, also known as
TileMatrixHeight. If specified, this determines the number of tiles at the
root of the quadtree tiling scheme in the Y direction.

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.root_tiles_y"></a>

#### root\_tiles\_y

```python
@root_tiles_y.setter
def root_tiles_y(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_west"></a>

#### rectangle\_west

```python
@property
def rectangle_west() -> float
```

(double):  [Read-Write] The west boundary of the bounding rectangle used for the quadtree tiling
scheme. Specified in longitude degrees in the range [-180, 180].

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_west"></a>

#### rectangle\_west

```python
@rectangle_west.setter
def rectangle_west(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.west"></a>

#### west

```python
@property
def west() -> float
```

deprecated: 'west' was renamed to 'rectangle_west'.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.west"></a>

#### west

```python
@west.setter
def west(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_south"></a>

#### rectangle\_south

```python
@property
def rectangle_south() -> float
```

(double):  [Read-Write] The south boundary of the bounding rectangle used for the quadtree tiling
scheme. Specified in latitude degrees in the range [-90, 90].

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_south"></a>

#### rectangle\_south

```python
@rectangle_south.setter
def rectangle_south(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.south"></a>

#### south

```python
@property
def south() -> float
```

deprecated: 'south' was renamed to 'rectangle_south'.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.south"></a>

#### south

```python
@south.setter
def south(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_east"></a>

#### rectangle\_east

```python
@property
def rectangle_east() -> float
```

(double):  [Read-Write] The east boundary of the bounding rectangle used for the quadtree tiling
scheme. Specified in longitude degrees in the range [-180, 180].

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_east"></a>

#### rectangle\_east

```python
@rectangle_east.setter
def rectangle_east(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.east"></a>

#### east

```python
@property
def east() -> float
```

deprecated: 'east' was renamed to 'rectangle_east'.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.east"></a>

#### east

```python
@east.setter
def east(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_north"></a>

#### rectangle\_north

```python
@property
def rectangle_north() -> float
```

(double):  [Read-Write] The north boundary of the bounding rectangle used for the quadtree tiling
scheme. Specified in latitude degrees in the range [-90, 90].

Only applicable if "Specify Tiling Scheme" is set to true.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.rectangle_north"></a>

#### rectangle\_north

```python
@rectangle_north.setter
def rectangle_north(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.north"></a>

#### north

```python
@property
def north() -> float
```

deprecated: 'north' was renamed to 'rectangle_north'.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.north"></a>

#### north

```python
@north.setter
def north(value: float) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_zoom_levels"></a>

#### specify\_zoom\_levels

```python
@property
def specify_zoom_levels() -> bool
```

(bool):  [Read-Write] Set this to true to directly specify the minimum and maximum zoom levels
available from the server. If false, the minimum and maximum zoom levels
will be retrieved from the server's tilemapresource.xml file.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.specify_zoom_levels"></a>

#### specify\_zoom\_levels

```python
@specify_zoom_levels.setter
def specify_zoom_levels(value: bool) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.minimum_level"></a>

#### minimum\_level

```python
@property
def minimum_level() -> int
```

(int32):  [Read-Write] Minimum zoom level.

Take care when specifying this that the number of tiles at the minimum
level is small, such as four or less. A larger number is likely to result
in rendering problems.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.minimum_level"></a>

#### minimum\_level

```python
@minimum_level.setter
def minimum_level(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.maximum_level"></a>

#### maximum\_level

```python
@property
def maximum_level() -> int
```

(int32):  [Read-Write] Maximum zoom level.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.maximum_level"></a>

#### maximum\_level

```python
@maximum_level.setter
def maximum_level(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_width"></a>

#### tile\_width

```python
@property
def tile_width() -> int
```

(int32):  [Read-Write] The pixel width of the image tiles.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_width"></a>

#### tile\_width

```python
@tile_width.setter
def tile_width(value: int) -> None
```

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_height"></a>

#### tile\_height

```python
@property
def tile_height() -> int
```

(int32):  [Read-Write] The pixel height of the image tiles.

<a id="unreal.CesiumWebMapTileServiceRasterOverlay.tile_height"></a>

#### tile\_height

```python
@tile_height.setter
def tile_height(value: int) -> None
```

<a id="unreal.CesiumWgs84Ellipsoid"></a>