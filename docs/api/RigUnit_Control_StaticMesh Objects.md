## RigUnit_Control_StaticMesh Objects

```python
class RigUnit_Control_StaticMesh(RigUnit_Control)
```

A control unit used to drive a transform from an external source

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Control_StaticMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base`` (Transform):  [Read-Write] The base that transform is relative to
- ``filter`` (TransformFilter):  [Read-Write] The filter determines what axes can be manipulated by the in-viewport widgets
- ``init_transform`` (Transform):  [Read-Write] The initial transform that The Transform is initialized to.
- ``mesh_transform`` (Transform):  [Read-Write] The the transform the mesh will be rendered with (applied on top of the control's transform in the viewport)
- ``result`` (Transform):  [Read-Write] The resultant transform of this unit (Base * Filter(Transform))
- ``transform`` (EulerTransform):  [Read-Write] The transform of this control

<a id="unreal.RigUnit_Control_StaticMesh.__init__"></a>

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
                               [True, True, True]],
    mesh_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_Control_StaticMesh.mesh_transform"></a>

#### mesh_transform

```python
@property
def mesh_transform() -> Transform
```

(Transform):  [Read-Write] The the transform the mesh will be rendered with (applied on top of the control's transform in the viewport)

<a id="unreal.RigUnit_Control_StaticMesh.mesh_transform"></a>

#### mesh_transform

```python
@mesh_transform.setter
def mesh_transform(value: Transform) -> None
```

<a id="unreal.RigDispatch_GetUserData"></a>