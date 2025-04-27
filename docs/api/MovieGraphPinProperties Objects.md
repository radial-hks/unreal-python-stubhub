## MovieGraphPinProperties Objects

```python
class MovieGraphPinProperties(StructBase)
```

Movie Graph Pin Properties

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphPin.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_multiple_connections`` (bool):  [Read-Write] Whether this pin can accept multiple connections.
- ``is_branch`` (bool):  [Read-Write] Whether this pin represents a branch. If it does not represent a branch, then it is a value-providing pin.
- ``is_built_in`` (bool):  [Read-Write] Whether this pin is built-in (ie, the pin ships with the node and cannot be removed). Option pins on the Select
  node would be an example of pins which are not built-in (they can be added and removed dynamically).
- ``label`` (Name):  [Read-Write] The name assigned to the pin.
- ``type`` (MovieGraphValueType):  [Read-Write] The type of the pin. If the pin represents a branch, this type is ignored.
- ``type_object`` (Object):  [Read-Write] The value type of the pin, if the type is an enum, struct, class, or object.

<a id="unreal.MovieGraphPinProperties.__init__"></a>

#### __init__

```python
def __init__(label: Name = "None",
             type: MovieGraphValueType = 0,
             type_object: Object = None,
             allow_multiple_connections: bool = False,
             is_branch: bool = False,
             is_built_in: bool = False) -> None
```

<a id="unreal.MovieGraphPinProperties.label"></a>

#### label

```python
@property
def label() -> Name
```

(Name):  [Read-Write] The name assigned to the pin.

<a id="unreal.MovieGraphPinProperties.label"></a>

#### label

```python
@label.setter
def label(value: Name) -> None
```

<a id="unreal.MovieGraphPinProperties.type"></a>

#### type

```python
@property
def type() -> MovieGraphValueType
```

(MovieGraphValueType):  [Read-Write] The type of the pin. If the pin represents a branch, this type is ignored.

<a id="unreal.MovieGraphPinProperties.type"></a>

#### type

```python
@type.setter
def type(value: MovieGraphValueType) -> None
```

<a id="unreal.MovieGraphPinProperties.type_object"></a>

#### type_object

```python
@property
def type_object() -> Object
```

(Object):  [Read-Write] The value type of the pin, if the type is an enum, struct, class, or object.

<a id="unreal.MovieGraphPinProperties.type_object"></a>

#### type_object

```python
@type_object.setter
def type_object(value: Object) -> None
```

<a id="unreal.MovieGraphPinProperties.allow_multiple_connections"></a>

#### allow_multiple_connections

```python
@property
def allow_multiple_connections() -> bool
```

(bool):  [Read-Write] Whether this pin can accept multiple connections.

<a id="unreal.MovieGraphPinProperties.allow_multiple_connections"></a>

#### allow_multiple_connections

```python
@allow_multiple_connections.setter
def allow_multiple_connections(value: bool) -> None
```

<a id="unreal.MovieGraphPinProperties.is_branch"></a>

#### is_branch

```python
@property
def is_branch() -> bool
```

(bool):  [Read-Write] Whether this pin represents a branch. If it does not represent a branch, then it is a value-providing pin.

<a id="unreal.MovieGraphPinProperties.is_branch"></a>

#### is_branch

```python
@is_branch.setter
def is_branch(value: bool) -> None
```

<a id="unreal.MovieGraphPinProperties.is_built_in"></a>

#### is_built_in

```python
@property
def is_built_in() -> bool
```

(bool):  [Read-Write] Whether this pin is built-in (ie, the pin ships with the node and cannot be removed). Option pins on the Select
node would be an example of pins which are not built-in (they can be added and removed dynamically).

<a id="unreal.MovieGraphPinProperties.is_built_in"></a>

#### is_built_in

```python
@is_built_in.setter
def is_built_in(value: bool) -> None
```

<a id="unreal.MovieGraphMetadataAttribute"></a>