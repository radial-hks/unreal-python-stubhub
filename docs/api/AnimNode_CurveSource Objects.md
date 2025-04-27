## AnimNode_CurveSource Objects

```python
class AnimNode_CurveSource(AnimNode_Base)
```

Supply curves from some external source (e.g. audio)

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_CurveSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] How much we wan to blend the curve in by
- ``source_binding`` (Name):  [Read-Write] The binding of the curve source we want to bind to.
  We will bind to an object that implements ICurveSourceInterface. First we check
  the actor that owns this (if any), then we check each of its components to see if we should
  bind to the source that matches this name.
- ``source_pose`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_CurveSource.__init__"></a>

#### __init__

```python
def __init__(source_pose: PoseLink = [],
             source_binding: Name = "None",
             alpha: float = 0.000000) -> None
```

<a id="unreal.AnimNode_CurveSource.source_pose"></a>

#### source_pose

```python
@property
def source_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_CurveSource.source_pose"></a>

#### source_pose

```python
@source_pose.setter
def source_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_CurveSource.source_binding"></a>

#### source_binding

```python
@property
def source_binding() -> Name
```

(Name):  [Read-Write] The binding of the curve source we want to bind to.
We will bind to an object that implements ICurveSourceInterface. First we check
the actor that owns this (if any), then we check each of its components to see if we should
bind to the source that matches this name.

<a id="unreal.AnimNode_CurveSource.source_binding"></a>

#### source_binding

```python
@source_binding.setter
def source_binding(value: Name) -> None
```

<a id="unreal.AnimNode_CurveSource.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] How much we wan to blend the curve in by

<a id="unreal.AnimNode_CurveSource.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_LayeredBoneBlend"></a>