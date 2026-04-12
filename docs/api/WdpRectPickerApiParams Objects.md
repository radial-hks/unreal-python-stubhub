## WdpRectPickerApiParams Objects

```python
class WdpRectPickerApiParams(ParamsBase)
```

Wdp Rect Picker Api Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_type_filter`` (Set[str]):  [Read-Write]
- ``filter_for_exclude`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``must_be_fully_enclosed`` (bool):  [Read-Write]
- ``p0`` (Vector2D):  [Read-Write]
- ``p1`` (Vector2D):  [Read-Write]
- ``select_mode`` (WdpSelectionMode):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(p0: Vector2D = [0.000000, 0.000000],
             p1: Vector2D = [0.000000, 0.000000],
             must_be_fully_enclosed: bool = False,
             entity_type_filter: Set[str] = [],
             filter_for_exclude: bool = False,
             select_mode: WdpSelectionMode = WdpSelectionMode.NONE) -> None
```

<a id="unreal.WdpRectPickerApiParams.p0"></a>

#### p0

```python
@property
def p0() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.p0"></a>

#### p0

```python
@p0.setter
def p0(value: Vector2D) -> None
```

<a id="unreal.WdpRectPickerApiParams.p1"></a>

#### p1

```python
@property
def p1() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.p1"></a>

#### p1

```python
@p1.setter
def p1(value: Vector2D) -> None
```

<a id="unreal.WdpRectPickerApiParams.must_be_fully_enclosed"></a>

#### must\_be\_fully\_enclosed

```python
@property
def must_be_fully_enclosed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.must_be_fully_enclosed"></a>

#### must\_be\_fully\_enclosed

```python
@must_be_fully_enclosed.setter
def must_be_fully_enclosed(value: bool) -> None
```

<a id="unreal.WdpRectPickerApiParams.entity_type_filter"></a>

#### entity\_type\_filter

```python
@property
def entity_type_filter() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.entity_type_filter"></a>

#### entity\_type\_filter

```python
@entity_type_filter.setter
def entity_type_filter(value: Set[str]) -> None
```

<a id="unreal.WdpRectPickerApiParams.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@property
def filter_for_exclude() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@filter_for_exclude.setter
def filter_for_exclude(value: bool) -> None
```

<a id="unreal.WdpRectPickerApiParams.select_mode"></a>

#### select\_mode

```python
@property
def select_mode() -> WdpSelectionMode
```

(WdpSelectionMode):  [Read-Write]

<a id="unreal.WdpRectPickerApiParams.select_mode"></a>

#### select\_mode

```python
@select_mode.setter
def select_mode(value: WdpSelectionMode) -> None
```

<a id="unreal.GetEntitiesInViewportParams"></a>