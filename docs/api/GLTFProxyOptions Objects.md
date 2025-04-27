## GLTFProxyOptions Objects

```python
class GLTFProxyOptions(Object)
```

GLTFProxy Options

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFProxyOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_material_inputs`` (bool):  [Read-Write] If enabled, a material input may be baked out to a texture (using a simple quad). Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).
- ``default_input_bake_settings`` (Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific default bake settings that override the general defaults above.
- ``default_material_bake_filter`` (TextureFilter):  [Read-Write] Default filtering mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``default_material_bake_size`` (GLTFMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input). Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``default_material_bake_tiling`` (TextureAddress):  [Read-Write] Default addressing mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.
- ``use_thin_translucent_shading_model`` (bool):  [Read-Write] If enabled, materials with shading model thin translucency will be used. Conversion is only partial.

<a id="unreal.GLTFProxyOptions.bake_material_inputs"></a>

#### bake_material_inputs

```python
@property
def bake_material_inputs() -> bool
```

(bool):  [Read-Write] If enabled, a material input may be baked out to a texture (using a simple quad). Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).

<a id="unreal.GLTFProxyOptions.bake_material_inputs"></a>

#### bake_material_inputs

```python
@bake_material_inputs.setter
def bake_material_inputs(value: bool) -> None
```

<a id="unreal.GLTFProxyOptions.use_thin_translucent_shading_model"></a>

#### use_thin_translucent_shading_model

```python
@property
def use_thin_translucent_shading_model() -> bool
```

(bool):  [Read-Write] If enabled, materials with shading model thin translucency will be used. Conversion is only partial.

<a id="unreal.GLTFProxyOptions.use_thin_translucent_shading_model"></a>

#### use_thin_translucent_shading_model

```python
@use_thin_translucent_shading_model.setter
def use_thin_translucent_shading_model(value: bool) -> None
```

<a id="unreal.GLTFProxyOptions.default_material_bake_size"></a>

#### default_material_bake_size

```python
@property
def default_material_bake_size() -> GLTFMaterialBakeSize
```

(GLTFMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input). Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFProxyOptions.default_material_bake_size"></a>

#### default_material_bake_size

```python
@default_material_bake_size.setter
def default_material_bake_size(value: GLTFMaterialBakeSize) -> None
```

<a id="unreal.GLTFProxyOptions.default_material_bake_filter"></a>

#### default_material_bake_filter

```python
@property
def default_material_bake_filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] Default filtering mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFProxyOptions.default_material_bake_filter"></a>

#### default_material_bake_filter

```python
@default_material_bake_filter.setter
def default_material_bake_filter(value: TextureFilter) -> None
```

<a id="unreal.GLTFProxyOptions.default_material_bake_tiling"></a>

#### default_material_bake_tiling

```python
@property
def default_material_bake_tiling() -> TextureAddress
```

(TextureAddress):  [Read-Write] Default addressing mode used when sampling the baked out texture. Can be overridden by material- and input-specific bake settings, see GLTFMaterialExportOptions.

<a id="unreal.GLTFProxyOptions.default_material_bake_tiling"></a>

#### default_material_bake_tiling

```python
@default_material_bake_tiling.setter
def default_material_bake_tiling(value: TextureAddress) -> None
```

<a id="unreal.GLTFProxyOptions.default_input_bake_settings"></a>

#### default_input_bake_settings

```python
@property
def default_input_bake_settings(
) -> Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
```

(Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific default bake settings that override the general defaults above.

<a id="unreal.GLTFProxyOptions.default_input_bake_settings"></a>

#### default_input_bake_settings

```python
@default_input_bake_settings.setter
def default_input_bake_settings(
    value: Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
) -> None
```

<a id="unreal.GLTFProxyOptions.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Reset to Default

<a id="unreal.GLTFMaterialExportOptions"></a>