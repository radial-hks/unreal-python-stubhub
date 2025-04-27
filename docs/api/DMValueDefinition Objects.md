## DMValueDefinition Objects

```python
class DMValueDefinition(StructBase)
```

Stores information about basic value types, such as EDMValueType::Float1.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMValueDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_names`` (Array[Text]):  [Read-Only]
- ``display_name`` (Text):  [Read-Only]
- ``float_count`` (uint8):  [Read-Only]
- ``type`` (DMValueType):  [Read-Only]
- ``value_class`` (type(Class)):  [Read-Only]

<a id="unreal.DMValueDefinition.__init__"></a>

#### __init__

```python
def __init__(type: DMValueType = DMValueType.VT_NONE,
             float_count: int = 0,
             display_name: Text = "",
             channel_names: Array[Text] = [],
             value_class: Class = None) -> None
```

<a id="unreal.DMValueDefinition.type"></a>

#### type

```python
@property
def type() -> DMValueType
```

(DMValueType):  [Read-Only]

<a id="unreal.DMValueDefinition.float_count"></a>

#### float_count

```python
@property
def float_count() -> int
```

(uint8):  [Read-Only]

<a id="unreal.DMValueDefinition.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.DMValueDefinition.channel_names"></a>

#### channel_names

```python
@property
def channel_names() -> Array[Text]
```

(Array[Text]):  [Read-Only]

<a id="unreal.DMValueDefinition.value_class"></a>

#### value_class

```python
@property
def value_class() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.DMMaterialTexture"></a>