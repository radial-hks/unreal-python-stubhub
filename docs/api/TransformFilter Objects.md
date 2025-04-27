## TransformFilter Objects

```python
class TransformFilter(StructBase)
```

A filter for a whole transform

**C++ Source:**

- **Module**: AnimationCore
- **File**: Constraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotation_filter`` (FilterOptionPerAxis):  [Read-Write]
- ``scale_filter`` (FilterOptionPerAxis):  [Read-Write]
- ``translation_filter`` (FilterOptionPerAxis):  [Read-Write]

<a id="unreal.TransformFilter.__init__"></a>

#### __init__

```python
def __init__(translation_filter: FilterOptionPerAxis = [True, True, True],
             rotation_filter: FilterOptionPerAxis = [True, True, True],
             scale_filter: FilterOptionPerAxis = [True, True, True]) -> None
```

<a id="unreal.TransformFilter.translation_filter"></a>

#### translation_filter

```python
@property
def translation_filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.TransformFilter.translation_filter"></a>

#### translation_filter

```python
@translation_filter.setter
def translation_filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.TransformFilter.rotation_filter"></a>

#### rotation_filter

```python
@property
def rotation_filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.TransformFilter.rotation_filter"></a>

#### rotation_filter

```python
@rotation_filter.setter
def rotation_filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.TransformFilter.scale_filter"></a>

#### scale_filter

```python
@property
def scale_filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.TransformFilter.scale_filter"></a>

#### scale_filter

```python
@scale_filter.setter
def scale_filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.ConstraintDescription"></a>