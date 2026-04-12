## DataRegistryCachePolicy Objects

```python
class DataRegistryCachePolicy(StructBase)
```

Rules to use when deciding how to unload registry items and related assets

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: DataRegistryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_is_always_volatile`` (bool):  [Read-Write] If this is true, the cache is always considered volatile when returning EDataRegistryCacheResult
- ``force_keep_seconds`` (float):  [Read-Write] Any item accessed within this amount of seconds is never unloaded
- ``force_release_seconds`` (float):  [Read-Write] Any item not accessed within this amount of seconds is always unloaded
- ``max_number_kept`` (int32):  [Read-Write] Maximum number of items to keep loaded, 0 means infinite
- ``min_number_kept`` (int32):  [Read-Write] Will not release items if fewer then this number loaded, 0 means infinite
- ``use_curve_table_cache_version`` (bool):  [Read-Write] If this is true, the cache version is synchronized with the global CurveTable cache version

<a id="unreal.DataRegistryCachePolicy.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cache_is_always_volatile: bool = False,
             use_curve_table_cache_version: bool = False,
             min_number_kept: int = 0,
             max_number_kept: int = 0,
             force_keep_seconds: float = 0.000000,
             force_release_seconds: float = 0.000000) -> None
```

<a id="unreal.DataRegistryCachePolicy.cache_is_always_volatile"></a>

#### cache\_is\_always\_volatile

```python
@property
def cache_is_always_volatile() -> bool
```

(bool):  [Read-Write] If this is true, the cache is always considered volatile when returning EDataRegistryCacheResult

<a id="unreal.DataRegistryCachePolicy.cache_is_always_volatile"></a>

#### cache\_is\_always\_volatile

```python
@cache_is_always_volatile.setter
def cache_is_always_volatile(value: bool) -> None
```

<a id="unreal.DataRegistryCachePolicy.use_curve_table_cache_version"></a>

#### use\_curve\_table\_cache\_version

```python
@property
def use_curve_table_cache_version() -> bool
```

(bool):  [Read-Write] If this is true, the cache version is synchronized with the global CurveTable cache version

<a id="unreal.DataRegistryCachePolicy.use_curve_table_cache_version"></a>

#### use\_curve\_table\_cache\_version

```python
@use_curve_table_cache_version.setter
def use_curve_table_cache_version(value: bool) -> None
```

<a id="unreal.DataRegistryCachePolicy.min_number_kept"></a>

#### min\_number\_kept

```python
@property
def min_number_kept() -> int
```

(int32):  [Read-Write] Will not release items if fewer then this number loaded, 0 means infinite

<a id="unreal.DataRegistryCachePolicy.min_number_kept"></a>

#### min\_number\_kept

```python
@min_number_kept.setter
def min_number_kept(value: int) -> None
```

<a id="unreal.DataRegistryCachePolicy.max_number_kept"></a>

#### max\_number\_kept

```python
@property
def max_number_kept() -> int
```

(int32):  [Read-Write] Maximum number of items to keep loaded, 0 means infinite

<a id="unreal.DataRegistryCachePolicy.max_number_kept"></a>

#### max\_number\_kept

```python
@max_number_kept.setter
def max_number_kept(value: int) -> None
```

<a id="unreal.DataRegistryCachePolicy.force_keep_seconds"></a>

#### force\_keep\_seconds

```python
@property
def force_keep_seconds() -> float
```

(float):  [Read-Write] Any item accessed within this amount of seconds is never unloaded

<a id="unreal.DataRegistryCachePolicy.force_keep_seconds"></a>

#### force\_keep\_seconds

```python
@force_keep_seconds.setter
def force_keep_seconds(value: float) -> None
```

<a id="unreal.DataRegistryCachePolicy.force_release_seconds"></a>

#### force\_release\_seconds

```python
@property
def force_release_seconds() -> float
```

(float):  [Read-Write] Any item not accessed within this amount of seconds is always unloaded

<a id="unreal.DataRegistryCachePolicy.force_release_seconds"></a>

#### force\_release\_seconds

```python
@force_release_seconds.setter
def force_release_seconds(value: float) -> None
```

<a id="unreal.DataRegistryOrTableRow"></a>