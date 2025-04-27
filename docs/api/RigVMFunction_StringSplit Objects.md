## RigVMFunction_StringSplit Objects

```python
class RigVMFunction_StringSplit(RigVMFunction_StringBase)
```

Splits a string into multiple sections given a separator

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Array[str]):  [Read-Write]
- ``separator`` (str):  [Read-Write]
- ``value`` (str):  [Read-Write]

<a id="unreal.RigVMFunction_StringSplit.__init__"></a>

#### __init__

```python
def __init__(value: str = "",
             separator: str = "",
             result: Array[str] = []) -> None
```

<a id="unreal.RigVMFunction_StringSplit.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringSplit.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.RigVMFunction_StringSplit.separator"></a>

#### separator

```python
@property
def separator() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringSplit.separator"></a>

#### separator

```python
@separator.setter
def separator(value: str) -> None
```

<a id="unreal.RigVMFunction_StringSplit.result"></a>

#### result

```python
@property
def result() -> Array[str]
```

(Array[str]):  [Read-Only]

<a id="unreal.RigUnit_StringSplit"></a>