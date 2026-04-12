## EarthVegetationSettings Objects

```python
class EarthVegetationSettings(EarthLayerSettingsBase)
```

地球植被设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthVegetationSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_levels`` (Array[int32]):  [Read-Write] 需要缓存的级别
- ``cast_shadow`` (bool):  [Read-Write]
- ``city_vegetation_biome_rule_data_table`` (SoftObjectPath):  [Read-Write] 城市地区植被规则配置
- ``default_eco_id`` (int32):  [Read-Write]
- ``default_vegetation_biome_rule_data_table`` (SoftObjectPath):  [Read-Write] 默认地区植被规则配置
- ``degree_range`` (IntPoint):  [Read-Write] 全局随机旋转角度
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``desired_max_draw_distance`` (float):  [Read-Write]
- ``dispersed_degrees`` (Array[int32]):  [Read-Write] 全局分散度
- ``fix_dom_sample_level`` (bool):  [Read-Write]
- ``fixed_dom_sample_level`` (int32):  [Read-Write]
- ``global_density_scale`` (float):  [Read-Write] 全局密度缩放值
- ``halton_base`` (IntPoint):  [Read-Write]
- ``instance_register_slice_factor`` (int32):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write] 植被是否显示
- ``level_config`` (Map[int32, EarthVegetationLevelConfig]):  [Read-Write] 哪些级别会产生生成物
- ``max_concurrent_batch`` (int32):  [Read-Write]
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``max_register_instance_num`` (int32):  [Read-Write]
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``preallocate_instance_component_instance_num`` (int32):  [Read-Write]
- ``preallocate_instance_components`` (int32):  [Read-Write]
- ``random_offset`` (Vector):  [Read-Write] 全局随机偏移值（cm）
- ``random_seed`` (int32):  [Read-Write] The random seed used to generate the random number.
- ``receives_decals`` (bool):  [Read-Write] 是否接收贴花
- ``sample_slice_factor`` (int32):  [Read-Write] 并行任务大小
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``total_scale`` (float):  [Read-Write] 全局植被缩放比例
- ``use_bake_board`` (bool):  [Read-Write]
- ``use_default_eco_id`` (bool):  [Read-Write] The default ecoregion id.
  find the ecoregion id in legendData.json.
- ``use_dispersed_degree_samples`` (bool):  [Read-Write] 是否使用全局分散度
- ``use_distance_cull`` (bool):  [Read-Write]
- ``use_instance_component_pool`` (bool):  [Read-Write]
- ``use_parallel_sample`` (bool):  [Read-Write] 是否并行运算
- ``use_random_offset`` (bool):  [Read-Write] 是否使用随机偏移值
- ``use_random_rotation`` (bool):  [Read-Write] 是否使用随机旋转值
- ``vgmthreshhold`` (IntPoint):  [Read-Write] Vgm边缘值范围
- ``world_position_offset_disable_distance`` (int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False,
             default_vegetation_biome_rule_data_table: SoftObjectPath = [""],
             city_vegetation_biome_rule_data_table: SoftObjectPath = [""],
             is_visible: bool = False,
             halton_base: IntPoint = [0, 0],
             use_default_eco_id: bool = False,
             default_eco_id: int = 0,
             random_seed: int = 0,
             total_scale: float = 0.000000,
             vgmthreshhold: IntPoint = [0, 0],
             use_random_offset: bool = False,
             random_offset: Vector = [0.000000, 0.000000, 0.000000],
             use_random_rotation: bool = False,
             use_dispersed_degree_samples: bool = False,
             degree_range: IntPoint = [0, 0],
             dispersed_degrees: Array[int] = [],
             global_density_scale: float = 0.000000,
             fix_dom_sample_level: bool = False,
             fixed_dom_sample_level: int = 0,
             use_parallel_sample: bool = False,
             sample_slice_factor: int = 0,
             cast_shadow: bool = False,
             use_distance_cull: bool = False,
             desired_max_draw_distance: float = 0.000000,
             max_register_instance_num: int = 0,
             use_instance_component_pool: bool = False,
             preallocate_instance_components: int = 0,
             preallocate_instance_component_instance_num: int = 0,
             max_concurrent_batch: int = 0,
             instance_register_slice_factor: int = 0,
             world_position_offset_disable_distance: int = 0) -> None
```

<a id="unreal.EarthVegetationSettings.default_vegetation_biome_rule_data_table"></a>

#### default\_vegetation\_biome\_rule\_data\_table

```python
@property
def default_vegetation_biome_rule_data_table() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 默认地区植被规则配置

<a id="unreal.EarthVegetationSettings.default_vegetation_biome_rule_data_table"></a>

#### default\_vegetation\_biome\_rule\_data\_table

```python
@default_vegetation_biome_rule_data_table.setter
def default_vegetation_biome_rule_data_table(value: SoftObjectPath) -> None
```

<a id="unreal.EarthVegetationSettings.city_vegetation_biome_rule_data_table"></a>

#### city\_vegetation\_biome\_rule\_data\_table

```python
@property
def city_vegetation_biome_rule_data_table() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 城市地区植被规则配置

<a id="unreal.EarthVegetationSettings.city_vegetation_biome_rule_data_table"></a>

#### city\_vegetation\_biome\_rule\_data\_table

```python
@city_vegetation_biome_rule_data_table.setter
def city_vegetation_biome_rule_data_table(value: SoftObjectPath) -> None
```

<a id="unreal.EarthVegetationSettings.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write] 植被是否显示

<a id="unreal.EarthVegetationSettings.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.halton_base"></a>

#### halton\_base

```python
@property
def halton_base() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.EarthVegetationSettings.halton_base"></a>

#### halton\_base

```python
@halton_base.setter
def halton_base(value: IntPoint) -> None
```

<a id="unreal.EarthVegetationSettings.use_default_eco_id"></a>

#### use\_default\_eco\_id

```python
@property
def use_default_eco_id() -> bool
```

(bool):  [Read-Write] The default ecoregion id.
find the ecoregion id in legendData.json.

<a id="unreal.EarthVegetationSettings.use_default_eco_id"></a>

#### use\_default\_eco\_id

```python
@use_default_eco_id.setter
def use_default_eco_id(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.default_eco_id"></a>

#### default\_eco\_id

```python
@property
def default_eco_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.default_eco_id"></a>

#### default\_eco\_id

```python
@default_eco_id.setter
def default_eco_id(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.random_seed"></a>

#### random\_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] The random seed used to generate the random number.

<a id="unreal.EarthVegetationSettings.random_seed"></a>

#### random\_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.total_scale"></a>

#### total\_scale

```python
@property
def total_scale() -> float
```

(float):  [Read-Write] 全局植被缩放比例

<a id="unreal.EarthVegetationSettings.total_scale"></a>

#### total\_scale

```python
@total_scale.setter
def total_scale(value: float) -> None
```

<a id="unreal.EarthVegetationSettings.vgmthreshhold"></a>

#### vgmthreshhold

```python
@property
def vgmthreshhold() -> IntPoint
```

(IntPoint):  [Read-Write] Vgm边缘值范围

<a id="unreal.EarthVegetationSettings.vgmthreshhold"></a>

#### vgmthreshhold

```python
@vgmthreshhold.setter
def vgmthreshhold(value: IntPoint) -> None
```

<a id="unreal.EarthVegetationSettings.use_random_offset"></a>

#### use\_random\_offset

```python
@property
def use_random_offset() -> bool
```

(bool):  [Read-Write] 是否使用随机偏移值

<a id="unreal.EarthVegetationSettings.use_random_offset"></a>

#### use\_random\_offset

```python
@use_random_offset.setter
def use_random_offset(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.random_offset"></a>

#### random\_offset

```python
@property
def random_offset() -> Vector
```

(Vector):  [Read-Write] 全局随机偏移值（cm）

<a id="unreal.EarthVegetationSettings.random_offset"></a>

#### random\_offset

```python
@random_offset.setter
def random_offset(value: Vector) -> None
```

<a id="unreal.EarthVegetationSettings.use_random_rotation"></a>

#### use\_random\_rotation

```python
@property
def use_random_rotation() -> bool
```

(bool):  [Read-Write] 是否使用随机旋转值

<a id="unreal.EarthVegetationSettings.use_random_rotation"></a>

#### use\_random\_rotation

```python
@use_random_rotation.setter
def use_random_rotation(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.use_dispersed_degree_samples"></a>

#### use\_dispersed\_degree\_samples

```python
@property
def use_dispersed_degree_samples() -> bool
```

(bool):  [Read-Write] 是否使用全局分散度

<a id="unreal.EarthVegetationSettings.use_dispersed_degree_samples"></a>

#### use\_dispersed\_degree\_samples

```python
@use_dispersed_degree_samples.setter
def use_dispersed_degree_samples(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.degree_range"></a>

#### degree\_range

```python
@property
def degree_range() -> IntPoint
```

(IntPoint):  [Read-Write] 全局随机旋转角度

<a id="unreal.EarthVegetationSettings.degree_range"></a>

#### degree\_range

```python
@degree_range.setter
def degree_range(value: IntPoint) -> None
```

<a id="unreal.EarthVegetationSettings.dispersed_degrees"></a>

#### dispersed\_degrees

```python
@property
def dispersed_degrees() -> Array[int]
```

(Array[int32]):  [Read-Write] 全局分散度

<a id="unreal.EarthVegetationSettings.dispersed_degrees"></a>

#### dispersed\_degrees

```python
@dispersed_degrees.setter
def dispersed_degrees(value: Array[int]) -> None
```

<a id="unreal.EarthVegetationSettings.global_density_scale"></a>

#### global\_density\_scale

```python
@property
def global_density_scale() -> float
```

(float):  [Read-Write] 全局密度缩放值

<a id="unreal.EarthVegetationSettings.global_density_scale"></a>

#### global\_density\_scale

```python
@global_density_scale.setter
def global_density_scale(value: float) -> None
```

<a id="unreal.EarthVegetationSettings.fix_dom_sample_level"></a>

#### fix\_dom\_sample\_level

```python
@property
def fix_dom_sample_level() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthVegetationSettings.fix_dom_sample_level"></a>

#### fix\_dom\_sample\_level

```python
@fix_dom_sample_level.setter
def fix_dom_sample_level(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.fixed_dom_sample_level"></a>

#### fixed\_dom\_sample\_level

```python
@property
def fixed_dom_sample_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.fixed_dom_sample_level"></a>

#### fixed\_dom\_sample\_level

```python
@fixed_dom_sample_level.setter
def fixed_dom_sample_level(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.use_parallel_sample"></a>

#### use\_parallel\_sample

```python
@property
def use_parallel_sample() -> bool
```

(bool):  [Read-Write] 是否并行运算

<a id="unreal.EarthVegetationSettings.use_parallel_sample"></a>

#### use\_parallel\_sample

```python
@use_parallel_sample.setter
def use_parallel_sample(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.sample_slice_factor"></a>

#### sample\_slice\_factor

```python
@property
def sample_slice_factor() -> int
```

(int32):  [Read-Write] 并行任务大小

<a id="unreal.EarthVegetationSettings.sample_slice_factor"></a>

#### sample\_slice\_factor

```python
@sample_slice_factor.setter
def sample_slice_factor(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.cast_shadow"></a>

#### cast\_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthVegetationSettings.cast_shadow"></a>

#### cast\_shadow

```python
@cast_shadow.setter
def cast_shadow(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.use_distance_cull"></a>

#### use\_distance\_cull

```python
@property
def use_distance_cull() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthVegetationSettings.use_distance_cull"></a>

#### use\_distance\_cull

```python
@use_distance_cull.setter
def use_distance_cull(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.desired_max_draw_distance"></a>

#### desired\_max\_draw\_distance

```python
@property
def desired_max_draw_distance() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthVegetationSettings.desired_max_draw_distance"></a>

#### desired\_max\_draw\_distance

```python
@desired_max_draw_distance.setter
def desired_max_draw_distance(value: float) -> None
```

<a id="unreal.EarthVegetationSettings.max_register_instance_num"></a>

#### max\_register\_instance\_num

```python
@property
def max_register_instance_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.max_register_instance_num"></a>

#### max\_register\_instance\_num

```python
@max_register_instance_num.setter
def max_register_instance_num(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.use_instance_component_pool"></a>

#### use\_instance\_component\_pool

```python
@property
def use_instance_component_pool() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthVegetationSettings.use_instance_component_pool"></a>

#### use\_instance\_component\_pool

```python
@use_instance_component_pool.setter
def use_instance_component_pool(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings.preallocate_instance_components"></a>

#### preallocate\_instance\_components

```python
@property
def preallocate_instance_components() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.preallocate_instance_components"></a>

#### preallocate\_instance\_components

```python
@preallocate_instance_components.setter
def preallocate_instance_components(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.preallocate_instance_component_instance_num"></a>

#### preallocate\_instance\_component\_instance\_num

```python
@property
def preallocate_instance_component_instance_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.preallocate_instance_component_instance_num"></a>

#### preallocate\_instance\_component\_instance\_num

```python
@preallocate_instance_component_instance_num.setter
def preallocate_instance_component_instance_num(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.max_concurrent_batch"></a>

#### max\_concurrent\_batch

```python
@property
def max_concurrent_batch() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.max_concurrent_batch"></a>

#### max\_concurrent\_batch

```python
@max_concurrent_batch.setter
def max_concurrent_batch(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.instance_register_slice_factor"></a>

#### instance\_register\_slice\_factor

```python
@property
def instance_register_slice_factor() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.instance_register_slice_factor"></a>

#### instance\_register\_slice\_factor

```python
@instance_register_slice_factor.setter
def instance_register_slice_factor(value: int) -> None
```

<a id="unreal.EarthVegetationSettings.world_position_offset_disable_distance"></a>

#### world\_position\_offset\_disable\_distance

```python
@property
def world_position_offset_disable_distance() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthVegetationSettings.world_position_offset_disable_distance"></a>

#### world\_position\_offset\_disable\_distance

```python
@world_position_offset_disable_distance.setter
def world_position_offset_disable_distance(value: int) -> None
```

<a id="unreal.EarthVegetationLevelConfig"></a>