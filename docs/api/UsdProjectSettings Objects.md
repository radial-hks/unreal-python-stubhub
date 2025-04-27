## UsdProjectSettings Objects

```python
class UsdProjectSettings(DeveloperSettings)
```

USDCore and defaultconfig here so this ends up at DefaultUSDCore.ini in the editor, and is sent to the
packaged game as well

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDProjectSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_material_purposes`` (Array[Name]):  [Read-Write] Material purposes to show on drop-downs in addition to the standard "preview" and "full"
- ``additional_plugin_directories`` (Array[DirectoryPath]):  [Read-Write] Additional paths to check for USD plugins.

  If you want the USD plugins to be included in a packaged game, you must use a relative
  path to a location within your project directory, and you must also add that same path
  to the "Additional Non-Asset Directories To Copy" Project Packaging setting.

  For example, this relative path could be used to locate USD plugins in a directory at
  the root of your project:
      ../USD_Plugins

  The packaging process cannot use an absolute path and will raise an error if given one
  when it tries to concatenate the game content directory path with an absolute path.
- ``default_asset_cache`` (SoftObjectPath):  [Read-Write] USD Asset Cache to use for USD Stage Actors that don't have any asset cache specified.
  Leave this empty to have each stage actor generate it's on transient cache instead.
- ``default_resolver_search_path`` (Array[DirectoryPath]):  [Read-Write] The directories that will be used as the default search path by USD's default resolver
  during asset resolution.

  Each directory in the search path should be an absolute path. If it is not, it will be
  anchored to the current working directory.

  Note that the default search path must be set before the first invocation of USD's
  resolver system, so changing this setting will require a restart of the engine in order
  for the new setting to take effect.
- ``default_sound_attenuation`` (SoftObjectPath):  [Read-Write] Note that the below properties being FSoftObjectPath ensure that these assets are cooked into packaged games
- ``edit_in_instanceable_behavior`` (UsdEditInInstanceBehavior):  [Read-Write] Whether to show the warning dialog when authoring opinions inside an instance or instance proxy
- ``log_usd_sdk_errors`` (bool):  [Read-Write] Whether to show on the output log messages, warnings and errors reported directly by the USD SDK
- ``reference_default_svt_material`` (SoftObjectPath):  [Read-Write] Material to use when handling .vdb files as Sparse Volume Textures. An instance of this material will be
  added to the AHeterogeneousVolume, and will use the parsed SparseVolumeTexture as a texture parameter.
  Note that alternatively Volume prims can have material bindings to Unreal materials, and the importer
  will prioritize trying to use those as the volumetric materials for the Sparse Volume Textures instead.
- ``reference_display_color_and_opacity_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_display_color_and_opacity_two_sided_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_display_color_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_display_color_two_sided_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_model_card_texture_material`` (SoftObjectPath):  [Read-Write] What material to use for UUsdDrawModeComponents with "Cards" draw mode and provided textures (corresponding to
  UsdGeomModelAPI with the "cards" drawMode).
  Each face of the card geometry will use a separate texture material instance, and the UTexture2D will be set
  as a material parameter named "Texture".
  You can swap this with your own material, but make sure the replacement material has a "Texture" parameter
- ``reference_preview_surface_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_translucent_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_translucent_two_sided_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_translucent_two_sided_vt_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_translucent_vt_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_two_sided_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_two_sided_vt_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``reference_preview_surface_vt_material`` (SoftObjectPath):  [Read-Write] What material to use as reference material when creating material instances from USD materials.
  You can swap these with your own materials, but make sure that the replacement materials have parameters with
  the same names and types as the ones provided by the default material, otherwise the instances will not have
  the parameters filled with values extracted from the USD material when parsing.
- ``show_confirmation_when_clearing_layers`` (bool):  [Read-Write]
- ``show_confirmation_when_muting_dirty_layers`` (bool):  [Read-Write]
- ``show_confirmation_when_reloading_dirty_layers`` (bool):  [Read-Write]
- ``show_create_default_asset_cache_dialog`` (bool):  [Read-Write]
- ``show_inherited_visibility_warning`` (bool):  [Read-Write] Whether to show the warning dialog when authoring new visibility tracks from Unreal
- ``show_overridden_opinions_warning`` (bool):  [Read-Write] Whether to show the warning dialog when authoring opinions that could have no effect on the composed stage
- ``show_save_layers_dialog_when_closing`` (UsdSaveDialogBehavior):  [Read-Write] Whether to display the pop up dialog asking what to do about dirty USD layers when closing USD stages
- ``show_save_layers_dialog_when_saving`` (UsdSaveDialogBehavior):  [Read-Write] Whether to display the pop up dialog asking what to do about dirty USD layers when saving the UE level
- ``show_transform_on_camera_component_warning`` (bool):  [Read-Write] Whether to show the warning dialog when authoring a transforms directly to a camera component
- ``show_transform_track_on_camera_component_warning`` (bool):  [Read-Write] Whether to show the warning dialog when authoring a transform track directly to a camera component
- ``show_warning_on_incomplete_duplication`` (bool):  [Read-Write] Whether to show a warning whenever the "Duplicate All Local Layer Specs" option is picked, and the duplicated
  prim has some specs outside the local layer stack that will not be duplicated.

<a id="unreal.UsdReferenceOptions"></a>