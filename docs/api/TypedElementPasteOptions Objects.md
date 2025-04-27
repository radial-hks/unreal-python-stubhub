## TypedElementPasteOptions Objects

```python
class TypedElementPasteOptions(StructBase)
```

Typed Element Paste Options

**C++ Source:**

- **Module**: Engine
- **File**: TypedElementCommonActions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``paste_at_location`` (bool):  [Read-Write]
- ``paste_location`` (Vector):  [Read-Write]
- ``selection_set_to_modify`` (TypedElementSelectionSet):  [Read-Write] If provided the SelectionSet selection will only contains the newly added elements

<a id="unreal.TypedElementPasteOptions.__init__"></a>

#### __init__

```python
def __init__(selection_set_to_modify: TypedElementSelectionSet = None,
             paste_at_location: bool = False,
             paste_location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.TypedElementPasteOptions.selection_set_to_modify"></a>

#### selection_set_to_modify

```python
@property
def selection_set_to_modify() -> TypedElementSelectionSet
```

(TypedElementSelectionSet):  [Read-Write] If provided the SelectionSet selection will only contains the newly added elements

<a id="unreal.TypedElementPasteOptions.selection_set_to_modify"></a>

#### selection_set_to_modify

```python
@selection_set_to_modify.setter
def selection_set_to_modify(value: TypedElementSelectionSet) -> None
```

<a id="unreal.TypedElementPasteOptions.paste_at_location"></a>

#### paste_at_location

```python
@property
def paste_at_location() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementPasteOptions.paste_at_location"></a>

#### paste_at_location

```python
@paste_at_location.setter
def paste_at_location(value: bool) -> None
```

<a id="unreal.TypedElementPasteOptions.paste_location"></a>

#### paste_location

```python
@property
def paste_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.TypedElementPasteOptions.paste_location"></a>

#### paste_location

```python
@paste_location.setter
def paste_location(value: Vector) -> None
```

<a id="unreal.TypedElementDeletionOptions"></a>