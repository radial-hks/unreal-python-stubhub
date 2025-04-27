## RigVMFunction_StringJoin Objects

```python
class RigVMFunction_StringJoin(RigVMFunction_StringBase)
```

Joins a string into multiple sections given a separator

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_String.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (str):  [Read-Write]
- ``separator`` (str):  [Read-Write]
- ``values`` (Array[str]):  [Read-Write]

<a id="unreal.RigVMFunction_StringJoin.__init__"></a>

#### __init__

```python
def __init__(values: Array[str] = [],
             separator: str = "",
             result: str = "") -> None
```

<a id="unreal.RigVMFunction_StringJoin.values"></a>

#### values

```python
@property
def values() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RigVMFunction_StringJoin.values"></a>

#### values

```python
@values.setter
def values(value: Array[str]) -> None
```

<a id="unreal.RigVMFunction_StringJoin.separator"></a>

#### separator

```python
@property
def separator() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMFunction_StringJoin.separator"></a>

#### separator

```python
@separator.setter
def separator(value: str) -> None
```

<a id="unreal.RigVMFunction_StringJoin.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Only]

<a id="unreal.RigUnit_StringJoin"></a>