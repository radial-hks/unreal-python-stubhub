## PythonRBFValues Objects

```python
class PythonRBFValues(Object)
```

Python RBFValues

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonRBFLib.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``values`` (Array[float]):  [Read-Write] Set of values for this target, size must be TargetDimensions

<a id="unreal.PythonRBFValues.get_dimensions"></a>

#### get\_dimensions

```python
def get_dimensions() -> int
```

x.get_dimensions() -> int32
Return dimensionality of this target

Returns:
    int32:

<a id="unreal.PythonRBFValues.as_vector"></a>

#### as\_vector

```python
def as_vector(index: int) -> Vector
```

x.as_vector(index) -> Vector
As Vector

Args:
    index (int32): 

Returns:
    Vector:

<a id="unreal.PythonRBFValues.as_rotator"></a>

#### as\_rotator

```python
def as_rotator(index: int) -> Rotator
```

x.as_rotator(index) -> Rotator
Return a target as an rotator, assuming Values is a sequence of Euler entries. Index is which Euler to convert.

Args:
    index (int32): 

Returns:
    Rotator:

<a id="unreal.PythonRBFValues.as_quat"></a>

#### as\_quat

```python
def as_quat(index: int) -> Quat
```

x.as_quat(index) -> Quat
Return a target as a quaternion, assuming Values is a sequence of Euler entries. Index is which Euler to convert.

Args:
    index (int32): 

Returns:
    Quat:

<a id="unreal.PythonRBFValues.add_from_vector"></a>

#### add\_from\_vector

```python
def add_from_vector(vector: Vector) -> None
```

x.add_from_vector(vector) -> None
Set this entry to 3 floats from supplied vector

Args:
    vector (Vector):

<a id="unreal.PythonRBFValues.add_from_rotator"></a>

#### add\_from\_rotator

```python
def add_from_rotator(rot: Rotator) -> None
```

x.add_from_rotator(rot) -> None
Set this entry to 3 floats from supplied rotator

Args:
    rot (Rotator):

<a id="unreal.PythonRBFLib"></a>