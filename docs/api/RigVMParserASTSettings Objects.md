## RigVMParserASTSettings Objects

```python
class RigVMParserASTSettings(StructBase)
```

* The settings to apply during the parse of the abstract syntax tree.
* The folding settings can affect the performance of the parse dramatically.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMAST.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context_struct`` (ScriptStruct):  [Read-Only]
- ``fold_assignments`` (bool):  [Read-Write] fold assignments / copies
- ``fold_literals`` (bool):  [Read-Write] fold literals and share memory
- ``setup_traits`` (bool):  [Read-Write]

<a id="unreal.RigVMParserASTSettings.__init__"></a>

#### __init__

```python
def __init__(setup_traits: bool = False) -> None
```

<a id="unreal.RigVMParserASTSettings.setup_traits"></a>

#### setup_traits

```python
@property
def setup_traits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMParserASTSettings.setup_traits"></a>

#### setup_traits

```python
@setup_traits.setter
def setup_traits(value: bool) -> None
```

<a id="unreal.RigVMCompileSettings"></a>