## TrueTypeFontFactory Objects

```python
class TrueTypeFontFactory(TextureFactory)
```

True Type Font Factory

**C++ Source:**

- **Module**: UnrealEd
- **File**: TrueTypeFontFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_coverage_thresholds`` (Vector4):  [Read-Write] Channel values to compare to when preserving alpha coverage from a mask for mips
- ``alpha_to_emissive`` (bool):  [Read-Write] If enabled, link the texture's alpha to the created material's emissive color
- ``alpha_to_opacity`` (bool):  [Read-Write] If enabled, link the texture's alpha to the created material's opacity
- ``alpha_to_opacity_mask`` (bool):  [Read-Write] If enabled, link the texture's alpha to the created material's opacity mask
- ``alpha_to_roughness`` (bool):  [Read-Write] If enabled, link the texture's alpha to the created material's roughness
- ``asset_import_task`` (AssetImportTask):  [Read-Write] Task for importing file via script interfaces
- ``automated_import_data`` (AutomatedAssetImportData):  [Read-Write] Data for how to import files via the automated command line importing interface
- ``blending`` (BlendMode):  [Read-Write] The blend mode of the created material
- ``compression_settings`` (TextureCompressionSettings):  [Read-Write] Compression settings for the texture
- ``context_class`` (type(Class)):  [Read-Write] Class of the context object used to help create the object.
- ``create_material`` (bool):  [Read-Write] If enabled, a material will automatically be created for the texture
- ``create_new`` (bool):  [Read-Write] The default value to return from CanCreateNew()
- ``defer_compression`` (bool):  [Read-Write] If enabled, compression is deferred until the texture is saved
- ``do_scale_mips_for_alpha_coverage`` (bool):  [Read-Write] Whether mip RGBA should be scaled to preserve the number of pixels with Value >= AlphaCoverageThresholds
- ``edit_after_new`` (bool):  [Read-Write] true if the associated editor should be opened after creating a new object.
- ``editor_import`` (bool):  [Read-Write] true if the factory imports objects from files.
- ``flip_normal_map_green_channel`` (bool):  [Read-Write] If enabled, the texture's green channel will be inverted. This is useful for some normal maps
- ``formats`` (Array[str]):  [Read-Write] List of formats supported by the factory. Each entry is of the form "ext;Description" where ext is the file extension.
- ``import_options`` (FontImportOptions):  [Read-Write] Import options for the font
- ``lod_group`` (TextureGroup):  [Read-Write] The group the texture belongs to
- ``mip_gen_settings`` (TextureMipGenSettings):  [Read-Write] The mip-map generation settings for the texture; Allows customization of the content of the mip-map chain
- ``no_alpha`` (bool):  [Read-Write] If enabled, the texture's alpha channel will be discarded during compression
- ``preserve_border`` (bool):  [Read-Write] If enabled, preserve the value of border pixels when creating mip-maps
- ``rgb_to_base_color`` (bool):  [Read-Write] If enabled, link the texture to the created material's base color
- ``rgb_to_emissive`` (bool):  [Read-Write] If enabled, link the texture to the created material's emissive color
- ``shading_model`` (MaterialShadingModel):  [Read-Write] The shading model of the created material
- ``supported_class`` (type(Class)):  [Read-Write] The class manufactured by this factory.
- ``text`` (bool):  [Read-Write] true if the factory imports objects from text.
- ``two_sided`` (bool):  [Read-Write] If enabled, the created material will be two-sided
- ``use_new_mip_filter`` (bool):  [Read-Write] Whether to use newer & faster mip generation filter

<a id="unreal.UnrealEditorSubsystem"></a>