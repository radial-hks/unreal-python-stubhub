## AesObjectAssetTagData Objects

```python
class AesObjectAssetTagData(StructBase)
```

单网格体资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesObjectAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_ref`` (SoftObjectPath):  [Read-Write] 模型资产引用
- ``component_class`` (SoftClassPath):  [Read-Write] 组件引用
- ``custom_data`` (Map[Name, float]):  [Read-Write] 自定义数据
- ``override_materials`` (Array[SoftObjectPath]):  [Read-Write] 替换材质列表
- ``primitive_data`` (Map[Name, float]):  [Read-Write] 图元数据

<a id="unreal.AesObjectAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_ref: SoftObjectPath = [""],
             component_class: SoftClassPath = [""],
             override_materials: Array[SoftObjectPath] = [],
             primitive_data: Map[Name, float] = {},
             custom_data: Map[Name, float] = {}) -> None
```

<a id="unreal.AesObjectAssetTagData.asset_ref"></a>

#### asset\_ref

```python
@property
def asset_ref() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 模型资产引用

<a id="unreal.AesObjectAssetTagData.asset_ref"></a>

#### asset\_ref

```python
@asset_ref.setter
def asset_ref(value: SoftObjectPath) -> None
```

<a id="unreal.AesObjectAssetTagData.component_class"></a>

#### component\_class

```python
@property
def component_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] 组件引用

<a id="unreal.AesObjectAssetTagData.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: SoftClassPath) -> None
```

<a id="unreal.AesObjectAssetTagData.override_materials"></a>

#### override\_materials

```python
@property
def override_materials() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 替换材质列表

<a id="unreal.AesObjectAssetTagData.override_materials"></a>

#### override\_materials

```python
@override_materials.setter
def override_materials(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.AesObjectAssetTagData.primitive_data"></a>

#### primitive\_data

```python
@property
def primitive_data() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 图元数据

<a id="unreal.AesObjectAssetTagData.primitive_data"></a>

#### primitive\_data

```python
@primitive_data.setter
def primitive_data(value: Map[Name, float]) -> None
```

<a id="unreal.AesObjectAssetTagData.custom_data"></a>

#### custom\_data

```python
@property
def custom_data() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 自定义数据

<a id="unreal.AesObjectAssetTagData.custom_data"></a>

#### custom\_data

```python
@custom_data.setter
def custom_data(value: Map[Name, float]) -> None
```

<a id="unreal.AesObjectAssetData"></a>