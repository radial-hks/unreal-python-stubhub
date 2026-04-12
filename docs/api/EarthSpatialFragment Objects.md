## EarthSpatialFragment Objects

```python
class EarthSpatialFragment(EarthFragment)
```

空间片段基类：定义预制体的几何形状或空间布局，可关联矢量、点云、栅格等数据
一般由外部数据传入，如果是静态预制体资产，则会存储一份在预制体资产中
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthSpatialFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_component: ActorComponent = None) -> None
```

<a id="unreal.EarthSpatialFragment.owned_component"></a>

#### owned\_component

```python
@property
def owned_component() -> ActorComponent
```

(ActorComponent):  [Read-Write] 空间片段所拥有的组件

<a id="unreal.EarthSpatialFragment.owned_component"></a>

#### owned\_component

```python
@owned_component.setter
def owned_component(value: ActorComponent) -> None
```

<a id="unreal.EarthExtensionFragment"></a>