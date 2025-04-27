## ComponentSpacePose Objects

```python
class ComponentSpacePose(StructBase)
```

A pose in component space (i.e. each transform is relative to the component's transform)

**C++ Source:**

- **Module**: Engine
- **File**: AnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``names`` (Array[Name]):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]

<a id="unreal.ComponentSpacePose.__init__"></a>

#### __init__

```python
def __init__(transforms: Array[Transform] = [],
             names: Array[Name] = []) -> None
```

<a id="unreal.ComponentSpacePose.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.ComponentSpacePose.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.ComponentSpacePose.names"></a>

#### names

```python
@property
def names() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.ComponentSpacePose.names"></a>

#### names

```python
@names.setter
def names(value: Array[Name]) -> None
```

<a id="unreal.AnimCurveBase"></a>