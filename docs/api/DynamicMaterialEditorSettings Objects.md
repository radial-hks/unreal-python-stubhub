## DynamicMaterialEditorSettings Objects

```python
class DynamicMaterialEditorSettings(DeveloperSettings)
```

Material Designer Settings

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DynamicMaterialEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``content_browser_thumbnail`` (DMContentBrowserThumbnailSettings):  [Read-Write]
- ``custom_effects_folders`` (Array[Name]):  [Read-Write] * Add paths to search for custom effects.
  *
  * Format examples:
  * - /Game/Some/Path
  * - /Plugin/Some/Path
  *
  * The assets must be in a sub-folder of the base path. The sub-folder
  * will be used as the category name.
  *
  * Asset Examples:
  * - /Game/Some/Path/UV/Asset.Asset -> Category: UV
  * - /Plugin/Some/Path/Color/OtherAsset.OtherAsset -> Category: Color
- ``custom_preview_mesh`` (StaticMesh):  [Read-Write]
- ``default_mask`` (Texture):  [Read-Write]
- ``default_slot_value_overrides`` (Map[DMMaterialPropertyType, DMDefaultMaterialPropertySlotValue]):  [Read-Write] Overrides the default values given to slots created in the given material property.
- ``follow_selection`` (bool):  [Read-Write] Changes the currently active material in the designer following actor/object selection.
- ``layout`` (DMMaterialEditorLayout):  [Read-Write]
- ``material_channel_presets`` (Array[DMMaterialChannelListPreset]):  [Read-Write]
- ``preview_images_use_texture_u_vs`` (bool):  [Read-Write]
- ``preview_mesh`` (DMMaterialPreviewMesh):  [Read-Write]
- ``preview_splitter_location`` (float):  [Read-Write] Adjusts the vertical size of the material layer view.
- ``property_preview_size`` (float):  [Read-Write]
- ``show_preview_background`` (bool):  [Read-Write]
- ``splitter_location`` (float):  [Read-Write] Adjusts the vertical size of the material layer view.
- ``stage_preview_size`` (float):  [Read-Write]
- ``thumbnail_size`` (double):  [Read-Write]
- ``use_full_channel_names_in_top_slim_layout`` (bool):  [Read-Write]
- ``use_linear_color_for_vectors`` (bool):  [Read-Write]
- ``uv_visualizer_visible`` (bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.follow_selection"></a>

#### follow_selection

```python
@property
def follow_selection() -> bool
```

(bool):  [Read-Write] Changes the currently active material in the designer following actor/object selection.

<a id="unreal.DynamicMaterialEditorSettings.follow_selection"></a>

#### follow_selection

```python
@follow_selection.setter
def follow_selection(value: bool) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.layout"></a>

#### layout

```python
@property
def layout() -> DMMaterialEditorLayout
```

(DMMaterialEditorLayout):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.layout"></a>

#### layout

```python
@layout.setter
def layout(value: DMMaterialEditorLayout) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.splitter_location"></a>

#### splitter_location

```python
@property
def splitter_location() -> float
```

(float):  [Read-Write] Adjusts the vertical size of the material layer view.

<a id="unreal.DynamicMaterialEditorSettings.splitter_location"></a>

#### splitter_location

```python
@splitter_location.setter
def splitter_location(value: float) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.preview_splitter_location"></a>

#### preview_splitter_location

```python
@property
def preview_splitter_location() -> float
```

(float):  [Read-Write] Adjusts the vertical size of the material layer view.

<a id="unreal.DynamicMaterialEditorSettings.preview_splitter_location"></a>

#### preview_splitter_location

```python
@preview_splitter_location.setter
def preview_splitter_location(value: float) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.uv_visualizer_visible"></a>

#### uv_visualizer_visible

```python
@property
def uv_visualizer_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.uv_visualizer_visible"></a>

#### uv_visualizer_visible

```python
@uv_visualizer_visible.setter
def uv_visualizer_visible(value: bool) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.use_full_channel_names_in_top_slim_layout"></a>

#### use_full_channel_names_in_top_slim_layout

```python
@property
def use_full_channel_names_in_top_slim_layout() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.use_full_channel_names_in_top_slim_layout"></a>

#### use_full_channel_names_in_top_slim_layout

```python
@use_full_channel_names_in_top_slim_layout.setter
def use_full_channel_names_in_top_slim_layout(value: bool) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.stage_preview_size"></a>

#### stage_preview_size

```python
@property
def stage_preview_size() -> float
```

(float):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.stage_preview_size"></a>

#### stage_preview_size

```python
@stage_preview_size.setter
def stage_preview_size(value: float) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.property_preview_size"></a>

#### property_preview_size

```python
@property
def property_preview_size() -> float
```

(float):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.property_preview_size"></a>

#### property_preview_size

```python
@property_preview_size.setter
def property_preview_size(value: float) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.thumbnail_size"></a>

#### thumbnail_size

```python
@property
def thumbnail_size() -> float
```

(double):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.thumbnail_size"></a>

#### thumbnail_size

```python
@thumbnail_size.setter
def thumbnail_size(value: float) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.preview_mesh"></a>

#### preview_mesh

```python
@property
def preview_mesh() -> DMMaterialPreviewMesh
```

(DMMaterialPreviewMesh):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.preview_mesh"></a>

#### preview_mesh

```python
@preview_mesh.setter
def preview_mesh(value: DMMaterialPreviewMesh) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.custom_preview_mesh"></a>

#### custom_preview_mesh

```python
@property
def custom_preview_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.custom_preview_mesh"></a>

#### custom_preview_mesh

```python
@custom_preview_mesh.setter
def custom_preview_mesh(value: StaticMesh) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.show_preview_background"></a>

#### show_preview_background

```python
@property
def show_preview_background() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.show_preview_background"></a>

#### show_preview_background

```python
@show_preview_background.setter
def show_preview_background(value: bool) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.preview_images_use_texture_u_vs"></a>

#### preview_images_use_texture_u_vs

```python
@property
def preview_images_use_texture_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.preview_images_use_texture_u_vs"></a>

#### preview_images_use_texture_u_vs

```python
@preview_images_use_texture_u_vs.setter
def preview_images_use_texture_u_vs(value: bool) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.default_mask"></a>

#### default_mask

```python
@property
def default_mask() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.default_mask"></a>

#### default_mask

```python
@default_mask.setter
def default_mask(value: Texture) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.default_slot_value_overrides"></a>

#### default_slot_value_overrides

```python
@property
def default_slot_value_overrides(
) -> Map[DMMaterialPropertyType, DMDefaultMaterialPropertySlotValue]
```

(Map[DMMaterialPropertyType, DMDefaultMaterialPropertySlotValue]):  [Read-Write] Overrides the default values given to slots created in the given material property.

<a id="unreal.DynamicMaterialEditorSettings.default_slot_value_overrides"></a>

#### default_slot_value_overrides

```python
@default_slot_value_overrides.setter
def default_slot_value_overrides(
    value: Map[DMMaterialPropertyType, DMDefaultMaterialPropertySlotValue]
) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.custom_effects_folders"></a>

#### custom_effects_folders

```python
@property
def custom_effects_folders() -> Array[Name]
```

(Array[Name]):  [Read-Write] * Add paths to search for custom effects.
*
* Format examples:
* - /Game/Some/Path
* - /Plugin/Some/Path
*
* The assets must be in a sub-folder of the base path. The sub-folder
* will be used as the category name.
*
* Asset Examples:
* - /Game/Some/Path/UV/Asset.Asset -> Category: UV
* - /Plugin/Some/Path/Color/OtherAsset.OtherAsset -> Category: Color

<a id="unreal.DynamicMaterialEditorSettings.custom_effects_folders"></a>

#### custom_effects_folders

```python
@custom_effects_folders.setter
def custom_effects_folders(value: Array[Name]) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.material_channel_presets"></a>

#### material_channel_presets

```python
@property
def material_channel_presets() -> Array[DMMaterialChannelListPreset]
```

(Array[DMMaterialChannelListPreset]):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.material_channel_presets"></a>

#### material_channel_presets

```python
@material_channel_presets.setter
def material_channel_presets(
        value: Array[DMMaterialChannelListPreset]) -> None
```

<a id="unreal.DynamicMaterialEditorSettings.use_linear_color_for_vectors"></a>

#### use_linear_color_for_vectors

```python
@property
def use_linear_color_for_vectors() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DynamicMaterialEditorSettings.use_linear_color_for_vectors"></a>

#### use_linear_color_for_vectors

```python
@use_linear_color_for_vectors.setter
def use_linear_color_for_vectors(value: bool) -> None
```

<a id="unreal.DynamicMaterialInstanceFactory"></a>