## TypedElementSelectionOptions Objects

```python
class TypedElementSelectionOptions(StructBase)
```

Typed Element Selection Options

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementSelectionInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_groups`` (bool):  [Read-Write]
- ``allow_hidden`` (bool):  [Read-Write]
- ``allow_legacy_notifications`` (bool):  [Read-Write]
- ``allow_sub_root_selection`` (bool):  [Read-Write]
- ``child_element_inclusion_method`` (TypedElementChildInclusionMethod):  [Read-Write]
- ``warn_if_locked`` (bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    allow_hidden: bool = False,
    allow_groups: bool = False,
    allow_legacy_notifications: bool = False,
    warn_if_locked: bool = False,
    allow_sub_root_selection: bool = False,
    child_element_inclusion_method:
    TypedElementChildInclusionMethod = TypedElementChildInclusionMethod.NONE
) -> None
```

<a id="unreal.TypedElementSelectionOptions.allow_hidden"></a>

#### allow\_hidden

```python
@property
def allow_hidden() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.allow_hidden"></a>

#### allow\_hidden

```python
@allow_hidden.setter
def allow_hidden(value: bool) -> None
```

<a id="unreal.TypedElementSelectionOptions.allow_groups"></a>

#### allow\_groups

```python
@property
def allow_groups() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.allow_groups"></a>

#### allow\_groups

```python
@allow_groups.setter
def allow_groups(value: bool) -> None
```

<a id="unreal.TypedElementSelectionOptions.allow_legacy_notifications"></a>

#### allow\_legacy\_notifications

```python
@property
def allow_legacy_notifications() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.allow_legacy_notifications"></a>

#### allow\_legacy\_notifications

```python
@allow_legacy_notifications.setter
def allow_legacy_notifications(value: bool) -> None
```

<a id="unreal.TypedElementSelectionOptions.warn_if_locked"></a>

#### warn\_if\_locked

```python
@property
def warn_if_locked() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.warn_if_locked"></a>

#### warn\_if\_locked

```python
@warn_if_locked.setter
def warn_if_locked(value: bool) -> None
```

<a id="unreal.TypedElementSelectionOptions.allow_sub_root_selection"></a>

#### allow\_sub\_root\_selection

```python
@property
def allow_sub_root_selection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.allow_sub_root_selection"></a>

#### allow\_sub\_root\_selection

```python
@allow_sub_root_selection.setter
def allow_sub_root_selection(value: bool) -> None
```

<a id="unreal.TypedElementSelectionOptions.child_element_inclusion_method"></a>

#### child\_element\_inclusion\_method

```python
@property
def child_element_inclusion_method() -> TypedElementChildInclusionMethod
```

(TypedElementChildInclusionMethod):  [Read-Write]

<a id="unreal.TypedElementSelectionOptions.child_element_inclusion_method"></a>

#### child\_element\_inclusion\_method

```python
@child_element_inclusion_method.setter
def child_element_inclusion_method(
        value: TypedElementChildInclusionMethod) -> None
```

<a id="unreal.TypedElementSelectionSetState"></a>