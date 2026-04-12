## CesiumIonRasterOverlay Objects

```python
class CesiumIonRasterOverlay(CesiumRasterOverlay)
```

A raster overlay that uses an IMAGERY asset from Cesium ion.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumIonRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cesium_ion_server`` (CesiumIonServer):  [Read-Write] The Cesium ion Server from which this raster overlay is loaded.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``ion_access_token`` (str):  [Read-Write] The access token to use to access the Cesium ion resource.
- ``ion_asset_endpoint_url`` (str):  [Read-Write] The URL of the ion asset endpoint. Defaults to Cesium ion but a custom
  endpoint can be specified.
  deprecated: Use CesiumIonServer instead.
- ``ion_asset_id`` (int64):  [Read-Write] The ID of the Cesium ion asset to use.

  If this property is non-zero, the Bing Maps Key and Map Style properties
  are ignored.
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

<a id="unreal.CesiumIonRasterOverlay.ion_asset_id"></a>

#### ion\_asset\_id

```python
@property
def ion_asset_id() -> int
```

(int64):  [Read-Write] The ID of the Cesium ion asset to use.

If this property is non-zero, the Bing Maps Key and Map Style properties
are ignored.

<a id="unreal.CesiumIonRasterOverlay.ion_asset_id"></a>

#### ion\_asset\_id

```python
@ion_asset_id.setter
def ion_asset_id(value: int) -> None
```

<a id="unreal.CesiumIonRasterOverlay.ion_access_token"></a>

#### ion\_access\_token

```python
@property
def ion_access_token() -> str
```

(str):  [Read-Write] The access token to use to access the Cesium ion resource.

<a id="unreal.CesiumIonRasterOverlay.ion_access_token"></a>

#### ion\_access\_token

```python
@ion_access_token.setter
def ion_access_token(value: str) -> None
```

<a id="unreal.CesiumIonRasterOverlay.ion_asset_endpoint_url"></a>

#### ion\_asset\_endpoint\_url

```python
@property
def ion_asset_endpoint_url() -> str
```

(str):  [Read-Write] The URL of the ion asset endpoint. Defaults to Cesium ion but a custom
endpoint can be specified.
deprecated: Use CesiumIonServer instead.

<a id="unreal.CesiumIonRasterOverlay.ion_asset_endpoint_url"></a>

#### ion\_asset\_endpoint\_url

```python
@ion_asset_endpoint_url.setter
def ion_asset_endpoint_url(value: str) -> None
```

<a id="unreal.CesiumIonRasterOverlay.cesium_ion_server"></a>

#### cesium\_ion\_server

```python
@property
def cesium_ion_server() -> CesiumIonServer
```

(CesiumIonServer):  [Read-Write] The Cesium ion Server from which this raster overlay is loaded.

<a id="unreal.CesiumIonRasterOverlay.cesium_ion_server"></a>

#### cesium\_ion\_server

```python
@cesium_ion_server.setter
def cesium_ion_server(value: CesiumIonServer) -> None
```

<a id="unreal.CesiumMetadataPickingBlueprintLibrary"></a>