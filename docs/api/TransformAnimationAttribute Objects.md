## TransformAnimationAttribute Objects

```python
class TransformAnimationAttribute(StructBase)
```

Attribute type supporting the legacy TVariant<FTransform> attributes

**C++ Source:**

- **Module**: Engine
- **File**: BuiltInAttributeTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (Transform):  [Read-Write]

<a id="unreal.TransformAnimationAttribute.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.TransformAnimationAttribute.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.TransformAnimationAttribute.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.VectorAnimationAttribute"></a>