## EarthInputCollection Objects

```python
class EarthInputCollection(StructBase)
```

输入数据集合
实体数据集为空时，共享数据的父级坐标变换等价于一个点数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInputTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instanced_entities`` (Array[InstancedStruct]):  [Read-Write] 实例化结构体类型的实体数据，给当前结构体作为UObject的成员时序列化所用
- ``owned_component`` (ActorComponent):  [Read-Write] 添加该成员是为了使当前结构体作为AActor的成员时，带有CPF_ContainsInstancedReference，避免在AActor::ResetPropertiesForConstruction()中被CDO填充默认值

<a id="unreal.EarthInputCollection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instanced_entities: Array[InstancedStruct] = [],
             owned_component: ActorComponent = None) -> None
```

<a id="unreal.EarthInputCollection.instanced_entities"></a>

#### instanced\_entities

```python
@property
def instanced_entities() -> Array[InstancedStruct]
```

(Array[InstancedStruct]):  [Read-Write] 实例化结构体类型的实体数据，给当前结构体作为UObject的成员时序列化所用

<a id="unreal.EarthInputCollection.instanced_entities"></a>

#### instanced\_entities

```python
@instanced_entities.setter
def instanced_entities(value: Array[InstancedStruct]) -> None
```

<a id="unreal.EarthInputCollection.owned_component"></a>

#### owned\_component

```python
@property
def owned_component() -> ActorComponent
```

(ActorComponent):  [Read-Write] 添加该成员是为了使当前结构体作为AActor的成员时，带有CPF_ContainsInstancedReference，避免在AActor::ResetPropertiesForConstruction()中被CDO填充默认值

<a id="unreal.EarthInputCollection.owned_component"></a>

#### owned\_component

```python
@owned_component.setter
def owned_component(value: ActorComponent) -> None
```

<a id="unreal.EarthInstanceSplineFragment"></a>