## MovieGraphMetadataAttribute Objects

```python
class MovieGraphMetadataAttribute(StructBase)
```

Represents a metadata attribute that can be included in a file.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSetMetadataAttributesNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write] Enable state. If disabled, this metadata attribute won't be added to the file.
- ``name`` (str):  [Read-Write] The name of the metadata attribute.
- ``value`` (str):  [Read-Write] The value of the metadata attribute.

<a id="unreal.MovieGraphMetadataAttribute.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             value: str = "",
             is_enabled: bool = False) -> None
```

<a id="unreal.MovieGraphMetadataAttribute.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] The name of the metadata attribute.

<a id="unreal.MovieGraphMetadataAttribute.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.MovieGraphMetadataAttribute.value"></a>

#### value

```python
@property
def value() -> str
```

(str):  [Read-Write] The value of the metadata attribute.

<a id="unreal.MovieGraphMetadataAttribute.value"></a>

#### value

```python
@value.setter
def value(value: str) -> None
```

<a id="unreal.MovieGraphMetadataAttribute.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable state. If disabled, this metadata attribute won't be added to the file.

<a id="unreal.MovieGraphMetadataAttribute.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.MovieGraphBranch"></a>