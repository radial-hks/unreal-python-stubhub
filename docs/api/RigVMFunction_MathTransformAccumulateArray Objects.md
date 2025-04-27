## RigVMFunction_MathTransformAccumulateArray Objects

```python
class RigVMFunction_MathTransformAccumulateArray(
        RigVMFunction_MathTransformMutableBase)
```

Treats the provided transforms as a chain with global / local transforms, and
projects each transform into the target space. Optionally you can provide
a custom parent indices array, with which you can represent more than just chains.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``parent_indices`` (Array[int32]):  [Read-Write] If this array is the same size as the transforms array the indices will be used
  to look up each transform's parent. They are expected to be in order.
- ``root`` (Transform):  [Read-Write] Provides the parent transform for the root
- ``target_space`` (RigVMTransformSpace):  [Read-Write] Defines the space to project to
- ``transforms`` (Array[Transform]):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: RigVMExecuteContext = [],
        transforms: Array[Transform] = [],
        target_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
        root: Transform = [[0.000000, 0.000000, 0.000000],
                           [-0.000000, 0.000000, 0.000000],
                           [1.000000, 1.000000, 1.000000]],
        parent_indices: Array[int] = []) -> None
```

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.target_space"></a>

#### target_space

```python
@property
def target_space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines the space to project to

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.target_space"></a>

#### target_space

```python
@target_space.setter
def target_space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.root"></a>

#### root

```python
@property
def root() -> Transform
```

(Transform):  [Read-Write] Provides the parent transform for the root

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.root"></a>

#### root

```python
@root.setter
def root(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.parent_indices"></a>

#### parent_indices

```python
@property
def parent_indices() -> Array[int]
```

(Array[int32]):  [Read-Write] If this array is the same size as the transforms array the indices will be used
to look up each transform's parent. They are expected to be in order.

<a id="unreal.RigVMFunction_MathTransformAccumulateArray.parent_indices"></a>

#### parent_indices

```python
@parent_indices.setter
def parent_indices(value: Array[int]) -> None
```

<a id="unreal.RigUnit_MathTransformAccumulateArray"></a>