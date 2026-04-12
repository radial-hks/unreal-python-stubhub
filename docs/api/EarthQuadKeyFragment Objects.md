## EarthQuadKeyFragment Objects

```python
class EarthQuadKeyFragment(EarthSpatialFragment)
```

QuadKey数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``quad_key`` (str):  [Read-Write] QuadKey数据
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthQuadKeyFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_component: ActorComponent = None,
             quad_key: str = "") -> None
```

<a id="unreal.EarthQuadKeyFragment.quad_key"></a>

#### quad\_key

```python
@property
def quad_key() -> str
```

(str):  [Read-Write] QuadKey数据

<a id="unreal.EarthQuadKeyFragment.quad_key"></a>

#### quad\_key

```python
@quad_key.setter
def quad_key(value: str) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset"></a>