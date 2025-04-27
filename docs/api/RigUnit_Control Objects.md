## RigUnit_Control Objects

```python
class RigUnit_Control(RigUnit)
```

A control unit used to drive a transform from an external source

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Control.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base`` (Transform):  [Read-Write] The base that transform is relative to
- ``filter`` (TransformFilter):  [Read-Write] The filter determines what axes can be manipulated by the in-viewport widgets
- ``init_transform`` (Transform):  [Read-Write] The initial transform that The Transform is initialized to.
- ``result`` (Transform):  [Read-Write] The resultant transform of this unit (Base * Filter(Transform))
- ``transform`` (EulerTransform):  [Read-Write] The transform of this control

<a id="unreal.RigUnit_Control.__init__"></a>

#### __init__

```python
def __init__(
    transform: EulerTransform = [[0.000000, 0.000000, 0.000000],
                                 [0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
    base: Transform = [[0.000000, 0.000000, 0.000000],
                       [-0.000000, 0.000000, 0.000000],
                       [1.000000, 1.000000, 1.000000]],
    init_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]],
    filter: TransformFilter = [[True, True, True], [True, True, True],
                               [True, True, True]]
) -> None
```

<a id="unreal.RigUnit_Control.transform"></a>

#### transform

```python
@property
def transform() -> EulerTransform
```

(EulerTransform):  [Read-Write] The transform of this control

<a id="unreal.RigUnit_Control.transform"></a>

#### transform

```python
@transform.setter
def transform(value: EulerTransform) -> None
```

<a id="unreal.RigUnit_Control.base"></a>

#### base

```python
@property
def base() -> Transform
```

(Transform):  [Read-Write] The base that transform is relative to

<a id="unreal.RigUnit_Control.base"></a>

#### base

```python
@base.setter
def base(value: Transform) -> None
```

<a id="unreal.RigUnit_Control.init_transform"></a>

#### init_transform

```python
@property
def init_transform() -> Transform
```

(Transform):  [Read-Write] The initial transform that The Transform is initialized to.

<a id="unreal.RigUnit_Control.init_transform"></a>

#### init_transform

```python
@init_transform.setter
def init_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_Control.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only] The resultant transform of this unit (Base * Filter(Transform))

<a id="unreal.RigUnit_Control.filter"></a>

#### filter

```python
@property
def filter() -> TransformFilter
```

(TransformFilter):  [Read-Write] The filter determines what axes can be manipulated by the in-viewport widgets

<a id="unreal.RigUnit_Control.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TransformFilter) -> None
```

<a id="unreal.RigUnit_Control_StaticMesh"></a>