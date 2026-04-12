## EarthCollisionFragment Objects

```python
class EarthCollisionFragment(EarthOutputFragment)
```

定义碰撞数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCollisionFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 包围盒片段
- ``collision_type`` (EarthCollisionType):  [Read-Write] 碰撞创建类型
- ``complex_collision`` (bool):  [Read-Write] 是否使用静态网格体资产的复杂碰撞
- ``component_class`` (Class):  [Read-Write] 碰撞组件类引用
- ``has_cap`` (bool):  [Read-Write] 包围盒是否有封顶
- ``index_buffer`` (Array[int32]):  [Read-Write] 索引缓冲区
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``tag_fragment`` (EarthTagFragment):  [Read-Write] 标签片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``vertex_buffer`` (Array[Vector3f]):  [Read-Write] 顶点缓冲区

<a id="unreal.EarthCollisionFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             collision_type: EarthCollisionType = EarthCollisionType.NONE,
             complex_collision: bool = False,
             has_cap: bool = False,
             component_class: Class = None,
             vertex_buffer: Array[Vector3f] = [],
             index_buffer: Array[int] = [],
             bounds_fragment: EarthBoundsFragment = [
                 False,
                 [[0.000000, 0.000000, 0.000000],
                  [0.000000, 0.000000, 0.000000], False], False, False
             ],
             tag_fragment: EarthTagFragment = [[], False, False]) -> None
```

<a id="unreal.EarthCollisionFragment.collision_type"></a>

#### collision\_type

```python
@property
def collision_type() -> EarthCollisionType
```

(EarthCollisionType):  [Read-Write] 碰撞创建类型

<a id="unreal.EarthCollisionFragment.collision_type"></a>

#### collision\_type

```python
@collision_type.setter
def collision_type(value: EarthCollisionType) -> None
```

<a id="unreal.EarthCollisionFragment.complex_collision"></a>

#### complex\_collision

```python
@property
def complex_collision() -> bool
```

(bool):  [Read-Write] 是否使用静态网格体资产的复杂碰撞

<a id="unreal.EarthCollisionFragment.complex_collision"></a>

#### complex\_collision

```python
@complex_collision.setter
def complex_collision(value: bool) -> None
```

<a id="unreal.EarthCollisionFragment.has_cap"></a>

#### has\_cap

```python
@property
def has_cap() -> bool
```

(bool):  [Read-Write] 包围盒是否有封顶

<a id="unreal.EarthCollisionFragment.has_cap"></a>

#### has\_cap

```python
@has_cap.setter
def has_cap(value: bool) -> None
```

<a id="unreal.EarthCollisionFragment.component_class"></a>

#### component\_class

```python
@property
def component_class() -> Class
```

(Class):  [Read-Write] 碰撞组件类引用

<a id="unreal.EarthCollisionFragment.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: Class) -> None
```

<a id="unreal.EarthCollisionFragment.vertex_buffer"></a>

#### vertex\_buffer

```python
@property
def vertex_buffer() -> Array[Vector3f]
```

(Array[Vector3f]):  [Read-Write] 顶点缓冲区

<a id="unreal.EarthCollisionFragment.vertex_buffer"></a>

#### vertex\_buffer

```python
@vertex_buffer.setter
def vertex_buffer(value: Array[Vector3f]) -> None
```

<a id="unreal.EarthCollisionFragment.index_buffer"></a>

#### index\_buffer

```python
@property
def index_buffer() -> Array[int]
```

(Array[int32]):  [Read-Write] 索引缓冲区

<a id="unreal.EarthCollisionFragment.index_buffer"></a>

#### index\_buffer

```python
@index_buffer.setter
def index_buffer(value: Array[int]) -> None
```

<a id="unreal.EarthCollisionFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@property
def bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 包围盒片段

<a id="unreal.EarthCollisionFragment.bounds_fragment"></a>

#### bounds\_fragment

```python
@bounds_fragment.setter
def bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthCollisionFragment.tag_fragment"></a>

#### tag\_fragment

```python
@property
def tag_fragment() -> EarthTagFragment
```

(EarthTagFragment):  [Read-Write] 标签片段

<a id="unreal.EarthCollisionFragment.tag_fragment"></a>

#### tag\_fragment

```python
@tag_fragment.setter
def tag_fragment(value: EarthTagFragment) -> None
```

<a id="unreal.EarthTagFragment"></a>