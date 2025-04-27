## MovieGraphNode Objects

```python
class MovieGraphNode(Object)
```

This is a base class for all nodes that can exist in the UMovieGraphConfig network.
In the editor, each node in the network will have an editor-only representation too
which contains data about it's visual position in the graph, comments, etc.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphNode.script_tags"></a>

#### script_tags

```python
@property
def script_tags() -> Array[str]
```

(Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphNode.script_tags"></a>

#### script_tags

```python
@script_tags.setter
def script_tags(value: Array[str]) -> None
```

<a id="unreal.MovieGraphNode.toggle_promote_property_to_pin"></a>

#### toggle_promote_property_to_pin

```python
def toggle_promote_property_to_pin(property_name: Name) -> None
```

x.toggle_promote_property_to_pin(property_name) -> None
Toggles the promotion of the property with the given name to a pin on the node.

Args:
    property_name (Name):

<a id="unreal.MovieGraphNode.set_node_pos_y"></a>

#### set_node_pos_y

```python
def set_node_pos_y(node_pos_y: int) -> None
```

x.set_node_pos_y(node_pos_y) -> None
Set Node Pos Y

Args:
    node_pos_y (int32):

<a id="unreal.MovieGraphNode.set_node_pos_x"></a>

#### set_node_pos_x

```python
def set_node_pos_x(node_pos_x: int) -> None
```

x.set_node_pos_x(node_pos_x) -> None
Set Node Pos X

Args:
    node_pos_x (int32):

<a id="unreal.MovieGraphNode.set_node_comment"></a>

#### set_node_comment

```python
def set_node_comment(node_comment: str) -> None
```

x.set_node_comment(node_comment) -> None
Set Node Comment

Args:
    node_comment (str):

<a id="unreal.MovieGraphNode.set_is_comment_bubble_visible"></a>

#### set_is_comment_bubble_visible

```python
def set_is_comment_bubble_visible(is_visible: int) -> None
```

x.set_is_comment_bubble_visible(is_visible) -> None
Set Is Comment Bubble Visible

Args:
    is_visible (uint8):

<a id="unreal.MovieGraphNode.set_is_comment_bubble_pinned"></a>

#### set_is_comment_bubble_pinned

```python
def set_is_comment_bubble_pinned(is_pinned: int) -> None
```

x.set_is_comment_bubble_pinned(is_pinned) -> None
Set Is Comment Bubble Pinned

Args:
    is_pinned (uint8):

<a id="unreal.MovieGraphNode.set_disabled"></a>

#### set_disabled

```python
def set_disabled(new_disable_state: bool) -> None
```

x.set_disabled(new_disable_state) -> None
Set whether this node is currently disabled.

Args:
    new_disable_state (bool):

<a id="unreal.MovieGraphNode.is_disabled"></a>

#### is_disabled

```python
def is_disabled() -> bool
```

x.is_disabled() -> bool
Determines if this node is currently disabled.

Returns:
    bool:

<a id="unreal.MovieGraphNode.is_comment_bubble_visible"></a>

#### is_comment_bubble_visible

```python
def is_comment_bubble_visible() -> bool
```

x.is_comment_bubble_visible() -> bool
Is Comment Bubble Visible

Returns:
    bool:

<a id="unreal.MovieGraphNode.is_comment_bubble_pinned"></a>

#### is_comment_bubble_pinned

```python
def is_comment_bubble_pinned() -> bool
```

x.is_comment_bubble_pinned() -> bool
Is Comment Bubble Pinned

Returns:
    bool:

<a id="unreal.MovieGraphNode.get_overrideable_property_info"></a>

#### get_overrideable_property_info

```python
def get_overrideable_property_info() -> Array[MovieGraphPropertyInfo]
```

x.get_overrideable_property_info() -> Array[MovieGraphPropertyInfo]
Gets the information about properties which can be exposed as a pin on the node.

Returns:
    Array[MovieGraphPropertyInfo]:

<a id="unreal.MovieGraphNode.get_output_pins"></a>

#### get_output_pins

```python
def get_output_pins() -> Array[MovieGraphPin]
```

x.get_output_pins() -> Array[MovieGraphPin]
Gets all output pins on the node. Note that the returned array is const, so output pins cannot be added/removed from the node via this array.

Returns:
    Array[MovieGraphPin]:

<a id="unreal.MovieGraphNode.get_output_pin_properties"></a>

#### get_output_pin_properties

```python
def get_output_pin_properties() -> Array[MovieGraphPinProperties]
```

x.get_output_pin_properties() -> Array[MovieGraphPinProperties]
Gets the properties for all output pins.

Returns:
    Array[MovieGraphPinProperties]:

<a id="unreal.MovieGraphNode.get_output_pin"></a>

#### get_output_pin

```python
def get_output_pin(pin_label: Name) -> MovieGraphPin
```

x.get_output_pin(pin_label) -> MovieGraphPin
Gets the output pin with the specified name, or nullptr if one could not be found.

Args:
    pin_label (Name): 

Returns:
    MovieGraphPin:

<a id="unreal.MovieGraphNode.get_node_title"></a>

#### get_node_title

```python
def get_node_title(get_descriptive: bool = False) -> Text
```

x.get_node_title(get_descriptive=False) -> Text
Gets the node's title. Optionally gets a more descriptive, multi-line title for the node if bGetDescriptive is
set to true.

Args:
    get_descriptive (bool): 

Returns:
    Text:

<a id="unreal.MovieGraphNode.get_node_pos_y"></a>

#### get_node_pos_y

```python
def get_node_pos_y() -> int
```

x.get_node_pos_y() -> int32
Get Node Pos Y

Returns:
    int32:

<a id="unreal.MovieGraphNode.get_node_pos_x"></a>

#### get_node_pos_x

```python
def get_node_pos_x() -> int
```

x.get_node_pos_x() -> int32
Get Node Pos X

Returns:
    int32:

<a id="unreal.MovieGraphNode.get_node_comment"></a>

#### get_node_comment

```python
def get_node_comment() -> str
```

x.get_node_comment() -> str
Get Node Comment

Returns:
    str:

<a id="unreal.MovieGraphNode.get_menu_category"></a>

#### get_menu_category

```python
def get_menu_category() -> Text
```

x.get_menu_category() -> Text
Gets the category that the node belongs under.

Returns:
    Text:

<a id="unreal.MovieGraphNode.get_keywords"></a>

#### get_keywords

```python
def get_keywords() -> Text
```

x.get_keywords() -> Text
Gets the keywords (space-separated) that will be searched in the node creation context menu.

Returns:
    Text:

<a id="unreal.MovieGraphNode.get_input_pins"></a>

#### get_input_pins

```python
def get_input_pins() -> Array[MovieGraphPin]
```

x.get_input_pins() -> Array[MovieGraphPin]
Gets all input pins on the node. Note that the returned array is const, so input pins cannot be added/removed from the node via this array.

Returns:
    Array[MovieGraphPin]:

<a id="unreal.MovieGraphNode.get_input_pin_properties"></a>

#### get_input_pin_properties

```python
def get_input_pin_properties() -> Array[MovieGraphPinProperties]
```

x.get_input_pin_properties() -> Array[MovieGraphPinProperties]
Gets the properties for all input pins.

Returns:
    Array[MovieGraphPinProperties]:

<a id="unreal.MovieGraphNode.get_input_pin"></a>

#### get_input_pin

```python
def get_input_pin(
    pin_label: Name,
    pin_requirement:
    MovieGraphPinQueryRequirement = MovieGraphPinQueryRequirement.
    BUILT_IN_OR_DYNAMIC
) -> MovieGraphPin
```

x.get_input_pin(pin_label, pin_requirement=MovieGraphPinQueryRequirement.BUILT_IN_OR_DYNAMIC) -> MovieGraphPin
Gets the input pin with the specified name, or nullptr if one could not be found. Most pins on a node are
"built-in", meaning they ship with the node. Dynamic pins (pins which are not built-in) can potentially have the
same name as a built-in (eg, the option pins on the Select node). To disambiguate between built-in and dynamic
pins, specify bIsBuiltInPin = false if trying to fetch a pin that is not built-in.

Args:
    pin_label (Name): 
    pin_requirement (MovieGraphPinQueryRequirement): 

Returns:
    MovieGraphPin:

<a id="unreal.MovieGraphNode.get_first_connected_output_pin"></a>

#### get_first_connected_output_pin

```python
def get_first_connected_output_pin() -> MovieGraphPin
```

x.get_first_connected_output_pin() -> MovieGraphPin
Gets the first output pin on the node which has a connection, or nullptr if no pins are connected.

Returns:
    MovieGraphPin:

<a id="unreal.MovieGraphNode.get_first_connected_input_pin"></a>

#### get_first_connected_input_pin

```python
def get_first_connected_input_pin() -> MovieGraphPin
```

x.get_first_connected_input_pin() -> MovieGraphPin
Gets the first input pin on the node which has a connection, or nullptr if no pins are connected.

Returns:
    MovieGraphPin:

<a id="unreal.MovieGraphNode.get_exposed_properties"></a>

#### get_exposed_properties

```python
def get_exposed_properties() -> Array[MovieGraphPropertyInfo]
```

x.get_exposed_properties() -> Array[MovieGraphPropertyInfo]
Gets the information about properties which are currently exposed as pins on the node.

Returns:
    Array[MovieGraphPropertyInfo]:

<a id="unreal.MovieGraphNode.get_branch_restriction"></a>

#### get_branch_restriction

```python
def get_branch_restriction() -> MovieGraphBranchRestriction
```

x.get_branch_restriction() -> MovieGraphBranchRestriction
Determines which types of branches the node can be created in.

Returns:
    MovieGraphBranchRestriction:

<a id="unreal.MovieGraphNode.can_be_disabled"></a>

#### can_be_disabled

```python
def can_be_disabled() -> bool
```

x.can_be_disabled() -> bool
Determines if this node can be disabled.

Returns:
    bool:

<a id="unreal.MovieGraphNode.can_be_added_by_user"></a>

#### can_be_added_by_user

```python
def can_be_added_by_user() -> bool
```

x.can_be_added_by_user() -> bool
Determines if this node type can be added to the graph interactively by a user or via the API when constructing a graph.

Returns:
    bool: true if the object can be added via the API, false otherwise

<a id="unreal.MovieGraphSettingNode"></a>