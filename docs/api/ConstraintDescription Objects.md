## ConstraintDescription Objects

```python
class ConstraintDescription(StructBase)
```

A description of how to apply a simple transform constraint

**C++ Source:**

- **Module**: AnimationCore
- **File**: Constraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parent`` (bool):  [Read-Write] this does composed transform - where as individual will accumulate per component
- ``rotation`` (bool):  [Read-Write]
- ``rotation_axes`` (FilterOptionPerAxis):  [Read-Write]
- ``scale`` (bool):  [Read-Write]
- ``scale_axes`` (FilterOptionPerAxis):  [Read-Write]
- ``translation`` (bool):  [Read-Write]
- ``translation_axes`` (FilterOptionPerAxis):  [Read-Write]

<a id="unreal.ConstraintDescription.__init__"></a>

#### __init__

```python
def __init__(translation: bool = False,
             rotation: bool = False,
             scale: bool = False,
             parent: bool = False,
             translation_axes: FilterOptionPerAxis = [True, True, True],
             rotation_axes: FilterOptionPerAxis = [True, True, True],
             scale_axes: FilterOptionPerAxis = [True, True, True]) -> None
```

<a id="unreal.ConstraintDescription.translation"></a>

#### translation

```python
@property
def translation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ConstraintDescription.translation"></a>

#### translation

```python
@translation.setter
def translation(value: bool) -> None
```

<a id="unreal.ConstraintDescription.rotation"></a>

#### rotation

```python
@property
def rotation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ConstraintDescription.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: bool) -> None
```

<a id="unreal.ConstraintDescription.scale"></a>

#### scale

```python
@property
def scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ConstraintDescription.scale"></a>

#### scale

```python
@scale.setter
def scale(value: bool) -> None
```

<a id="unreal.ConstraintDescription.parent"></a>

#### parent

```python
@property
def parent() -> bool
```

(bool):  [Read-Write] this does composed transform - where as individual will accumulate per component

<a id="unreal.ConstraintDescription.parent"></a>

#### parent

```python
@parent.setter
def parent(value: bool) -> None
```

<a id="unreal.ConstraintDescription.translation_axes"></a>

#### translation_axes

```python
@property
def translation_axes() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.ConstraintDescription.translation_axes"></a>

#### translation_axes

```python
@translation_axes.setter
def translation_axes(value: FilterOptionPerAxis) -> None
```

<a id="unreal.ConstraintDescription.rotation_axes"></a>

#### rotation_axes

```python
@property
def rotation_axes() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.ConstraintDescription.rotation_axes"></a>

#### rotation_axes

```python
@rotation_axes.setter
def rotation_axes(value: FilterOptionPerAxis) -> None
```

<a id="unreal.ConstraintDescription.scale_axes"></a>

#### scale_axes

```python
@property
def scale_axes() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.ConstraintDescription.scale_axes"></a>

#### scale_axes

```python
@scale_axes.setter
def scale_axes(value: FilterOptionPerAxis) -> None
```

<a id="unreal.TransformConstraint"></a>