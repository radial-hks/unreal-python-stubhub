## EarthStaticMeshFragment Objects

```python
class EarthStaticMeshFragment(EarthOutputFragment)
```

定义动态网格体数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthStaticMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 包围盒片段
- ``component_class`` (Class):  [Read-Write] 组件类引用
- ``lod_feature_buffer`` (Array[EarthFeatureBuffer]):  [Read-Only] 要素缓冲区
- ``material_fragment`` (EarthMaterialFragment):  [Read-Write] 材质片段
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``primitive_data_fragment`` (EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段
- ``static_mesh`` (StaticMesh):  [Read-Write] TODO: 将类型改为 TSoftObjectPtr<UStaticMesh>
  静态网格体资产引用
- ``tag_fragment`` (EarthTagFragment):  [Read-Write] 标签片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthStaticMeshFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             static_mesh: StaticMesh = None,
             component_class: Class = None,
             lod_feature_buffer: Array[EarthFeatureBuffer] = [],
             material_fragment: EarthMaterialFragment = [[], None, [], False,
                                                         False],
             primitive_data_fragment: EarthPrimitiveDataFragment = [{}, False,
                                                                    False],
             bounds_fragment: EarthBoundsFragment = [
                 False,
                 [[0.000000, 0.000000, 0.000000],
                  [0.000000, 0.000000, 0.000000], False], False, False
             ],
             tag_fragment: EarthTagFragment = [[], False, False]) -> None
```

<a id="unreal.EarthStaticMeshFragment.static_mesh"></a>

#### static\_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] TODO: 将类型改为 TSoftObjectPtr<UStaticMesh>
静态网格体资产引用

<a id="unreal.EarthStaticMeshFragment.static_mesh"></a>

#### static\_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.EarthStaticMeshFragment.component_class"></a>

#### component\_class

```python
@property
def component_class() -> Class
```

(Class):  [Read-Write] 组件类引用

<a id="unreal.EarthStaticMeshFragment.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: Class) -> None
```

<a id="unreal.EarthStaticMeshFragment.lod_feature_buffer"></a>

#### lod\_feature\_buffer

```python
@property
def lod_feature_buffer() -> Array[EarthFeatureBuffer]
```

(Array[EarthFeatureBuffer]):  [Read-Only] 要素缓冲区

<a id="unreal.EarthStaticMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@property
def material_fragment() -> EarthMaterialFragment
```

(EarthMaterialFragment):  [Read-Write] 材质片段

<a id="unreal.EarthStaticMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@material_fragment.setter
def material_fragment(value: EarthMaterialFragment) -> None
```

<a id="unreal.EarthStaticMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@property
def primitive_data_fragment() -> EarthPrimitiveDataFragment
```

(EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段

<a id="unreal.EarthStaticMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@primitive_data_fragment.setter
def primitive_data_fragment(value: EarthPrimitiveDataFragment) -> None
```

<a id="unreal.EarthStaticMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@property
def bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 包围盒片段

<a id="unreal.EarthStaticMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@bounds_fragment.setter
def bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthStaticMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@property
def tag_fragment() -> EarthTagFragment
```

(EarthTagFragment):  [Read-Write] 标签片段

<a id="unreal.EarthStaticMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@tag_fragment.setter
def tag_fragment(value: EarthTagFragment) -> None
```

<a id="unreal.EarthStaticMeshPrefab"></a>