## RigVMTag Objects

```python
class RigVMTag(StructBase)
```

User applied tag

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMVariant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``label`` (str):  [Read-Write]
- ``marks_subject_as_invalid`` (bool):  [Read-Write] Enabling this will mark the subject (asset, function etc) as (soft) deprecated.
  The content referring to variants with this tag will continue to work, but the
  user interface will suggest the user to upgrade to a later variant.
- ``name`` (Name):  [Read-Write]
- ``show_in_user_interface`` (bool):  [Read-Write] Enabling this will show tags in the user interface within
  the variant widgets and other places.
  Disabling this will interpret this tag as automation / scripting only.
- ``tool_tip`` (Text):  [Read-Write]

<a id="unreal.RigVMTag.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             label: str = "",
             tool_tip: Text = "",
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             show_in_user_interface: bool = False,
             marks_subject_as_invalid: bool = False) -> None
```

<a id="unreal.RigVMTag.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMTag.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigVMTag.label"></a>

#### label

```python
@property
def label() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMTag.label"></a>

#### label

```python
@label.setter
def label(value: str) -> None
```

<a id="unreal.RigVMTag.tool_tip"></a>

#### tool_tip

```python
@property
def tool_tip() -> Text
```

(Text):  [Read-Write]

<a id="unreal.RigVMTag.tool_tip"></a>

#### tool_tip

```python
@tool_tip.setter
def tool_tip(value: Text) -> None
```

<a id="unreal.RigVMTag.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMTag.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMTag.show_in_user_interface"></a>

#### show_in_user_interface

```python
@property
def show_in_user_interface() -> bool
```

(bool):  [Read-Write] Enabling this will show tags in the user interface within
the variant widgets and other places.
Disabling this will interpret this tag as automation / scripting only.

<a id="unreal.RigVMTag.show_in_user_interface"></a>

#### show_in_user_interface

```python
@show_in_user_interface.setter
def show_in_user_interface(value: bool) -> None
```

<a id="unreal.RigVMTag.marks_subject_as_invalid"></a>

#### marks_subject_as_invalid

```python
@property
def marks_subject_as_invalid() -> bool
```

(bool):  [Read-Write] Enabling this will mark the subject (asset, function etc) as (soft) deprecated.
The content referring to variants with this tag will continue to work, but the
user interface will suggest the user to upgrade to a later variant.

<a id="unreal.RigVMTag.marks_subject_as_invalid"></a>

#### marks_subject_as_invalid

```python
@marks_subject_as_invalid.setter
def marks_subject_as_invalid(value: bool) -> None
```

<a id="unreal.RigVMMemoryStatistics"></a>