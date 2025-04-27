## RigVMGraphParameterDescription Objects

```python
class RigVMGraphParameterDescription(StructBase)
```

The parameter description is used to convey information
about unique parameters within a Graph. Multiple Parameter
Nodes can share the same parameter description.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMParameterNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cpp_type`` (str):  [Read-Write] The C++ data type of the parameter
- ``cpp_type_object`` (Object):  [Read-Write] The Struct of the C++ data type of the parameter (or nullptr)
- ``default_value`` (str):  [Read-Write] The default value of the parameter
- ``is_input`` (bool):  [Read-Write] True if the parameter is an input
- ``name`` (Name):  [Read-Write] The name of the parameter

<a id="unreal.RigVMGraphParameterDescription.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             is_input: bool = False,
             cpp_type: str = "",
             cpp_type_object: Object = None,
             default_value: str = "") -> None
```

<a id="unreal.RigVMGraphParameterDescription.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] The name of the parameter

<a id="unreal.RigVMGraphParameterDescription.is_input"></a>

#### is_input

```python
@property
def is_input() -> bool
```

(bool):  [Read-Only] True if the parameter is an input

<a id="unreal.RigVMGraphParameterDescription.cpp_type"></a>

#### cpp_type

```python
@property
def cpp_type() -> str
```

(str):  [Read-Only] The C++ data type of the parameter

<a id="unreal.RigVMGraphParameterDescription.cpp_type_object"></a>

#### cpp_type_object

```python
@property
def cpp_type_object() -> Object
```

(Object):  [Read-Only] The Struct of the C++ data type of the parameter (or nullptr)

<a id="unreal.RigVMGraphParameterDescription.default_value"></a>

#### default_value

```python
@property
def default_value() -> str
```

(str):  [Read-Only] The default value of the parameter

<a id="unreal.RigVMFunctionReferenceArray"></a>