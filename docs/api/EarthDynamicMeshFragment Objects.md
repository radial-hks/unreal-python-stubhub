## EarthDynamicMeshFragment Objects

```python
class EarthDynamicMeshFragment(EarthOutputFragment)
```

定义动态网格体数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthDynamicMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 包围盒片段
- ``component_class`` (Class):  [Read-Write] 组件类引用
- ``feature_buffer`` (EarthFeatureBuffer):  [Read-Only] 要素缓冲区
- ``material_fragment`` (EarthMaterialFragment):  [Read-Write] 材质片段
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``primitive_data_fragment`` (EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段
- ``tag_fragment`` (EarthTagFragment):  [Read-Write] 标签片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthDynamicMeshFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             component_class: Class = None,
             feature_buffer: EarthFeatureBuffer = [[]],
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

<a id="unreal.EarthDynamicMeshFragment.component_class"></a>

#### component\_class

```python
@property
def component_class() -> Class
```

(Class):  [Read-Write] 组件类引用

<a id="unreal.EarthDynamicMeshFragment.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: Class) -> None
```

<a id="unreal.EarthDynamicMeshFragment.feature_buffer"></a>

#### feature\_buffer

```python
@property
def feature_buffer() -> EarthFeatureBuffer
```

(EarthFeatureBuffer):  [Read-Only] 要素缓冲区

<a id="unreal.EarthDynamicMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@property
def material_fragment() -> EarthMaterialFragment
```

(EarthMaterialFragment):  [Read-Write] 材质片段

<a id="unreal.EarthDynamicMeshFragment.material_fragment"></a>

#### material\_fragment

```python
@material_fragment.setter
def material_fragment(value: EarthMaterialFragment) -> None
```

<a id="unreal.EarthDynamicMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@property
def primitive_data_fragment() -> EarthPrimitiveDataFragment
```

(EarthPrimitiveDataFragment):  [Read-Write] 图元数据片段

<a id="unreal.EarthDynamicMeshFragment.primitive_data_fragment"></a>

#### primitive\_data\_fragment

```python
@primitive_data_fragment.setter
def primitive_data_fragment(value: EarthPrimitiveDataFragment) -> None
```

<a id="unreal.EarthDynamicMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@property
def bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 包围盒片段

<a id="unreal.EarthDynamicMeshFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@bounds_fragment.setter
def bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthDynamicMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@property
def tag_fragment() -> EarthTagFragment
```

(EarthTagFragment):  [Read-Write] 标签片段

<a id="unreal.EarthDynamicMeshFragment.tag_fragment"></a>

#### tag\_fragment

```python
@tag_fragment.setter
def tag_fragment(value: EarthTagFragment) -> None
```

<a id="unreal.EarthDynamicMeshPrefab"></a>