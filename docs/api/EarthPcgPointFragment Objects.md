## EarthPcgPointFragment Objects

```python
class EarthPcgPointFragment(EarthSpatialFragment)
```

Earth Pcg Point Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box):  [Read-Write]
- ``colors`` (Array[Vector4]):  [Read-Write]
- ``height`` (int32):  [Read-Write]
- ``lcg`` (Array[double]):  [Read-Write]
- ``normals`` (Array[Vector]):  [Read-Write]
- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``positions`` (Array[Vector]):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``vgm`` (Array[double]):  [Read-Write]
- ``with_`` (int32):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    owned_component: ActorComponent = None,
    with_: int = 0,
    height: int = 0,
    positions: Array[Vector] = [],
    normals: Array[Vector] = [],
    colors: Array[Vector4] = [],
    vgm: Array[float] = [],
    lcg: Array[float] = [],
    bounds: Box = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.EarthPcgPointFragment.with_"></a>

#### with\_

```python
@property
def with_() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.with_"></a>

#### with\_

```python
@with_.setter
def with_(value: int) -> None
```

<a id="unreal.EarthPcgPointFragment.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.EarthPcgPointFragment.positions"></a>

#### positions

```python
@property
def positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.positions"></a>

#### positions

```python
@positions.setter
def positions(value: Array[Vector]) -> None
```

<a id="unreal.EarthPcgPointFragment.normals"></a>

#### normals

```python
@property
def normals() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.normals"></a>

#### normals

```python
@normals.setter
def normals(value: Array[Vector]) -> None
```

<a id="unreal.EarthPcgPointFragment.colors"></a>

#### colors

```python
@property
def colors() -> Array[Vector4]
```

(Array[Vector4]):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.colors"></a>

#### colors

```python
@colors.setter
def colors(value: Array[Vector4]) -> None
```

<a id="unreal.EarthPcgPointFragment.vgm"></a>

#### vgm

```python
@property
def vgm() -> Array[float]
```

(Array[double]):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.vgm"></a>

#### vgm

```python
@vgm.setter
def vgm(value: Array[float]) -> None
```

<a id="unreal.EarthPcgPointFragment.lcg"></a>

#### lcg

```python
@property
def lcg() -> Array[float]
```

(Array[double]):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.lcg"></a>

#### lcg

```python
@lcg.setter
def lcg(value: Array[float]) -> None
```

<a id="unreal.EarthPcgPointFragment.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box
```

(Box):  [Read-Write]

<a id="unreal.EarthPcgPointFragment.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box) -> None
```

<a id="unreal.EarthSpatialPrefab"></a>