## RigVMFunction_MathQuaternionMirrorTransform Objects

```python
class RigVMFunction_MathQuaternionMirrorTransform(
        RigVMFunction_MathQuaternionBase)
```

Mirror a rotation about a central transform.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_to_flip`` (AxisType):  [Read-Write] the axis to flip for rotations
- ``central_transform`` (Transform):  [Read-Write] The transform about which to mirror
- ``mirror_axis`` (AxisType):  [Read-Write] the axis to mirror against
- ``result`` (Quat):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             mirror_axis: AxisType = AxisType.NONE,
             axis_to_flip: AxisType = AxisType.NONE,
             central_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                             [-0.000000, 0.000000, 0.000000],
                                             [1.000000, 1.000000, 1.000000]],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.mirror_axis"></a>

#### mirror_axis

```python
@property
def mirror_axis() -> AxisType
```

(AxisType):  [Read-Write] the axis to mirror against

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.mirror_axis"></a>

#### mirror_axis

```python
@mirror_axis.setter
def mirror_axis(value: AxisType) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.axis_to_flip"></a>

#### axis_to_flip

```python
@property
def axis_to_flip() -> AxisType
```

(AxisType):  [Read-Write] the axis to flip for rotations

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.axis_to_flip"></a>

#### axis_to_flip

```python
@axis_to_flip.setter
def axis_to_flip(value: AxisType) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.central_transform"></a>

#### central_transform

```python
@property
def central_transform() -> Transform
```

(Transform):  [Read-Write] The transform about which to mirror

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.central_transform"></a>

#### central_transform

```python
@central_transform.setter
def central_transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMirrorTransform.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionMirrorTransform"></a>