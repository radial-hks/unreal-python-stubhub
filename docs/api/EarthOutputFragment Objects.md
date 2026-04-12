## EarthOutputFragment Objects

```python
class EarthOutputFragment(EarthFragment)
```

输出片段基类：定义预制体生成的最终产物
可被其他系统消费（如渲染系统或游戏玩法系统）
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthOutputFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None) -> None
```

<a id="unreal.EarthOutputFragment.owned_object"></a>

#### owned\_object

```python
@property
def owned_object() -> Object
```

(Object):  [Read-Write] 输出片段所拥有的组件

<a id="unreal.EarthOutputFragment.owned_object"></a>

#### owned\_object

```python
@owned_object.setter
def owned_object(value: Object) -> None
```

<a id="unreal.EarthGuidFragment"></a>