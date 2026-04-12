## EarthPrefabAsset Objects

```python
class EarthPrefabAsset(DataAsset)
```

地球预制体资产，用于定义可复用的地球数字资产

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_fragments`` (Array[InstancedStruct]):  [Read-Write] 额外的片段数据，结构相同的片段有且仅有一份，会覆盖模板内相同的片段
- ``algorithm`` (Class):  [Read-Write] 算法类
- ``asset_id`` (str):  [Read-Only] 预制体资产的唯一识别码
- ``asset_version`` (uint32):  [Read-Only] 预制体资产版本号，仅在编辑时增加
- ``input_collection`` (EarthInputCollection):  [Read-Write] 预制体资产生前的输入数据集合
- ``output_collection`` (EarthOutputCollection):  [Read-Write] 预制体资产生成后的输出数据集合
- ``prefab`` (InstancedStruct):  [Read-Write] 预制体数据，仅在无模板时能手动定义，在有模板时会缓存完整的预制体数据
- ``prefab_struct`` (ScriptStruct):  [Read-Write]
- ``template_asset`` (EarthPrefabAsset):  [Read-Write] 预制体资产模板
- ``thumbnail`` (Texture2D):  [Read-Write] 预制体资产缩略图，推荐像素为256x256
- ``valid_algorithm`` (bool):  [Read-Write] 预制体数据是否有效
- ``valid_input_collection`` (bool):  [Read-Only] 预制体数据是否有效
- ``valid_output_collection`` (bool):  [Read-Only] 预制体数据是否有效
- ``valid_prefab`` (bool):  [Read-Write] 预制体数据是否有效

<a id="unreal.EarthPrefabAsset.template_asset"></a>

#### template\_asset

```python
@property
def template_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 预制体资产模板

<a id="unreal.EarthPrefabAsset.template_asset"></a>

#### template\_asset

```python
@template_asset.setter
def template_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthPrefabAsset.prefab"></a>

#### prefab

```python
@property
def prefab() -> InstancedStruct
```

(InstancedStruct):  [Read-Write] 预制体数据，仅在无模板时能手动定义，在有模板时会缓存完整的预制体数据

<a id="unreal.EarthPrefabAsset.prefab"></a>

#### prefab

```python
@prefab.setter
def prefab(value: InstancedStruct) -> None
```

<a id="unreal.EarthPrefabAsset.additional_fragments"></a>

#### additional\_fragments

```python
@property
def additional_fragments() -> Array[InstancedStruct]
```

(Array[InstancedStruct]):  [Read-Write] 额外的片段数据，结构相同的片段有且仅有一份，会覆盖模板内相同的片段

<a id="unreal.EarthPrefabAsset.additional_fragments"></a>

#### additional\_fragments

```python
@additional_fragments.setter
def additional_fragments(value: Array[InstancedStruct]) -> None
```

<a id="unreal.EarthPrefabAsset.valid_prefab"></a>

#### valid\_prefab

```python
@property
def valid_prefab() -> bool
```

(bool):  [Read-Write] 预制体数据是否有效

<a id="unreal.EarthPrefabAsset.valid_prefab"></a>

#### valid\_prefab

```python
@valid_prefab.setter
def valid_prefab(value: bool) -> None
```

<a id="unreal.EarthPrefabAsset.input_collection"></a>

#### input\_collection

```python
@property
def input_collection() -> EarthInputCollection
```

(EarthInputCollection):  [Read-Write] 预制体资产生前的输入数据集合

<a id="unreal.EarthPrefabAsset.input_collection"></a>

#### input\_collection

```python
@input_collection.setter
def input_collection(value: EarthInputCollection) -> None
```

<a id="unreal.EarthPrefabAsset.valid_input_collection"></a>

#### valid\_input\_collection

```python
@property
def valid_input_collection() -> bool
```

(bool):  [Read-Only] 预制体数据是否有效

<a id="unreal.EarthPrefabAsset.algorithm"></a>

#### algorithm

```python
@property
def algorithm() -> Class
```

(Class):  [Read-Write] 算法类

<a id="unreal.EarthPrefabAsset.algorithm"></a>

#### algorithm

```python
@algorithm.setter
def algorithm(value: Class) -> None
```

<a id="unreal.EarthPrefabAsset.valid_algorithm"></a>

#### valid\_algorithm

```python
@property
def valid_algorithm() -> bool
```

(bool):  [Read-Write] 预制体数据是否有效

<a id="unreal.EarthPrefabAsset.valid_algorithm"></a>

#### valid\_algorithm

```python
@valid_algorithm.setter
def valid_algorithm(value: bool) -> None
```

<a id="unreal.EarthPrefabAsset.output_collection"></a>

#### output\_collection

```python
@property
def output_collection() -> EarthOutputCollection
```

(EarthOutputCollection):  [Read-Write] 预制体资产生成后的输出数据集合

<a id="unreal.EarthPrefabAsset.output_collection"></a>

#### output\_collection

```python
@output_collection.setter
def output_collection(value: EarthOutputCollection) -> None
```

<a id="unreal.EarthPrefabAsset.valid_output_collection"></a>

#### valid\_output\_collection

```python
@property
def valid_output_collection() -> bool
```

(bool):  [Read-Only] 预制体数据是否有效

<a id="unreal.EarthPrefabAsset.thumbnail"></a>

#### thumbnail

```python
@property
def thumbnail() -> Texture2D
```

(Texture2D):  [Read-Write] 预制体资产缩略图，推荐像素为256x256

<a id="unreal.EarthPrefabAsset.thumbnail"></a>

#### thumbnail

```python
@thumbnail.setter
def thumbnail(value: Texture2D) -> None
```

<a id="unreal.EarthPrefabAsset.prefab_struct"></a>

#### prefab\_struct

```python
@property
def prefab_struct() -> ScriptStruct
```

(ScriptStruct):  [Read-Write]

<a id="unreal.EarthPrefabAsset.prefab_struct"></a>

#### prefab\_struct

```python
@prefab_struct.setter
def prefab_struct(value: ScriptStruct) -> None
```

<a id="unreal.EarthPrefabAsset.validate_asset"></a>

#### validate\_asset

```python
def validate_asset() -> None
```

x.validate_asset() -> None
执行预制体资产的有效性验证

<a id="unreal.EarthPrefabAsset.update_referencing_prefab_assets"></a>

#### update\_referencing\_prefab\_assets

```python
def update_referencing_prefab_assets() -> None
```

x.update_referencing_prefab_assets() -> None
更新引用此预制体资产的其他预制体资产

<a id="unreal.EarthPrefabAsset.update_prefab_on_property_change"></a>

#### update\_prefab\_on\_property\_change

```python
def update_prefab_on_property_change() -> None
```

x.update_prefab_on_property_change() -> None
使用模板资产更新当前预制体资产

<a id="unreal.EarthPrefabAsset.update_algorithm_on_property_change"></a>

#### update\_algorithm\_on\_property\_change

```python
def update_algorithm_on_property_change() -> None
```

x.update_algorithm_on_property_change() -> None
使用模板资产更新当前预制体资产

<a id="unreal.EarthPrefabAsset.set_thumbnail"></a>

#### set\_thumbnail

```python
def set_thumbnail(thumbnail: Texture2D) -> None
```

x.set_thumbnail(thumbnail) -> None
设置预制体资产缩略图

Args:
    thumbnail (Texture2D):

<a id="unreal.EarthPrefabAsset.set_prefab"></a>

#### set\_prefab

```python
def set_prefab(prefab: InstancedStruct) -> None
```

x.set_prefab(prefab) -> None
设置预制体

Args:
    prefab (InstancedStruct):

<a id="unreal.EarthPrefabAsset.set_output_collection"></a>

#### set\_output\_collection

```python
def set_output_collection(output_collection: EarthOutputCollection) -> None
```

x.set_output_collection(output_collection) -> None
设置输出数据集合

Args:
    output_collection (EarthOutputCollection):

<a id="unreal.EarthPrefabAsset.set_input_collection"></a>

#### set\_input\_collection

```python
def set_input_collection(input_collection: EarthInputCollection) -> None
```

x.set_input_collection(input_collection) -> None
设置输入数据集合

Args:
    input_collection (EarthInputCollection):

<a id="unreal.EarthPrefabAsset.set_algorithm"></a>

#### set\_algorithm

```python
def set_algorithm(algorithm: Class) -> None
```

x.set_algorithm(algorithm) -> None
设置算法类

Args:
    algorithm (type(Class)):

<a id="unreal.EarthPrefabAsset.on_property_change"></a>

#### on\_property\_change

```python
def on_property_change() -> None
```

x.on_property_change() -> None
属性改变事件

<a id="unreal.EarthPrefabAsset.load_thumbnail"></a>

#### load\_thumbnail

```python
def load_thumbnail() -> None
```

x.load_thumbnail() -> None
从缩略图资产加载缩略图

<a id="unreal.EarthPrefabAsset.load_data_from_fragment"></a>

#### load\_data\_from\_fragment

```python
def load_data_from_fragment() -> None
```

x.load_data_from_fragment() -> None
从数据片段加载预制体所需的数据

<a id="unreal.EarthPrefabAsset.get_thumbnail"></a>

#### get\_thumbnail

```python
def get_thumbnail() -> Texture2D
```

x.get_thumbnail() -> Texture2D
获取预制体资产缩略图

Returns:
    Texture2D:

<a id="unreal.EarthPrefabAsset.get_prefab_recursive"></a>

#### get\_prefab\_recursive

```python
def get_prefab_recursive(
        asset_owner: Object) -> Tuple[InstancedStruct, Array[Object]]
```

x.get_prefab_recursive(asset_owner) -> (out_prefab=InstancedStruct, visited=Array[Object])
获取合并了模板预制体的预制体数据

Args:
    asset_owner (Object): 

Returns:
    tuple: 

    out_prefab (InstancedStruct): 

    visited (Array[Object]):

<a id="unreal.EarthPrefabAsset.get_prefab_internal"></a>

#### get\_prefab\_internal

```python
def get_prefab_internal() -> InstancedStruct
```

x.get_prefab_internal() -> InstancedStruct
获取合并了模板预制体的预制体数据

Returns:
    InstancedStruct: 

    out_prefab (InstancedStruct):

<a id="unreal.EarthPrefabAsset.get_prefab_data"></a>

#### get\_prefab\_data

```python
def get_prefab_data() -> EarthPrefabBase
```

x.get_prefab_data() -> EarthPrefabBase
获取预制体数据

Returns:
    EarthPrefabBase:

<a id="unreal.EarthPrefabAsset.get_prefab"></a>

#### get\_prefab

```python
def get_prefab() -> InstancedStruct
```

x.get_prefab() -> InstancedStruct
获取预制体

Returns:
    InstancedStruct:

<a id="unreal.EarthPrefabAsset.get_output_collection_mutable"></a>

#### get\_output\_collection\_mutable

```python
def get_output_collection_mutable() -> EarthOutputCollection
```

x.get_output_collection_mutable() -> EarthOutputCollection
获取可修改的输出数据集合

Returns:
    EarthOutputCollection:

<a id="unreal.EarthPrefabAsset.get_output_collection"></a>

#### get\_output\_collection

```python
def get_output_collection() -> EarthOutputCollection
```

x.get_output_collection() -> EarthOutputCollection
获取输出数据集合

Returns:
    EarthOutputCollection:

<a id="unreal.EarthPrefabAsset.get_input_collection_mutable"></a>

#### get\_input\_collection\_mutable

```python
def get_input_collection_mutable() -> EarthInputCollection
```

x.get_input_collection_mutable() -> EarthInputCollection
获取可修改的输入数据集合

Returns:
    EarthInputCollection:

<a id="unreal.EarthPrefabAsset.get_input_collection"></a>

#### get\_input\_collection

```python
def get_input_collection() -> EarthInputCollection
```

x.get_input_collection() -> EarthInputCollection
获取输入数据集合

Returns:
    EarthInputCollection:

<a id="unreal.EarthPrefabAsset.get_bounds"></a>

#### get\_bounds

```python
def get_bounds() -> Box
```

x.get_bounds() -> Box
获取包围盒大小

Returns:
    Box:

<a id="unreal.EarthPrefabAsset.get_algorithm"></a>

#### get\_algorithm

```python
def get_algorithm() -> Class
```

x.get_algorithm() -> type(Class)
获取算法类

Returns:
    type(Class):

<a id="unreal.EarthPrefabAsset.execute_algorithm"></a>

#### execute\_algorithm

```python
def execute_algorithm() -> None
```

x.execute_algorithm() -> None
执行算法

<a id="unreal.EarthPrefabAsset.clear_output_collection"></a>

#### clear\_output\_collection

```python
def clear_output_collection() -> None
```

x.clear_output_collection() -> None
清空输出数据集合

<a id="unreal.EarthPrefabAsset.clear_input_collection"></a>

#### clear\_input\_collection

```python
def clear_input_collection() -> None
```

x.clear_input_collection() -> None
清空输入数据集合

<a id="unreal.EarthModuleAsset"></a>