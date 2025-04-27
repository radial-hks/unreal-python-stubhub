## PCGPreConfiguredSettingsInfo Objects

```python
class PCGPreConfiguredSettingsInfo(StructBase)
```

Pre-configured settings info
Will be passed to the settings to pre-configure the settings on creation.
Example: Maths operations: Add, Mul, etc...

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``label`` (Text):  [Read-Write] Label for the exposed asset. Can also be used instead of the index, if it is easier to deal with strings.
- ``preconfigured_index`` (int32):  [Read-Write] Index used by the settings to know which preconfigured settings it needs to set.
- ``tooltip`` (Text):  [Read-Write]

<a id="unreal.PCGPreConfiguredSettingsInfo.__init__"></a>

#### __init__

```python
def __init__(preconfigured_index: int = 0, label: Text = "") -> None
```

<a id="unreal.PCGPreConfiguredSettingsInfo.preconfigured_index"></a>

#### preconfigured_index

```python
@property
def preconfigured_index() -> int
```

(int32):  [Read-Write] Index used by the settings to know which preconfigured settings it needs to set.

<a id="unreal.PCGPreConfiguredSettingsInfo.preconfigured_index"></a>

#### preconfigured_index

```python
@preconfigured_index.setter
def preconfigured_index(value: int) -> None
```

<a id="unreal.PCGPreConfiguredSettingsInfo.label"></a>

#### label

```python
@property
def label() -> Text
```

(Text):  [Read-Write] Label for the exposed asset. Can also be used instead of the index, if it is easier to deal with strings.

<a id="unreal.PCGPreConfiguredSettingsInfo.label"></a>

#### label

```python
@label.setter
def label(value: Text) -> None
```

<a id="unreal.DeterminismTestResult"></a>