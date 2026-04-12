## EarthLODFragment Objects

```python
class EarthLODFragment(EarthExternalFragment)
```

定义细节级别片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lod`` (int32):  [Read-Write] 当前细节级别
- ``lod_max`` (int32):  [Read-Write] 最大细节级别
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthLODFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             lod: int = 0,
             lod_max: int = 0) -> None
```

<a id="unreal.EarthLODFragment.lod"></a>

#### lod

```python
@property
def lod() -> int
```

(int32):  [Read-Write] 当前细节级别

<a id="unreal.EarthLODFragment.lod"></a>

#### lod

```python
@lod.setter
def lod(value: int) -> None
```

<a id="unreal.EarthLODFragment.lod_max"></a>

#### lod\_max

```python
@property
def lod_max() -> int
```

(int32):  [Read-Write] 最大细节级别

<a id="unreal.EarthLODFragment.lod_max"></a>

#### lod\_max

```python
@lod_max.setter
def lod_max(value: int) -> None
```

<a id="unreal.EarthColorFragment"></a>