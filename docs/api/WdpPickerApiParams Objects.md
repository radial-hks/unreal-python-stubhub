## WdpPickerApiParams Objects

```python
class WdpPickerApiParams(ParamsBase)
```

Wdp Picker Api Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_type_filter`` (Set[str]):  [Read-Write]
- ``filter_for_exclude`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``screen_pos`` (Vector2D):  [Read-Write]

<a id="unreal.WdpPickerApiParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(screen_pos: Vector2D = [0.000000, 0.000000],
             entity_type_filter: Set[str] = [],
             filter_for_exclude: bool = False) -> None
```

<a id="unreal.WdpPickerApiParams.screen_pos"></a>

#### screen\_pos

```python
@property
def screen_pos() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpPickerApiParams.screen_pos"></a>

#### screen\_pos

```python
@screen_pos.setter
def screen_pos(value: Vector2D) -> None
```

<a id="unreal.WdpPickerApiParams.entity_type_filter"></a>

#### entity\_type\_filter

```python
@property
def entity_type_filter() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.WdpPickerApiParams.entity_type_filter"></a>

#### entity\_type\_filter

```python
@entity_type_filter.setter
def entity_type_filter(value: Set[str]) -> None
```

<a id="unreal.WdpPickerApiParams.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@property
def filter_for_exclude() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpPickerApiParams.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@filter_for_exclude.setter
def filter_for_exclude(value: bool) -> None
```

<a id="unreal.WdpRectPickerApiParams"></a>