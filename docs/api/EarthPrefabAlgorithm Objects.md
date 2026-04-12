## EarthPrefabAlgorithm Objects

```python
class EarthPrefabAlgorithm(Object)
```

预制体算法的基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAlgorithm.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``required_fragments`` (Array[ScriptStruct]):  [Read-Write] 算法所需的数据片段类型

<a id="unreal.EarthPrefabAlgorithm.required_fragments"></a>

#### required\_fragments

```python
@property
def required_fragments() -> Array[ScriptStruct]
```

(Array[ScriptStruct]):  [Read-Only] 算法所需的数据片段类型

<a id="unreal.EarthPrefabAlgorithm.receive_guess_internal"></a>

#### receive\_guess\_internal

```python
def receive_guess_internal(
        library: EarthRegionalPrefabAssetLibrary,
        input_collection: EarthInputCollection) -> EarthInputCollection
```

x.receive_guess_internal(library, input_collection) -> EarthInputCollection
Receive Guess Internal

Args:
    library (EarthRegionalPrefabAssetLibrary): 
    input_collection (EarthInputCollection): 

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAlgorithm.receive_execute_internal"></a>

#### receive\_execute\_internal

```python
def receive_execute_internal(
        input_collection: EarthInputCollection) -> EarthOutputCollection
```

x.receive_execute_internal(input_collection) -> EarthOutputCollection
执行算法核心逻辑的内部实现（蓝图实现）

Args:
    input_collection (EarthInputCollection): 输入数据集合

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection): 输出数据集合 说明： 1. 这是算法执行的核心入口，子类可重写此方法实现具体业务逻辑 2. 推荐通过EntityLoop方法遍历实体，会自动处理RequiredFragments的校验 3. 输入数据的有效性需在调用前通过ConfigureRequirements保证 4. 应通过OutputCollection.Merge()来合并输出结果，避免直接修改集合

<a id="unreal.EarthPrefabAlgorithm.load_algorithm_instance"></a>

#### load\_algorithm\_instance

```python
@classmethod
def load_algorithm_instance(cls, outer: Object,
                            algorithm: Class) -> EarthPrefabAlgorithm
```

X.load_algorithm_instance(outer, algorithm) -> EarthPrefabAlgorithm
加载算法实例

Args:
    outer (Object): 
    algorithm (type(Class)): 

Returns:
    EarthPrefabAlgorithm:

<a id="unreal.EarthPrefabAlgorithm.guess_parallel"></a>

#### guess\_parallel

```python
@classmethod
def guess_parallel(cls,
                   algorithm: Class,
                   prefab_assets: Array[EarthPrefabAsset],
                   batch_entity_size: int = 512) -> EarthInputCollection
```

X.guess_parallel(algorithm, prefab_assets, batch_entity_size=512) -> EarthInputCollection
静态并行猜测器

Args:
    algorithm (type(Class)): 
    prefab_assets (Array[EarthPrefabAsset]): 
    batch_entity_size (int32): 

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAlgorithm.guess_loop_body"></a>

#### guess\_loop\_body

```python
def guess_loop_body(
        library: EarthRegionalPrefabAssetLibrary,
        input_collection: EarthInputCollection, data: EarthPrefabBase,
        iteration: int) -> Tuple[EarthInputCollection, EarthPrefabBase]
```

x.guess_loop_body(library, input_collection, data, iteration) -> (input_collection=EarthInputCollection, data=EarthPrefabBase)
Guess Loop Body

Args:
    library (EarthRegionalPrefabAssetLibrary): 
    input_collection (EarthInputCollection): 
    data (EarthPrefabBase): 
    iteration (int32): 

Returns:
    tuple: 

    input_collection (EarthInputCollection): 

    data (EarthPrefabBase):

<a id="unreal.EarthPrefabAlgorithm.guess_loop"></a>

#### guess\_loop

```python
def guess_loop(library: EarthRegionalPrefabAssetLibrary,
               input_collection: EarthInputCollection) -> EarthInputCollection
```

x.guess_loop(library, input_collection) -> EarthInputCollection
在所有实体上执行GuessLoopBody

Args:
    library (EarthRegionalPrefabAssetLibrary): 
    input_collection (EarthInputCollection): 

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAlgorithm.guess"></a>

#### guess

```python
@classmethod
def guess(cls, algorithm: Class,
          prefab_assets: Array[EarthPrefabAsset]) -> EarthInputCollection
```

X.guess(algorithm, prefab_assets) -> EarthInputCollection
静态执行猜测器

Args:
    algorithm (type(Class)): 
    prefab_assets (Array[EarthPrefabAsset]): 

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAlgorithm.execute_with_prefab"></a>

#### execute\_with\_prefab

```python
@classmethod
def execute_with_prefab(
        cls, algorithm: Class, prefab: EarthPrefabBase,
        input_collection: EarthInputCollection) -> EarthOutputCollection
```

X.execute_with_prefab(algorithm, prefab, input_collection) -> EarthOutputCollection
静态执行算法，需要输入预制体数据
执行算法前需自行保证所有数据片段的有效性

Args:
    algorithm (type(Class)): 
    prefab (EarthPrefabBase): 
    input_collection (EarthInputCollection): 

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAlgorithm.execute"></a>

#### execute

```python
@classmethod
def execute(cls, algorithm: Class,
            input_collection: EarthInputCollection) -> EarthOutputCollection
```

X.execute(algorithm, input_collection) -> EarthOutputCollection
静态执行算法
执行算法前需自行保证所有数据片段的有效性

Args:
    algorithm (type(Class)): 
    input_collection (EarthInputCollection): 

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAlgorithm.entity_loop_body"></a>

#### entity\_loop\_body

```python
def entity_loop_body(input_collection: EarthInputCollection,
                     data: EarthPrefabBase,
                     entity_index: int) -> EarthOutputCollection
```

x.entity_loop_body(input_collection, data, entity_index) -> EarthOutputCollection
对单个实体执行循环体操作

Args:
    input_collection (EarthInputCollection): 输入数据集合
    data (EarthPrefabBase): 当前处理的实体数据
    entity_index (int32): 当前迭代次数（从0开始），标识当前处理的实体序号 说明： 1. 该函数会在EntityLoop中对每个实体迭代执行一次 2. 子类可通过重写此方法实现具体的逐实体处理逻辑，会自动处理RequiredFragments的校验 3. 通过修改OutputCollection来存储处理结果 4. 预制体数据通过InData参数传递，需确保已注册对应的RequiredFragments，且Fragment需确保有效性

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection): 输出数据集合

<a id="unreal.EarthPrefabAlgorithm.entity_loop"></a>

#### entity\_loop

```python
def entity_loop(
        input_collection: EarthInputCollection) -> EarthOutputCollection
```

x.entity_loop(input_collection) -> EarthOutputCollection
在所有实体上执行EntityLoopBody

Args:
    input_collection (EarthInputCollection): 

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAlgorithm.configure_requirements"></a>

#### configure\_requirements

```python
def configure_requirements() -> None
```

x.configure_requirements() -> None
配置算法所需要的预制体类型和数据片段类型

<a id="unreal.EarthPrefabAlgorithm.call_guess"></a>

#### call\_guess

```python
def call_guess(
        library: EarthRegionalPrefabAssetLibrary) -> EarthInputCollection
```

x.call_guess(library) -> EarthInputCollection
执行猜测器

Args:
    library (EarthRegionalPrefabAssetLibrary): 

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAlgorithm.call_execute_with_prefab"></a>

#### call\_execute\_with\_prefab

```python
def call_execute_with_prefab(
        prefab: EarthPrefabBase,
        input_collection: EarthInputCollection) -> EarthOutputCollection
```

x.call_execute_with_prefab(prefab, input_collection) -> EarthOutputCollection
执行算法

Args:
    prefab (EarthPrefabBase): 
    input_collection (EarthInputCollection): 

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAlgorithm.call_execute"></a>

#### call\_execute

```python
def call_execute(
        input_collection: EarthInputCollection) -> EarthOutputCollection
```

x.call_execute(input_collection) -> EarthOutputCollection
执行算法

Args:
    input_collection (EarthInputCollection): 

Returns:
    EarthOutputCollection: 

    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAlgorithm.add_requirement"></a>

#### add\_requirement

```python
def add_requirement(fragment_type: ScriptStruct) -> None
```

x.add_requirement(fragment_type) -> None
注册所需的数据片段类型

Args:
    fragment_type (ScriptStruct):

<a id="unreal.EarthBuildingPrefabAlgorithm"></a>