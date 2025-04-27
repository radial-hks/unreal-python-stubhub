## EditorDialogLibraryObjectDetailsViewOptions Objects

```python
class EditorDialogLibraryObjectDetailsViewOptions(StructBase)
```

Editor Dialog Library Object Details View Options

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorDialogLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_resizing`` (bool):  [Read-Write]
- ``allow_search`` (bool):  [Read-Write]
- ``min_height`` (int32):  [Read-Write] The minimum dialog height. If zero, default to the medium window height defined by the Editor style.
- ``min_width`` (int32):  [Read-Write] The minimum dialog width. If zero, default to the medium window width defined by the Editor style.
- ``show_object_name`` (bool):  [Read-Write]
- ``value_column_width_ratio`` (float):  [Read-Write] The column size proportion, between 0 and 1, used to display the property value. The remaining of the horizontal space will be used to display the property name.

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.__init__"></a>

#### __init__

```python
def __init__(show_object_name: bool = False,
             allow_search: bool = False,
             allow_resizing: bool = False,
             min_width: int = 0,
             min_height: int = 0,
             value_column_width_ratio: float = 0.000000) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.show_object_name"></a>

#### show_object_name

```python
@property
def show_object_name() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.show_object_name"></a>

#### show_object_name

```python
@show_object_name.setter
def show_object_name(value: bool) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_search"></a>

#### allow_search

```python
@property
def allow_search() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_search"></a>

#### allow_search

```python
@allow_search.setter
def allow_search(value: bool) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_resizing"></a>

#### allow_resizing

```python
@property
def allow_resizing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_resizing"></a>

#### allow_resizing

```python
@allow_resizing.setter
def allow_resizing(value: bool) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.min_width"></a>

#### min_width

```python
@property
def min_width() -> int
```

(int32):  [Read-Write] The minimum dialog width. If zero, default to the medium window width defined by the Editor style.

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.min_width"></a>

#### min_width

```python
@min_width.setter
def min_width(value: int) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.min_height"></a>

#### min_height

```python
@property
def min_height() -> int
```

(int32):  [Read-Write] The minimum dialog height. If zero, default to the medium window height defined by the Editor style.

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.min_height"></a>

#### min_height

```python
@min_height.setter
def min_height(value: int) -> None
```

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.value_column_width_ratio"></a>

#### value_column_width_ratio

```python
@property
def value_column_width_ratio() -> float
```

(float):  [Read-Write] The column size proportion, between 0 and 1, used to display the property value. The remaining of the horizontal space will be used to display the property name.

<a id="unreal.EditorDialogLibraryObjectDetailsViewOptions.value_column_width_ratio"></a>

#### value_column_width_ratio

```python
@value_column_width_ratio.setter
def value_column_width_ratio(value: float) -> None
```

<a id="unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated"></a>