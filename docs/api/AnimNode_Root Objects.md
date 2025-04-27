## AnimNode_Root Objects

```python
class AnimNode_Root(AnimNode_Base)
```

Root node of an animation tree (sink)

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_Root.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group`` (Name):  [Read-Write]
  deprecated: Please, use LayerGroup
- ``result`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_Root.__init__"></a>

#### __init__

```python
def __init__(result: PoseLink = []) -> None
```

<a id="unreal.AnimNode_Root.result"></a>

#### result

```python
@property
def result() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_Root.result"></a>

#### result

```python
@result.setter
def result(value: PoseLink) -> None
```

<a id="unreal.AnimNode_Root.group"></a>

#### group

```python
@property
def group() -> Name
```

(Name):  [Read-Write]
deprecated: Please, use LayerGroup

<a id="unreal.AnimNode_Root.group"></a>

#### group

```python
@group.setter
def group(value: Name) -> None
```

<a id="unreal.AnimNode_BlendSpaceSampleResult"></a>