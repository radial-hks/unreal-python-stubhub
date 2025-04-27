## OpenColorIOColorSpace Objects

```python
class OpenColorIOColorSpace(StructBase)
```

Structure to identify a ColorSpace as described in an OCIO configuration file.
Members are populated by data coming from a config file.

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIOColorSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_space_index`` (int32):  [Read-Write] The index of the ColorSpace in the config
- ``color_space_name`` (str):  [Read-Write] The ColorSpace name.
- ``family_name`` (str):  [Read-Write] The family of this ColorSpace as specified in the configuration file.
  When you have lots of colorspaces, you can regroup them by family to facilitate browsing them.

<a id="unreal.OpenColorIOColorSpace.__init__"></a>

#### __init__

```python
def __init__(color_space_name: str = "",
             color_space_index: int = 0,
             family_name: str = "") -> None
```

<a id="unreal.OpenColorIOColorSpace.color_space_name"></a>

#### color_space_name

```python
@property
def color_space_name() -> str
```

(str):  [Read-Write] The ColorSpace name.

<a id="unreal.OpenColorIOColorSpace.color_space_name"></a>

#### color_space_name

```python
@color_space_name.setter
def color_space_name(value: str) -> None
```

<a id="unreal.OpenColorIOColorSpace.color_space_index"></a>

#### color_space_index

```python
@property
def color_space_index() -> int
```

(int32):  [Read-Write] The index of the ColorSpace in the config

<a id="unreal.OpenColorIOColorSpace.color_space_index"></a>

#### color_space_index

```python
@color_space_index.setter
def color_space_index(value: int) -> None
```

<a id="unreal.OpenColorIOColorSpace.family_name"></a>

#### family_name

```python
@property
def family_name() -> str
```

(str):  [Read-Write] The family of this ColorSpace as specified in the configuration file.
When you have lots of colorspaces, you can regroup them by family to facilitate browsing them.

<a id="unreal.OpenColorIOColorSpace.family_name"></a>

#### family_name

```python
@family_name.setter
def family_name(value: str) -> None
```

<a id="unreal.OpenColorIODisplayView"></a>