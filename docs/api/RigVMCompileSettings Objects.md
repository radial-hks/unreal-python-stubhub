## RigVMCompileSettings Objects

```python
class RigVMCompileSettings(StructBase)
```

Rig VMCompile Settings

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMCompiler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ast_settings`` (RigVMParserASTSettings):  [Read-Write]
- ``enable_pin_watches`` (bool):  [Read-Write]
- ``surpress_errors`` (bool):  [Read-Write]
- ``surpress_info_messages`` (bool):  [Read-Write]
- ``surpress_warnings`` (bool):  [Read-Write]

<a id="unreal.RigVMCompileSettings.__init__"></a>

#### __init__

```python
def __init__(surpress_info_messages: bool = False,
             surpress_warnings: bool = False,
             surpress_errors: bool = False,
             enable_pin_watches: bool = False,
             ast_settings: RigVMParserASTSettings = [True]) -> None
```

<a id="unreal.RigVMCompileSettings.surpress_info_messages"></a>

#### surpress_info_messages

```python
@property
def surpress_info_messages() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMCompileSettings.surpress_info_messages"></a>

#### surpress_info_messages

```python
@surpress_info_messages.setter
def surpress_info_messages(value: bool) -> None
```

<a id="unreal.RigVMCompileSettings.surpress_warnings"></a>

#### surpress_warnings

```python
@property
def surpress_warnings() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMCompileSettings.surpress_warnings"></a>

#### surpress_warnings

```python
@surpress_warnings.setter
def surpress_warnings(value: bool) -> None
```

<a id="unreal.RigVMCompileSettings.surpress_errors"></a>

#### surpress_errors

```python
@property
def surpress_errors() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMCompileSettings.surpress_errors"></a>

#### surpress_errors

```python
@surpress_errors.setter
def surpress_errors(value: bool) -> None
```

<a id="unreal.RigVMCompileSettings.enable_pin_watches"></a>

#### enable_pin_watches

```python
@property
def enable_pin_watches() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMCompileSettings.enable_pin_watches"></a>

#### enable_pin_watches

```python
@enable_pin_watches.setter
def enable_pin_watches(value: bool) -> None
```

<a id="unreal.RigVMCompileSettings.ast_settings"></a>

#### ast_settings

```python
@property
def ast_settings() -> RigVMParserASTSettings
```

(RigVMParserASTSettings):  [Read-Write]

<a id="unreal.RigVMCompileSettings.ast_settings"></a>

#### ast_settings

```python
@ast_settings.setter
def ast_settings(value: RigVMParserASTSettings) -> None
```

<a id="unreal.RigVMGraphParameterDescription"></a>