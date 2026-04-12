## glTFRuntimeStaticMeshConfig Objects

```python
class glTFRuntimeStaticMeshConfig(StructBase)
```

Gl TFRuntime Static Mesh Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_cpu_access`` (bool):  [Read-Write]
- ``box_collisions`` (Array[Box]):  [Read-Write]
- ``build_complex_collision`` (bool):  [Read-Write]
- ``build_lumen_cards`` (bool):  [Read-Write]
- ``build_nav_collision`` (bool):  [Read-Write]
- ``build_simple_collision`` (bool):  [Read-Write]
- ``cache_mode`` (EglTFRuntimeCacheMode):  [Read-Write]
- ``collision_complexity`` (CollisionTraceFlag):  [Read-Write]
- ``custom_config_map`` (Map[str, str]):  [Read-Write]
- ``custom_config_objects`` (Array[DataAsset]):  [Read-Write]
- ``export_original_pivot_to_socket`` (str):  [Read-Write]
- ``generate_static_mesh_description`` (bool):  [Read-Write]
- ``lod_screen_size`` (Map[int32, float]):  [Read-Write]
- ``lod_screen_size_multiplier`` (float):  [Read-Write]
- ``materials_config`` (glTFRuntimeMaterialsConfig):  [Read-Write]
- ``normals_generation_strategy`` (EglTFRuntimeNormalsGenerationStrategy):  [Read-Write]
- ``outer`` (Object):  [Read-Write]
- ``pivot_position`` (EglTFRuntimePivotPosition):  [Read-Write]
- ``reverse_tangents`` (bool):  [Read-Write]
- ``reverse_winding`` (bool):  [Read-Write]
- ``sockets`` (Map[str, Transform]):  [Read-Write]
- ``sphere_collisions`` (Array[Vector4]):  [Read-Write]
- ``tangents_generation_strategy`` (EglTFRuntimeTangentsGenerationStrategy):  [Read-Write]
- ``use_high_precision_u_vs`` (bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE,
        reverse_winding: bool = False,
        build_simple_collision: bool = False,
        build_complex_collision: bool = False,
        box_collisions: Array[Box] = [],
        sphere_collisions: Array[Vector4] = [],
        collision_complexity: CollisionTraceFlag = CollisionTraceFlag.
    CTF_USE_DEFAULT,
        allow_cpu_access: bool = False,
        pivot_position: EglTFRuntimePivotPosition = EglTFRuntimePivotPosition.
    ASSET,
        outer: Object = None,
        materials_config: glTFRuntimeMaterialsConfig = [
            EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False,
            False, 0.000000, False, {},
            [
                TextureCompressionSettings.TC_DEFAULT,
                TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False,
                False, False, 0
            ], "", False, None, {}, False, None, True,
            EglTFRuntimePointsTriangulationMode.
            OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True,
            EglTFRuntimeLinesTriangulationMode.
            OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000,
            {}, {}, {}
        ],
        sockets: Map[str, Transform] = {},
        export_original_pivot_to_socket: str = "",
        lod_screen_size: Map[int, float] = {},
        normals_generation_strategy:
    EglTFRuntimeNormalsGenerationStrategy = EglTFRuntimeNormalsGenerationStrategy
    .IF_MISSING,
        tangents_generation_strategy:
    EglTFRuntimeTangentsGenerationStrategy = EglTFRuntimeTangentsGenerationStrategy
    .IF_MISSING,
        reverse_tangents: bool = False,
        use_high_precision_u_vs: bool = False,
        generate_static_mesh_description: bool = False,
        build_nav_collision: bool = False,
        custom_config_map: Map[str, str] = {},
        custom_config_objects: Array[DataAsset] = [],
        lod_screen_size_multiplier: float = 0.000000,
        build_lumen_cards: bool = False) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.cache_mode"></a>

#### cache\_mode

```python
@property
def cache_mode() -> EglTFRuntimeCacheMode
```

(EglTFRuntimeCacheMode):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.cache_mode"></a>

#### cache\_mode

```python
@cache_mode.setter
def cache_mode(value: EglTFRuntimeCacheMode) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.reverse_winding"></a>

#### reverse\_winding

```python
@property
def reverse_winding() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.reverse_winding"></a>

#### reverse\_winding

```python
@reverse_winding.setter
def reverse_winding(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.build_simple_collision"></a>

#### build\_simple\_collision

```python
@property
def build_simple_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.build_simple_collision"></a>

#### build\_simple\_collision

```python
@build_simple_collision.setter
def build_simple_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.build_complex_collision"></a>

#### build\_complex\_collision

```python
@property
def build_complex_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.build_complex_collision"></a>

#### build\_complex\_collision

```python
@build_complex_collision.setter
def build_complex_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.box_collisions"></a>

#### box\_collisions

```python
@property
def box_collisions() -> Array[Box]
```

(Array[Box]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.box_collisions"></a>

#### box\_collisions

```python
@box_collisions.setter
def box_collisions(value: Array[Box]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.sphere_collisions"></a>

#### sphere\_collisions

```python
@property
def sphere_collisions() -> Array[Vector4]
```

(Array[Vector4]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.sphere_collisions"></a>

#### sphere\_collisions

```python
@sphere_collisions.setter
def sphere_collisions(value: Array[Vector4]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.collision_complexity"></a>

#### collision\_complexity

```python
@property
def collision_complexity() -> CollisionTraceFlag
```

(CollisionTraceFlag):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.collision_complexity"></a>

#### collision\_complexity

```python
@collision_complexity.setter
def collision_complexity(value: CollisionTraceFlag) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.allow_cpu_access"></a>

#### allow\_cpu\_access

```python
@property
def allow_cpu_access() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.allow_cpu_access"></a>

#### allow\_cpu\_access

```python
@allow_cpu_access.setter
def allow_cpu_access(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.pivot_position"></a>

#### pivot\_position

```python
@property
def pivot_position() -> EglTFRuntimePivotPosition
```

(EglTFRuntimePivotPosition):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.pivot_position"></a>

#### pivot\_position

```python
@pivot_position.setter
def pivot_position(value: EglTFRuntimePivotPosition) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.outer"></a>

#### outer

```python
@property
def outer() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.outer"></a>

#### outer

```python
@outer.setter
def outer(value: Object) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.materials_config"></a>

#### materials\_config

```python
@property
def materials_config() -> glTFRuntimeMaterialsConfig
```

(glTFRuntimeMaterialsConfig):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.materials_config"></a>

#### materials\_config

```python
@materials_config.setter
def materials_config(value: glTFRuntimeMaterialsConfig) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.sockets"></a>

#### sockets

```python
@property
def sockets() -> Map[str, Transform]
```

(Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.sockets"></a>

#### sockets

```python
@sockets.setter
def sockets(value: Map[str, Transform]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.export_original_pivot_to_socket"></a>

#### export\_original\_pivot\_to\_socket

```python
@property
def export_original_pivot_to_socket() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.export_original_pivot_to_socket"></a>

#### export\_original\_pivot\_to\_socket

```python
@export_original_pivot_to_socket.setter
def export_original_pivot_to_socket(value: str) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.lod_screen_size"></a>

#### lod\_screen\_size

```python
@property
def lod_screen_size() -> Map[int, float]
```

(Map[int32, float]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.lod_screen_size"></a>

#### lod\_screen\_size

```python
@lod_screen_size.setter
def lod_screen_size(value: Map[int, float]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.normals_generation_strategy"></a>

#### normals\_generation\_strategy

```python
@property
def normals_generation_strategy() -> EglTFRuntimeNormalsGenerationStrategy
```

(EglTFRuntimeNormalsGenerationStrategy):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.normals_generation_strategy"></a>

#### normals\_generation\_strategy

```python
@normals_generation_strategy.setter
def normals_generation_strategy(
        value: EglTFRuntimeNormalsGenerationStrategy) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.tangents_generation_strategy"></a>

#### tangents\_generation\_strategy

```python
@property
def tangents_generation_strategy() -> EglTFRuntimeTangentsGenerationStrategy
```

(EglTFRuntimeTangentsGenerationStrategy):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.tangents_generation_strategy"></a>

#### tangents\_generation\_strategy

```python
@tangents_generation_strategy.setter
def tangents_generation_strategy(
        value: EglTFRuntimeTangentsGenerationStrategy) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.reverse_tangents"></a>

#### reverse\_tangents

```python
@property
def reverse_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.reverse_tangents"></a>

#### reverse\_tangents

```python
@reverse_tangents.setter
def reverse_tangents(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.use_high_precision_u_vs"></a>

#### use\_high\_precision\_u\_vs

```python
@property
def use_high_precision_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.use_high_precision_u_vs"></a>

#### use\_high\_precision\_u\_vs

```python
@use_high_precision_u_vs.setter
def use_high_precision_u_vs(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.generate_static_mesh_description"></a>

#### generate\_static\_mesh\_description

```python
@property
def generate_static_mesh_description() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.generate_static_mesh_description"></a>

#### generate\_static\_mesh\_description

```python
@generate_static_mesh_description.setter
def generate_static_mesh_description(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.build_nav_collision"></a>

#### build\_nav\_collision

```python
@property
def build_nav_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.build_nav_collision"></a>

#### build\_nav\_collision

```python
@build_nav_collision.setter
def build_nav_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.custom_config_map"></a>

#### custom\_config\_map

```python
@property
def custom_config_map() -> Map[str, str]
```

(Map[str, str]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.custom_config_map"></a>

#### custom\_config\_map

```python
@custom_config_map.setter
def custom_config_map(value: Map[str, str]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.custom_config_objects"></a>

#### custom\_config\_objects

```python
@property
def custom_config_objects() -> Array[DataAsset]
```

(Array[DataAsset]):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.custom_config_objects"></a>

#### custom\_config\_objects

```python
@custom_config_objects.setter
def custom_config_objects(value: Array[DataAsset]) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.lod_screen_size_multiplier"></a>

#### lod\_screen\_size\_multiplier

```python
@property
def lod_screen_size_multiplier() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.lod_screen_size_multiplier"></a>

#### lod\_screen\_size\_multiplier

```python
@lod_screen_size_multiplier.setter
def lod_screen_size_multiplier(value: float) -> None
```

<a id="unreal.glTFRuntimeStaticMeshConfig.build_lumen_cards"></a>

#### build\_lumen\_cards

```python
@property
def build_lumen_cards() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeStaticMeshConfig.build_lumen_cards"></a>

#### build\_lumen\_cards

```python
@build_lumen_cards.setter
def build_lumen_cards(value: bool) -> None
```

<a id="unreal.glTFRuntimeProceduralMeshConfig"></a>