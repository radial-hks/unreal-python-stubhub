## MovieGraphPropertyInfo Objects

```python
class MovieGraphPropertyInfo(StructBase)
```

Information about a property that currently is (or can be) exposed on a node.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_menu_name`` (Text):  [Read-Write] The display name of the property which will be shown in the context menu. If empty, the value from 'Name' will be used.
- ``is_dynamic_property`` (bool):  [Read-Write] Whether this property is dynamic (ie, it does not correspond to a native UPROPERTY on the node).
- ``name`` (Name):  [Read-Write] The name of the property.
- ``promotion_name`` (Name):  [Read-Write] If this property is promoted, this is the name of the variable that is created. If empty, the value from 'Name' will be used.
- ``value_type`` (MovieGraphValueType):  [Read-Write] The type of the value pointed to by the property.

<a id="unreal.MovieGraphPropertyInfo.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             context_menu_name: Text = "",
             promotion_name: Name = "None",
             is_dynamic_property: bool = False,
             value_type: MovieGraphValueType = 0) -> None
```

<a id="unreal.MovieGraphPropertyInfo.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] The name of the property.

<a id="unreal.MovieGraphPropertyInfo.context_menu_name"></a>

#### context_menu_name

```python
@property
def context_menu_name() -> Text
```

(Text):  [Read-Only] The display name of the property which will be shown in the context menu. If empty, the value from 'Name' will be used.

<a id="unreal.MovieGraphPropertyInfo.promotion_name"></a>

#### promotion_name

```python
@property
def promotion_name() -> Name
```

(Name):  [Read-Only] If this property is promoted, this is the name of the variable that is created. If empty, the value from 'Name' will be used.

<a id="unreal.MovieGraphPropertyInfo.is_dynamic_property"></a>

#### is_dynamic_property

```python
@property
def is_dynamic_property() -> bool
```

(bool):  [Read-Only] Whether this property is dynamic (ie, it does not correspond to a native UPROPERTY on the node).

<a id="unreal.MovieGraphPropertyInfo.value_type"></a>

#### value_type

```python
@property
def value_type() -> MovieGraphValueType
```

(MovieGraphValueType):  [Read-Only] The type of the value pointed to by the property.

<a id="unreal.MovieGraphPinProperties"></a>