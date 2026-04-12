## EarthRoadModelerLanePrefabAlgorithm Objects

```python
class EarthRoadModelerLanePrefabAlgorithm(EarthPrefabAlgorithm)
```

Earth Road Modeler Lane Prefab Algorithm

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadModelerLanePrefab.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``required_fragments`` (Array[ScriptStruct]):  [Read-Write] 算法所需的数据片段类型

<a id="unreal.EarthRoadModelerLanePrefabAlgorithm.build_by_template"></a>

#### build\_by\_template

```python
@classmethod
def build_by_template(cls, actor: Actor, template_asset_path: SoftObjectPath,
                      static_mesh: StaticMesh,
                      target_folder_path: str) -> None
```

X.build_by_template(actor, template_asset_path, static_mesh, target_folder_path) -> None
根据模板资产路径创建新的 RoadModelerLane Prefab 并使用指定的 StaticMesh 资产

Args:
    actor (Actor): 用于加载资产的外部对象
    template_asset_path (SoftObjectPath): 车道模板资产路径
    static_mesh (StaticMesh): 要使用的 StaticMesh 资产（必须有效）
    target_folder_path (str): 新 PrefabAsset 的保存路径（支持：/Game/Path, 相对路径, 或绝对路径）

<a id="unreal.EarthRoadModelerPrefabAlgorithm"></a>