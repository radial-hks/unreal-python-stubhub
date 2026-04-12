## EarthFlatRoofFragment Objects

```python
class EarthFlatRoofFragment(EarthRoofBaseFragment)
```

定义平屋顶数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoofFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 屋顶颜色
- ``enable_lot_subdivision`` (bool):  [Read-Write] 是否使用地块分割法分割屋顶
- ``irregularity`` (float):  [Read-Write] 分割的不规则度，较小的值意味着分割会在一个片元的中点进行，较大的值则会产生大小不同的片元
- ``iterations`` (int32):  [Read-Write] 分割细分次数，1次会生成2个片元，2次会生成4个片元，以此类推
- ``minimum_lot_size`` (float):  [Read-Write] 小于此尺寸的片元将不再被分割，单位为平方米
- ``over_hang`` (float):  [Read-Write] 挑檐长度
- ``roof_material`` (EarthMaterialInfo):  [Read-Write] 屋顶材质
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFlatRoofFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             over_hang: float = 0.000000,
             roof_material: EarthMaterialInfo = [
                 "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000,
                 [0, 0]
             ],
             enable_lot_subdivision: bool = False,
             iterations: int = 0,
             minimum_lot_size: float = 0.000000,
             irregularity: float = 0.000000) -> None
```

<a id="unreal.EarthFlatRoofFragment.enable_lot_subdivision"></a>

#### enable\_lot\_subdivision

```python
@property
def enable_lot_subdivision() -> bool
```

(bool):  [Read-Write] 是否使用地块分割法分割屋顶

<a id="unreal.EarthFlatRoofFragment.enable_lot_subdivision"></a>

#### enable\_lot\_subdivision

```python
@enable_lot_subdivision.setter
def enable_lot_subdivision(value: bool) -> None
```

<a id="unreal.EarthFlatRoofFragment.iterations"></a>

#### iterations

```python
@property
def iterations() -> int
```

(int32):  [Read-Write] 分割细分次数，1次会生成2个片元，2次会生成4个片元，以此类推

<a id="unreal.EarthFlatRoofFragment.iterations"></a>

#### iterations

```python
@iterations.setter
def iterations(value: int) -> None
```

<a id="unreal.EarthFlatRoofFragment.minimum_lot_size"></a>

#### minimum\_lot\_size

```python
@property
def minimum_lot_size() -> float
```

(float):  [Read-Write] 小于此尺寸的片元将不再被分割，单位为平方米

<a id="unreal.EarthFlatRoofFragment.minimum_lot_size"></a>

#### minimum\_lot\_size

```python
@minimum_lot_size.setter
def minimum_lot_size(value: float) -> None
```

<a id="unreal.EarthFlatRoofFragment.irregularity"></a>

#### irregularity

```python
@property
def irregularity() -> float
```

(float):  [Read-Write] 分割的不规则度，较小的值意味着分割会在一个片元的中点进行，较大的值则会产生大小不同的片元

<a id="unreal.EarthFlatRoofFragment.irregularity"></a>

#### irregularity

```python
@irregularity.setter
def irregularity(value: float) -> None
```

<a id="unreal.EarthHipRoofFragment"></a>