## MovieGraphPin Objects

```python
class MovieGraphPin(Object)
```

Movie Graph Pin

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphPin.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edges`` (Array[MovieGraphEdge]):  [Read-Write] A list of edges between pins. This is marked as TextExportTransient so that when we copy/paste nodes,
  we don't copy the edges, as they are rebuilt after paste based on the editor graph connections.
- ``node`` (MovieGraphNode):  [Read-Write] The node that this pin belongs to.
- ``properties`` (MovieGraphPinProperties):  [Read-Write]

<a id="unreal.MovieGraphPin.node"></a>

#### node

```python
@property
def node() -> MovieGraphNode
```

(MovieGraphNode):  [Read-Only] The node that this pin belongs to.

<a id="unreal.MovieGraphPin.properties"></a>

#### properties

```python
@property
def properties() -> MovieGraphPinProperties
```

(MovieGraphPinProperties):  [Read-Only]

<a id="unreal.MovieGraphPin.edges"></a>

#### edges

```python
@property
def edges() -> Array[MovieGraphEdge]
```

(Array[MovieGraphEdge]):  [Read-Only] A list of edges between pins. This is marked as TextExportTransient so that when we copy/paste nodes,
we don't copy the edges, as they are rebuilt after paste based on the editor graph connections.

<a id="unreal.MovieGraphPin.is_pin_direction_compatible_with"></a>

#### is_pin_direction_compatible_with

```python
def is_pin_direction_compatible_with(other_pin: MovieGraphPin) -> bool
```

x.is_pin_direction_compatible_with(other_pin) -> bool
Is Pin Direction Compatible With

Args:
    other_pin (MovieGraphPin): 

Returns:
    bool:

<a id="unreal.MovieGraphPin.is_output_pin"></a>

#### is_output_pin

```python
def is_output_pin() -> bool
```

x.is_output_pin() -> bool
Is Output Pin

Returns:
    bool:

<a id="unreal.MovieGraphPin.is_input_pin"></a>

#### is_input_pin

```python
def is_input_pin() -> bool
```

x.is_input_pin() -> bool
Is Input Pin

Returns:
    bool:

<a id="unreal.MovieGraphPin.is_connection_to_branch_allowed"></a>

#### is_connection_to_branch_allowed

```python
def is_connection_to_branch_allowed(
        other_pin: MovieGraphPin) -> Optional[Text]
```

x.is_connection_to_branch_allowed(other_pin) -> Text or None
Determines if the connection between this pin and OtherPin follows branch restriction rules. OutError is populated
with an error if the connection should be rejected and the function will return false.

Args:
    other_pin (MovieGraphPin): 

Returns:
    Text or None: 

    out_error (Text):

<a id="unreal.MovieGraphPin.is_connected"></a>

#### is_connected

```python
def is_connected() -> bool
```

x.is_connected() -> bool
Is Connected

Returns:
    bool:

<a id="unreal.MovieGraphPin.get_first_connected_pin"></a>

#### get_first_connected_pin

```python
def get_first_connected_pin() -> MovieGraphPin
```

x.get_first_connected_pin() -> MovieGraphPin
Gets the first pin connected to this pin. Returns nullptr if no valid connection exists.

Returns:
    MovieGraphPin:

<a id="unreal.MovieGraphPin.get_connected_nodes"></a>

#### get_connected_nodes

```python
def get_connected_nodes() -> Array[MovieGraphNode]
```

x.get_connected_nodes() -> Array[MovieGraphNode]
Utility function for scripting which gathers all of the nodes connected
to this particular pin. Equivalent to looping through all of the edges,
getting the connected pin, and then getting the node associated with that pin.

Returns:
    Array[MovieGraphNode]:

<a id="unreal.MovieGraphPin.get_all_connected_pins"></a>

#### get_all_connected_pins

```python
def get_all_connected_pins() -> Array[MovieGraphPin]
```

x.get_all_connected_pins() -> Array[MovieGraphPin]
Gets all connected pins.

Returns:
    Array[MovieGraphPin]:

<a id="unreal.MovieGraphPin.edge_count"></a>

#### edge_count

```python
def edge_count() -> int
```

x.edge_count() -> int32
Edge Count

Returns:
    int32:

<a id="unreal.MovieGraphPin.can_create_connection"></a>

#### can_create_connection

```python
def can_create_connection(other_pin: MovieGraphPin) -> bool
```

x.can_create_connection(other_pin) -> bool
Can Create Connection

Args:
    other_pin (MovieGraphPin): 

Returns:
    bool:

<a id="unreal.MovieGraphPin.allows_multiple_connections"></a>

#### allows_multiple_connections

```python
def allows_multiple_connections() -> bool
```

x.allows_multiple_connections() -> bool
Allows Multiple Connections

Returns:
    bool:

<a id="unreal.MoviePipelineBase"></a>