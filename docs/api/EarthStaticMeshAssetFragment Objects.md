## EarthStaticMeshAssetFragment Objects

```python
class EarthStaticMeshAssetFragment(EarthPropertyFragment)
```

定义静态网格体资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``static_mesh`` (StaticMesh):  [Read-Write] 静态网格体资产引用
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthStaticMeshAssetFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             static_mesh: StaticMesh = None) -> None
```

<a id="unreal.EarthStaticMeshAssetFragment.static_mesh"></a>

#### static\_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] 静态网格体资产引用

<a id="unreal.EarthStaticMeshAssetFragment.static_mesh"></a>

#### static\_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.EarthMeshReplacementFragment"></a>