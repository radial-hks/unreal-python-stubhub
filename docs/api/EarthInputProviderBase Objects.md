## EarthInputProviderBase Objects

```python
class EarthInputProviderBase(Object)
```

输入数据提供者的基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInputTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_prefab`` (EarthPrefabBase):  [Read-Write] 由输入数据提供者提供的全局预制体数据

<a id="unreal.EarthInputProviderBase.global_prefab"></a>

#### global\_prefab

```python
@property
def global_prefab() -> EarthPrefabBase
```

(EarthPrefabBase):  [Read-Write] 由输入数据提供者提供的全局预制体数据

<a id="unreal.EarthInputProviderBase.global_prefab"></a>

#### global\_prefab

```python
@global_prefab.setter
def global_prefab(value: EarthPrefabBase) -> None
```

<a id="unreal.EarthInputProviderBase.pre_generate_input_collection"></a>

#### pre\_generate\_input\_collection

```python
def pre_generate_input_collection(
        world_context_object: Object) -> EarthInputCollection
```

x.pre_generate_input_collection(world_context_object) -> EarthInputCollection
生成输入数据集合前的接口方法

Args:
    world_context_object (Object): 提供世界上下文信息的UObject

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection): （输出参数）生成的输入数据集合将被填充到此引用参数中

<a id="unreal.EarthInputProviderBase.generate_input_collection"></a>

#### generate\_input\_collection

```python
def generate_input_collection(
        world_context_object: Object) -> EarthInputCollection
```

x.generate_input_collection(world_context_object) -> EarthInputCollection
生成输入数据集合的接口方法

Args:
    world_context_object (Object): 提供世界上下文信息的UObject

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection): （输出参数）生成的输入数据集合将被填充到此引用参数中

<a id="unreal.EarthInputProviderBase.execute_generate_input_collection"></a>

#### execute\_generate\_input\_collection

```python
def execute_generate_input_collection(
        world_context_object: Object) -> EarthInputCollection
```

x.execute_generate_input_collection(world_context_object) -> EarthInputCollection
执行完整的输入数据集合生成流程

Args:
    world_context_object (Object): 提供世界上下文信息的UObject

Returns:
    EarthInputCollection: 

    input_collection (EarthInputCollection): （输出参数）生成的输入数据集合将被填充到此引用参数中

<a id="unreal.EarthInputProvider_Actor"></a>