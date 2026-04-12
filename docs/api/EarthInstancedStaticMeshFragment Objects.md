## EarthInstancedStaticMeshFragment Objects

```python
class EarthInstancedStaticMeshFragment(EarthOutputFragment)
```

定义实例化静态网格体数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInstancedStaticMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 包围盒片段
- ``component_class`` (Class):  [Read-Write] 组件类引用
- ``custom_data_attributes`` (Map[Name, float]):  [Read-Write] 实例自定义数据模板
- ``instance_transforms`` (Array[Matrix]):  [Read-Write] 实例变换数组
- ``material_fragment`` (EarthMaterialFragment):  [Read-Write] 材质片段
- ``mesh_bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 静态网格体资产的包围盒
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``per_instance_sm_custom_data`` (Array[float]):  [Read-Write] 实例自定义数据
- ``primitive_data_fragment`` (EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段
- ``static_mesh`` (StaticMesh):  [Read-Write] 静态网格体资产引用
- ``tag_fragment`` (EarthTagFragment):  [Read-Write] 标签片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthInstancedStaticMeshFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             static_mesh: StaticMesh = None,
             mesh_bounds_fragment: EarthBoundsFragment = [
                 False,
                 [[0.000000, 0.000000, 0.000000],
                  [0.000000, 0.000000, 0.000000], False], False, False
             ],
             component_class: Class = None,
             instance_transforms: Array[Matrix] = [],
             custom_data_attributes: Map[Name, float] = {},
             per_instance_sm_custom_data: Array[float] = [],
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

<a id="unreal.EarthInstancedStaticMeshFragment.static_mesh"></a>

#### static\_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] 静态网格体资产引用

<a id="unreal.EarthInstancedStaticMeshFragment.static_mesh"></a>

#### static\_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.mesh_bounds_fragment"></a>

#### mesh\_bounds\_fragment

```python
@property
def mesh_bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 静态网格体资产的包围盒

<a id="unreal.EarthInstancedStaticMeshFragment.mesh_bounds_fragment"></a>

#### mesh\_bounds\_fragment

```python
@mesh_bounds_fragment.setter
def mesh_bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.component_class"></a>

#### component\_class

```python
@property
def component_class() -> Class
```

(Class):  [Read-Write] 组件类引用

<a id="unreal.EarthInstancedStaticMeshFragment.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: Class) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.instance_transforms"></a>

#### instance\_transforms

```python
@property
def instance_transforms() -> Array[Matrix]
```

(Array[Matrix]):  [Read-Write] 实例变换数组

<a id="unreal.EarthInstancedStaticMeshFragment.instance_transforms"></a>

#### instance\_transforms

```python
@instance_transforms.setter
def instance_transforms(value: Array[Matrix]) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.custom_data_attributes"></a>

#### custom\_data\_attributes

```python
@property
def custom_data_attributes() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 实例自定义数据模板

<a id="unreal.EarthInstancedStaticMeshFragment.custom_data_attributes"></a>

#### custom\_data\_attributes

```python
@custom_data_attributes.setter
def custom_data_attributes(value: Map[Name, float]) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.per_instance_sm_custom_data"></a>

#### per\_instance\_sm\_custom\_data

```python
@property
def per_instance_sm_custom_data() -> Array[float]
```

(Array[float]):  [Read-Write] 实例自定义数据

<a id="unreal.EarthInstancedStaticMeshFragment.per_instance_sm_custom_data"></a>

#### per\_instance\_sm\_custom\_data

```python
@per_instance_sm_custom_data.setter
def per_instance_sm_custom_data(value: Array[float]) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@property
def material_fragment() -> EarthMaterialFragment
```

(EarthMaterialFragment):  [Read-Write] 材质片段

<a id="unreal.EarthInstancedStaticMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@material_fragment.setter
def material_fragment(value: EarthMaterialFragment) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@property
def primitive_data_fragment() -> EarthPrimitiveDataFragment
```

(EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段

<a id="unreal.EarthInstancedStaticMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@primitive_data_fragment.setter
def primitive_data_fragment(value: EarthPrimitiveDataFragment) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@property
def bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 包围盒片段

<a id="unreal.EarthInstancedStaticMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@bounds_fragment.setter
def bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@property
def tag_fragment() -> EarthTagFragment
```

(EarthTagFragment):  [Read-Write] 标签片段

<a id="unreal.EarthInstancedStaticMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@tag_fragment.setter
def tag_fragment(value: EarthTagFragment) -> None
```

<a id="unreal.EarthInstanceSplinePrefab"></a>