## RigControlCopy Objects

```python
class RigControlCopy(StructBase)
```

The Data Stored For Each Control in A Pose.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_type`` (RigControlType):  [Read-Write]
- ``global_transform`` (Transform):  [Read-Write]
- ``local_transform`` (Transform):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``offset_transform`` (Transform):  [Read-Write]
- ``parent_key`` (RigElementKey):  [Read-Write]
- ``parent_transform`` (Transform):  [Read-Write]

<a id="unreal.RigControlCopy.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    name: Name = "None",
    control_type: RigControlType = RigControlType.BOOL,
    parent_key: RigElementKey = [RigElementType.NONE, "None"],
    offset_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                   [-0.000000, 0.000000, 0.000000],
                                   [1.000000, 1.000000, 1.000000]],
    parent_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                   [-0.000000, 0.000000, 0.000000],
                                   [1.000000, 1.000000, 1.000000]],
    local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                  [-0.000000, 0.000000, 0.000000],
                                  [1.000000, 1.000000, 1.000000]],
    global_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                   [-0.000000, 0.000000, 0.000000],
                                   [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigControlCopy.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigControlCopy.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigControlCopy.control_type"></a>

#### control\_type

```python
@property
def control_type() -> RigControlType
```

(RigControlType):  [Read-Write]

<a id="unreal.RigControlCopy.control_type"></a>

#### control\_type

```python
@control_type.setter
def control_type(value: RigControlType) -> None
```

<a id="unreal.RigControlCopy.parent_key"></a>

#### parent\_key

```python
@property
def parent_key() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigControlCopy.parent_key"></a>

#### parent\_key

```python
@parent_key.setter
def parent_key(value: RigElementKey) -> None
```

<a id="unreal.RigControlCopy.offset_transform"></a>

#### offset\_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigControlCopy.offset_transform"></a>

#### offset\_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.RigControlCopy.parent_transform"></a>

#### parent\_transform

```python
@property
def parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigControlCopy.parent_transform"></a>

#### parent\_transform

```python
@parent_transform.setter
def parent_transform(value: Transform) -> None
```

<a id="unreal.RigControlCopy.local_transform"></a>

#### local\_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigControlCopy.local_transform"></a>

#### local\_transform

```python
@local_transform.setter
def local_transform(value: Transform) -> None
```

<a id="unreal.RigControlCopy.global_transform"></a>

#### global\_transform

```python
@property
def global_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigControlCopy.global_transform"></a>

#### global\_transform

```python
@global_transform.setter
def global_transform(value: Transform) -> None
```

<a id="unreal.ControlRigControlPose"></a>