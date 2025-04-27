## RigVMGraphFunctionArgument Objects

```python
class RigVMGraphFunctionArgument(StructBase)
```

Rig VMGraph Function Argument

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMGraphFunctionDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cpp_type`` (Name):  [Read-Only]
- ``cpp_type_object`` (Object):  [Read-Only]
- ``default_value`` (str):  [Read-Only]
- ``direction`` (RigVMPinDirection):  [Read-Only]
- ``display_name`` (Name):  [Read-Only]
- ``is_array`` (bool):  [Read-Only]
- ``is_const`` (bool):  [Read-Only]
- ``name`` (Name):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             display_name: Name = "None",
             cpp_type: Name = "None",
             cpp_type_object: Object = None,
             is_array: bool = False,
             direction: RigVMPinDirection = RigVMPinDirection.INPUT,
             default_value: str = "",
             is_const: bool = False) -> None
```

<a id="unreal.RigVMGraphFunctionArgument.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.display_name"></a>

#### display_name

```python
@property
def display_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.cpp_type"></a>

#### cpp_type

```python
@property
def cpp_type() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.cpp_type_object"></a>

#### cpp_type_object

```python
@property
def cpp_type_object() -> Object
```

(Object):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.is_array"></a>

#### is_array

```python
@property
def is_array() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.direction"></a>

#### direction

```python
@property
def direction() -> RigVMPinDirection
```

(RigVMPinDirection):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.default_value"></a>

#### default_value

```python
@property
def default_value() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionArgument.is_const"></a>

#### is_const

```python
@property
def is_const() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMVariant"></a>