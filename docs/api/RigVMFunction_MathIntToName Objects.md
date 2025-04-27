## RigVMFunction_MathIntToName Objects

```python
class RigVMFunction_MathIntToName(RigVMFunction_MathIntBase)
```

Converts an integer to a name

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathInt.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``number`` (int32):  [Read-Write]
- ``padded_size`` (int32):  [Read-Write] * For positive numbers you can pad the result to a required with
  * so rather than '13' return '00013' for a padded size of 5.
- ``result`` (Name):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntToName.__init__"></a>

#### __init__

```python
def __init__(number: int = 0,
             padded_size: int = 0,
             result: Name = "None") -> None
```

<a id="unreal.RigVMFunction_MathIntToName.number"></a>

#### number

```python
@property
def number() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntToName.number"></a>

#### number

```python
@number.setter
def number(value: int) -> None
```

<a id="unreal.RigVMFunction_MathIntToName.padded_size"></a>

#### padded_size

```python
@property
def padded_size() -> int
```

(int32):  [Read-Write] * For positive numbers you can pad the result to a required with
* so rather than '13' return '00013' for a padded size of 5.

<a id="unreal.RigVMFunction_MathIntToName.padded_size"></a>

#### padded_size

```python
@padded_size.setter
def padded_size(value: int) -> None
```

<a id="unreal.RigVMFunction_MathIntToName.result"></a>

#### result

```python
@property
def result() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigVMFunction_MathMatrixBase"></a>