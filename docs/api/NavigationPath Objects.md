## NavigationPath Objects

```python
class NavigationPath(Object)
```

UObject wrapper for FNavigationPath

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavigationPath.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``path_points`` (Array[Vector]):  [Read-Write]
- ``path_updated_notifier`` (OnNavigationPathUpdated):  [Read-Write]
- ``recalculate_on_invalidation`` (NavigationOptionFlag):  [Read-Write]

<a id="unreal.NavigationPath.path_updated_notifier"></a>

#### path_updated_notifier

```python
@property
def path_updated_notifier() -> OnNavigationPathUpdated
```

(OnNavigationPathUpdated):  [Read-Write]

<a id="unreal.NavigationPath.path_updated_notifier"></a>

#### path_updated_notifier

```python
@path_updated_notifier.setter
def path_updated_notifier(value: OnNavigationPathUpdated) -> None
```

<a id="unreal.NavigationPath.path_points"></a>

#### path_points

```python
@property
def path_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.NavigationPath.recalculate_on_invalidation"></a>

#### recalculate_on_invalidation

```python
@property
def recalculate_on_invalidation() -> NavigationOptionFlag
```

(NavigationOptionFlag):  [Read-Only]

<a id="unreal.NavigationPath.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Is Valid

Returns:
    bool:

<a id="unreal.NavigationPath.is_string_pulled"></a>

#### is_string_pulled

```python
def is_string_pulled() -> bool
```

x.is_string_pulled() -> bool
Is String Pulled

Returns:
    bool:

<a id="unreal.NavigationPath.is_partial"></a>

#### is_partial

```python
def is_partial() -> bool
```

x.is_partial() -> bool
Is Partial

Returns:
    bool:

<a id="unreal.NavigationPath.get_path_length"></a>

#### get_path_length

```python
def get_path_length() -> float
```

x.get_path_length() -> double
Get Path Length

Returns:
    double:

<a id="unreal.NavigationPath.get_path_lenght"></a>

#### get_path_lenght

```python
def get_path_lenght() -> float
```

deprecated: 'get_path_lenght' was renamed to 'get_path_length'.

<a id="unreal.NavigationPath.get_path_cost"></a>

#### get_path_cost

```python
def get_path_cost() -> float
```

x.get_path_cost() -> double
Get Path Cost

Returns:
    double:

<a id="unreal.NavigationPath.get_debug_string"></a>

#### get_debug_string

```python
def get_debug_string() -> str
```

x.get_debug_string() -> str
UObject end

Returns:
    str:

<a id="unreal.NavigationPath.enable_recalculation_on_invalidation"></a>

#### enable_recalculation_on_invalidation

```python
def enable_recalculation_on_invalidation(
        do_recalculation: NavigationOptionFlag) -> None
```

x.enable_recalculation_on_invalidation(do_recalculation) -> None
if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

Args:
    do_recalculation (NavigationOptionFlag):

<a id="unreal.NavigationPath.enable_debug_drawing"></a>

#### enable_debug_drawing

```python
def enable_debug_drawing(
    should_draw_debug_data: bool,
    path_color: LinearColor = [1.000000, 1.000000, 1.000000,
                               1.000000]) -> None
```

x.enable_debug_drawing(should_draw_debug_data, path_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Enable Debug Drawing

Args:
    should_draw_debug_data (bool): 
    path_color (LinearColor):

<a id="unreal.World"></a>