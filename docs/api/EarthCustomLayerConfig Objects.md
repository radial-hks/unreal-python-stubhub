## EarthCustomLayerConfig Objects

```python
class EarthCustomLayerConfig(StructBase)
```

Earth Custom Layer Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthCustomSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``build_parallel`` (bool):  [Read-Write] 是否执行并行计算
- ``build_pcg_point`` (bool):  [Read-Write] 是否生成PCG点数据
- ``debug_mode`` (bool):  [Read-Write] 是否为调试模式
- ``layer_type`` (LayerType):  [Read-Write] 使用何种数据源
- ``level_config`` (Array[int32]):  [Read-Write] 哪些级别会产生生成物
- ``prefab_type`` (ScriptStruct):  [Read-Write] 预制体类型

<a id="unreal.EarthCustomLayerConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(layer_type: LayerType = 0,
             prefab_type: ScriptStruct = None,
             level_config: Array[int] = [],
             build_pcg_point: bool = False,
             build_parallel: bool = False,
             batch_entity_size: int = 0,
             debug_mode: bool = False) -> None
```

<a id="unreal.EarthCustomLayerConfig.layer_type"></a>

#### layer\_type

```python
@property
def layer_type() -> LayerType
```

(LayerType):  [Read-Write] 使用何种数据源

<a id="unreal.EarthCustomLayerConfig.layer_type"></a>

#### layer\_type

```python
@layer_type.setter
def layer_type(value: LayerType) -> None
```

<a id="unreal.EarthCustomLayerConfig.prefab_type"></a>

#### prefab\_type

```python
@property
def prefab_type() -> ScriptStruct
```

(ScriptStruct):  [Read-Write] 预制体类型

<a id="unreal.EarthCustomLayerConfig.prefab_type"></a>

#### prefab\_type

```python
@prefab_type.setter
def prefab_type(value: ScriptStruct) -> None
```

<a id="unreal.EarthCustomLayerConfig.level_config"></a>

#### level\_config

```python
@property
def level_config() -> Array[int]
```

(Array[int32]):  [Read-Write] 哪些级别会产生生成物

<a id="unreal.EarthCustomLayerConfig.level_config"></a>

#### level\_config

```python
@level_config.setter
def level_config(value: Array[int]) -> None
```

<a id="unreal.EarthCustomLayerConfig.build_pcg_point"></a>

#### build\_pcg\_point

```python
@property
def build_pcg_point() -> bool
```

(bool):  [Read-Write] 是否生成PCG点数据

<a id="unreal.EarthCustomLayerConfig.build_pcg_point"></a>

#### build\_pcg\_point

```python
@build_pcg_point.setter
def build_pcg_point(value: bool) -> None
```

<a id="unreal.EarthCustomLayerConfig.build_parallel"></a>

#### build\_parallel

```python
@property
def build_parallel() -> bool
```

(bool):  [Read-Write] 是否执行并行计算

<a id="unreal.EarthCustomLayerConfig.build_parallel"></a>

#### build\_parallel

```python
@build_parallel.setter
def build_parallel(value: bool) -> None
```

<a id="unreal.EarthCustomLayerConfig.batch_entity_size"></a>

#### batch\_entity\_size

```python
@property
def batch_entity_size() -> int
```

(int32):  [Read-Write] 并行计算时，每批计算的实体数量

<a id="unreal.EarthCustomLayerConfig.batch_entity_size"></a>

#### batch\_entity\_size

```python
@batch_entity_size.setter
def batch_entity_size(value: int) -> None
```

<a id="unreal.EarthCustomLayerConfig.debug_mode"></a>

#### debug\_mode

```python
@property
def debug_mode() -> bool
```

(bool):  [Read-Write] 是否为调试模式

<a id="unreal.EarthCustomLayerConfig.debug_mode"></a>

#### debug\_mode

```python
@debug_mode.setter
def debug_mode(value: bool) -> None
```

<a id="unreal.EarthCustomSettings"></a>