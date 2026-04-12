## RigUnit\_HierarchyCreatePoseItemArray\_Entry Objects

```python
class RigUnit_HierarchyCreatePoseItemArray_Entry(StructBase)
```

Rig Unit Hierarchy Create Pose Item Array Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_value`` (float):  [Read-Write] in case of a curve this can be used to drive the curve value
- ``euler_angles`` (Vector):  [Read-Write] in case of a control this can be used to drive the preferred euler angles
- ``global_transform`` (Transform):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``local_transform`` (Transform):  [Read-Write]
- ``use_euler_angles`` (bool):  [Read-Write] in case of a control this can be used to drive the preferred euler angles

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.__init__"></a>

#### \_\_init\_\_

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             global_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             use_euler_angles: bool = False,
             euler_angles: Vector = [0.000000, 0.000000, 0.000000],
             curve_value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.local_transform"></a>

#### local\_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.local_transform"></a>

#### local\_transform

```python
@local_transform.setter
def local_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.global_transform"></a>

#### global\_transform

```python
@property
def global_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.global_transform"></a>

#### global\_transform

```python
@global_transform.setter
def global_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.use_euler_angles"></a>

#### use\_euler\_angles

```python
@property
def use_euler_angles() -> bool
```

(bool):  [Read-Write] in case of a control this can be used to drive the preferred euler angles

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.use_euler_angles"></a>

#### use\_euler\_angles

```python
@use_euler_angles.setter
def use_euler_angles(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.euler_angles"></a>

#### euler\_angles

```python
@property
def euler_angles() -> Vector
```

(Vector):  [Read-Write] in case of a control this can be used to drive the preferred euler angles

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.euler_angles"></a>

#### euler\_angles

```python
@euler_angles.setter
def euler_angles(value: Vector) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.curve_value"></a>

#### curve\_value

```python
@property
def curve_value() -> float
```

(float):  [Read-Write] in case of a curve this can be used to drive the curve value

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.curve_value"></a>

#### curve\_value

```python
@curve_value.setter
def curve_value(value: float) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray"></a>