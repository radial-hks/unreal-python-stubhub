## MetaSoundBuilderOptions Objects

```python
class MetaSoundBuilderOptions(StructBase)
```

Meta Sound Builder Options

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundBuilderBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``force_unique_class_name`` (bool):  [Read-Write] If the resulting MetaSound is building over an existing document, a unique class name will be generated,
  invalidating any referencing MetaSounds and registering the MetaSound as a new entry in the Frontend. If
  building a new document, option is ignored (new document always generates a unique class name).
- ``name`` (Name):  [Read-Write] Name of generated object. If object already exists, used as the base name to ensure new object is unique.
  If left 'None', creates unique name.

<a id="unreal.MetaSoundBuilderOptions.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             force_unique_class_name: bool = False) -> None
```

<a id="unreal.MetaSoundBuilderOptions.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Name of generated object. If object already exists, used as the base name to ensure new object is unique.
If left 'None', creates unique name.

<a id="unreal.MetaSoundBuilderOptions.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.MetaSoundBuilderOptions.force_unique_class_name"></a>

#### force_unique_class_name

```python
@property
def force_unique_class_name() -> bool
```

(bool):  [Read-Write] If the resulting MetaSound is building over an existing document, a unique class name will be generated,
invalidating any referencing MetaSounds and registering the MetaSound as a new entry in the Frontend. If
building a new document, option is ignored (new document always generates a unique class name).

<a id="unreal.MetaSoundBuilderOptions.force_unique_class_name"></a>

#### force_unique_class_name

```python
@force_unique_class_name.setter
def force_unique_class_name(value: bool) -> None
```

<a id="unreal.MeterChannelInfo"></a>