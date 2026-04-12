## glTFRuntimeMaterialsConfig Objects

```python
class glTFRuntimeMaterialsConfig(StructBase)
```

Gl TFRuntime Materials Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_mode`` (EglTFRuntimeCacheMode):  [Read-Write]
- ``custom_scalar_params`` (Map[str, float]):  [Read-Write]
- ``custom_texture_params`` (Map[str, Texture]):  [Read-Write]
- ``custom_vector_params`` (Map[str, LinearColor]):  [Read-Write]
- ``disable_vertex_colors`` (bool):  [Read-Write]
- ``force_material`` (MaterialInterface):  [Read-Write]
- ``generates_mip_maps`` (bool):  [Read-Write]
- ``images_config`` (glTFRuntimeImagesConfig):  [Read-Write]
- ``images_override_map`` (Map[int32, Texture2D]):  [Read-Write]
- ``lines_base_material`` (MaterialInterface):  [Read-Write]
- ``lines_scale_factor`` (float):  [Read-Write]
- ``lines_triangulation_mode`` (EglTFRuntimeLinesTriangulationMode):  [Read-Write]
- ``load_mip_maps`` (bool):  [Read-Write]
- ``materials_override_by_name_map`` (Map[str, MaterialInterface]):  [Read-Write]
- ``materials_override_map`` (Map[int32, MaterialInterface]):  [Read-Write]
- ``materials_override_map_inject_params`` (bool):  [Read-Write]
- ``merge_sections_by_material`` (bool):  [Read-Write]
- ``params_multiplier`` (Map[str, float]):  [Read-Write]
- ``points_base_material`` (MaterialInterface):  [Read-Write]
- ``points_scale_factor`` (float):  [Read-Write]
- ``points_triangulation_mode`` (EglTFRuntimePointsTriangulationMode):  [Read-Write]
- ``scalar_params_overrides`` (Map[str, float]):  [Read-Write]
- ``skip_lines`` (bool):  [Read-Write]
- ``skip_load`` (bool):  [Read-Write]
- ``skip_points`` (bool):  [Read-Write]
- ``specular_factor`` (float):  [Read-Write]
- ``textures_override_map`` (Map[int32, Texture2D]):  [Read-Write]
- ``uber_materials_override_map`` (Map[EglTFRuntimeMaterialType, MaterialInterface]):  [Read-Write]
- ``variant`` (str):  [Read-Write]
- ``vertex_color_only_material`` (MaterialInterface):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE,
        uber_materials_override_map: Map[EglTFRuntimeMaterialType,
                                         MaterialInterface] = {},
        materials_override_map: Map[int, MaterialInterface] = {},
        materials_override_by_name_map: Map[str, MaterialInterface] = {},
        textures_override_map: Map[int, Texture2D] = {},
        images_override_map: Map[int, Texture2D] = {},
        disable_vertex_colors: bool = False,
        generates_mip_maps: bool = False,
        merge_sections_by_material: bool = False,
        specular_factor: float = 0.000000,
        materials_override_map_inject_params: bool = False,
        params_multiplier: Map[str, float] = {},
        images_config: glTFRuntimeImagesConfig = [
            TextureCompressionSettings.TC_DEFAULT,
            TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False,
            False, 0
        ],
        variant: str = "",
        skip_load: bool = False,
        vertex_color_only_material: MaterialInterface = None,
        scalar_params_overrides: Map[str, float] = {},
        load_mip_maps: bool = False,
        force_material: MaterialInterface = None,
        skip_points: bool = False,
        points_triangulation_mode:
    EglTFRuntimePointsTriangulationMode = EglTFRuntimePointsTriangulationMode.
    TRIANGLE,
        points_base_material: MaterialInterface = None,
        points_scale_factor: float = 0.000000,
        skip_lines: bool = False,
        lines_triangulation_mode:
    EglTFRuntimeLinesTriangulationMode = EglTFRuntimeLinesTriangulationMode.
    RECTANGLE,
        lines_base_material: MaterialInterface = None,
        lines_scale_factor: float = 0.000000,
        custom_scalar_params: Map[str, float] = {},
        custom_vector_params: Map[str, LinearColor] = {},
        custom_texture_params: Map[str, Texture] = {}) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.cache_mode"></a>

#### cache\_mode

```python
@property
def cache_mode() -> EglTFRuntimeCacheMode
```

(EglTFRuntimeCacheMode):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.cache_mode"></a>

#### cache\_mode

```python
@cache_mode.setter
def cache_mode(value: EglTFRuntimeCacheMode) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.uber_materials_override_map"></a>

#### uber\_materials\_override\_map

```python
@property
def uber_materials_override_map(
) -> Map[EglTFRuntimeMaterialType, MaterialInterface]
```

(Map[EglTFRuntimeMaterialType, MaterialInterface]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.uber_materials_override_map"></a>

#### uber\_materials\_override\_map

```python
@uber_materials_override_map.setter
def uber_materials_override_map(
        value: Map[EglTFRuntimeMaterialType, MaterialInterface]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_map"></a>

#### materials\_override\_map

```python
@property
def materials_override_map() -> Map[int, MaterialInterface]
```

(Map[int32, MaterialInterface]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_map"></a>

#### materials\_override\_map

```python
@materials_override_map.setter
def materials_override_map(value: Map[int, MaterialInterface]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_by_name_map"></a>

#### materials\_override\_by\_name\_map

```python
@property
def materials_override_by_name_map() -> Map[str, MaterialInterface]
```

(Map[str, MaterialInterface]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_by_name_map"></a>

#### materials\_override\_by\_name\_map

```python
@materials_override_by_name_map.setter
def materials_override_by_name_map(value: Map[str, MaterialInterface]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.textures_override_map"></a>

#### textures\_override\_map

```python
@property
def textures_override_map() -> Map[int, Texture2D]
```

(Map[int32, Texture2D]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.textures_override_map"></a>

#### textures\_override\_map

```python
@textures_override_map.setter
def textures_override_map(value: Map[int, Texture2D]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.images_override_map"></a>

#### images\_override\_map

```python
@property
def images_override_map() -> Map[int, Texture2D]
```

(Map[int32, Texture2D]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.images_override_map"></a>

#### images\_override\_map

```python
@images_override_map.setter
def images_override_map(value: Map[int, Texture2D]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.disable_vertex_colors"></a>

#### disable\_vertex\_colors

```python
@property
def disable_vertex_colors() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.disable_vertex_colors"></a>

#### disable\_vertex\_colors

```python
@disable_vertex_colors.setter
def disable_vertex_colors(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.generates_mip_maps"></a>

#### generates\_mip\_maps

```python
@property
def generates_mip_maps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.generates_mip_maps"></a>

#### generates\_mip\_maps

```python
@generates_mip_maps.setter
def generates_mip_maps(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.merge_sections_by_material"></a>

#### merge\_sections\_by\_material

```python
@property
def merge_sections_by_material() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.merge_sections_by_material"></a>

#### merge\_sections\_by\_material

```python
@merge_sections_by_material.setter
def merge_sections_by_material(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.specular_factor"></a>

#### specular\_factor

```python
@property
def specular_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.specular_factor"></a>

#### specular\_factor

```python
@specular_factor.setter
def specular_factor(value: float) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_map_inject_params"></a>

#### materials\_override\_map\_inject\_params

```python
@property
def materials_override_map_inject_params() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.materials_override_map_inject_params"></a>

#### materials\_override\_map\_inject\_params

```python
@materials_override_map_inject_params.setter
def materials_override_map_inject_params(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.params_multiplier"></a>

#### params\_multiplier

```python
@property
def params_multiplier() -> Map[str, float]
```

(Map[str, float]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.params_multiplier"></a>

#### params\_multiplier

```python
@params_multiplier.setter
def params_multiplier(value: Map[str, float]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.images_config"></a>

#### images\_config

```python
@property
def images_config() -> glTFRuntimeImagesConfig
```

(glTFRuntimeImagesConfig):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.images_config"></a>

#### images\_config

```python
@images_config.setter
def images_config(value: glTFRuntimeImagesConfig) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.variant"></a>

#### variant

```python
@property
def variant() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.variant"></a>

#### variant

```python
@variant.setter
def variant(value: str) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.skip_load"></a>

#### skip\_load

```python
@property
def skip_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.skip_load"></a>

#### skip\_load

```python
@skip_load.setter
def skip_load(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.vertex_color_only_material"></a>

#### vertex\_color\_only\_material

```python
@property
def vertex_color_only_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.vertex_color_only_material"></a>

#### vertex\_color\_only\_material

```python
@vertex_color_only_material.setter
def vertex_color_only_material(value: MaterialInterface) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.scalar_params_overrides"></a>

#### scalar\_params\_overrides

```python
@property
def scalar_params_overrides() -> Map[str, float]
```

(Map[str, float]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.scalar_params_overrides"></a>

#### scalar\_params\_overrides

```python
@scalar_params_overrides.setter
def scalar_params_overrides(value: Map[str, float]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.load_mip_maps"></a>

#### load\_mip\_maps

```python
@property
def load_mip_maps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.load_mip_maps"></a>

#### load\_mip\_maps

```python
@load_mip_maps.setter
def load_mip_maps(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.force_material"></a>

#### force\_material

```python
@property
def force_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.force_material"></a>

#### force\_material

```python
@force_material.setter
def force_material(value: MaterialInterface) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.skip_points"></a>

#### skip\_points

```python
@property
def skip_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.skip_points"></a>

#### skip\_points

```python
@skip_points.setter
def skip_points(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.points_triangulation_mode"></a>

#### points\_triangulation\_mode

```python
@property
def points_triangulation_mode() -> EglTFRuntimePointsTriangulationMode
```

(EglTFRuntimePointsTriangulationMode):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.points_triangulation_mode"></a>

#### points\_triangulation\_mode

```python
@points_triangulation_mode.setter
def points_triangulation_mode(
        value: EglTFRuntimePointsTriangulationMode) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.points_base_material"></a>

#### points\_base\_material

```python
@property
def points_base_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.points_base_material"></a>

#### points\_base\_material

```python
@points_base_material.setter
def points_base_material(value: MaterialInterface) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.points_scale_factor"></a>

#### points\_scale\_factor

```python
@property
def points_scale_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.points_scale_factor"></a>

#### points\_scale\_factor

```python
@points_scale_factor.setter
def points_scale_factor(value: float) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.skip_lines"></a>

#### skip\_lines

```python
@property
def skip_lines() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.skip_lines"></a>

#### skip\_lines

```python
@skip_lines.setter
def skip_lines(value: bool) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.lines_triangulation_mode"></a>

#### lines\_triangulation\_mode

```python
@property
def lines_triangulation_mode() -> EglTFRuntimeLinesTriangulationMode
```

(EglTFRuntimeLinesTriangulationMode):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.lines_triangulation_mode"></a>

#### lines\_triangulation\_mode

```python
@lines_triangulation_mode.setter
def lines_triangulation_mode(
        value: EglTFRuntimeLinesTriangulationMode) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.lines_base_material"></a>

#### lines\_base\_material

```python
@property
def lines_base_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.lines_base_material"></a>

#### lines\_base\_material

```python
@lines_base_material.setter
def lines_base_material(value: MaterialInterface) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.lines_scale_factor"></a>

#### lines\_scale\_factor

```python
@property
def lines_scale_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.lines_scale_factor"></a>

#### lines\_scale\_factor

```python
@lines_scale_factor.setter
def lines_scale_factor(value: float) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.custom_scalar_params"></a>

#### custom\_scalar\_params

```python
@property
def custom_scalar_params() -> Map[str, float]
```

(Map[str, float]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.custom_scalar_params"></a>

#### custom\_scalar\_params

```python
@custom_scalar_params.setter
def custom_scalar_params(value: Map[str, float]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.custom_vector_params"></a>

#### custom\_vector\_params

```python
@property
def custom_vector_params() -> Map[str, LinearColor]
```

(Map[str, LinearColor]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.custom_vector_params"></a>

#### custom\_vector\_params

```python
@custom_vector_params.setter
def custom_vector_params(value: Map[str, LinearColor]) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig.custom_texture_params"></a>

#### custom\_texture\_params

```python
@property
def custom_texture_params() -> Map[str, Texture]
```

(Map[str, Texture]):  [Read-Write]

<a id="unreal.glTFRuntimeMaterialsConfig.custom_texture_params"></a>

#### custom\_texture\_params

```python
@custom_texture_params.setter
def custom_texture_params(value: Map[str, Texture]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig"></a>