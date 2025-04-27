## RigVMGraphVariableDescription Objects

```python
class RigVMGraphVariableDescription(StructBase)
```

The variable description is used to convey information
about unique variables within a Graph. Multiple Variable
Nodes can share the same variable description.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMVariableDescription.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cpp_type`` (str):  [Read-Write] The C++ data type of the variable
- ``cpp_type_object`` (Object):  [Read-Write] The Struct of the C++ data type of the variable (or nullptr)
- ``default_value`` (str):  [Read-Write] The default value of the variable
- ``name`` (Name):  [Read-Write] The name of the variable

<a id="unreal.RigVMGraphVariableDescription.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             cpp_type: str = "",
             cpp_type_object: Object = None,
             default_value: str = "") -> None
```

<a id="unreal.RigVMGraphVariableDescription.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] The name of the variable

<a id="unreal.RigVMGraphVariableDescription.cpp_type"></a>

#### cpp_type

```python
@property
def cpp_type() -> str
```

(str):  [Read-Only] The C++ data type of the variable

<a id="unreal.RigVMGraphVariableDescription.cpp_type_object"></a>

#### cpp_type_object

```python
@property
def cpp_type_object() -> Object
```

(Object):  [Read-Only] The Struct of the C++ data type of the variable (or nullptr)

<a id="unreal.RigVMGraphVariableDescription.default_value"></a>

#### default_value

```python
@property
def default_value() -> str
```

(str):  [Read-Only] The default value of the variable

<a id="unreal.RigVMParserASTSettings"></a>