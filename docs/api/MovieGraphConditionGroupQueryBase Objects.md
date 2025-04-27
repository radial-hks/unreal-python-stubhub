## MovieGraphConditionGroupQueryBase Objects

```python
class MovieGraphConditionGroupQueryBase(Object)
```

Base class that all condition group queries must inherit from.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphConditionGroupQueryBase.should_hide_property_names"></a>

#### should_hide_property_names

```python
def should_hide_property_names() -> bool
```

x.should_hide_property_names() -> bool
Determines if the public properties on the query class will have their names hidden in the details panel. Returns
false by default. Most query subclasses will only have one property and do not need to clutter the UI with the
property name (eg, the "Actor Name" query only shows one text box with entries for the actor names, no need to
show the property name).

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroupQueryBase.set_operation_type"></a>

#### set_operation_type

```python
def set_operation_type(
        operation_type: MovieGraphConditionGroupQueryOpType) -> None
```

x.set_operation_type(operation_type) -> None
Sets how the condition group query interacts with the condition group. This call is ignored for the first query
in the condition group (the first is always Union).

Args:
    operation_type (MovieGraphConditionGroupQueryOpType):

<a id="unreal.MovieGraphConditionGroupQueryBase.set_enabled"></a>

#### set_enabled

```python
def set_enabled(enabled: bool) -> None
```

x.set_enabled(enabled) -> None
Sets whether this query is enabled.

Args:
    enabled (bool):

<a id="unreal.MovieGraphConditionGroupQueryBase.is_first_condition_group_query"></a>

#### is_first_condition_group_query

```python
def is_first_condition_group_query() -> bool
```

x.is_first_condition_group_query() -> bool
Determines if this is the first condition group query under the parent condition group.

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroupQueryBase.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Determines if this query is enabled.

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroupQueryBase.is_editor_only_query"></a>

#### is_editor_only_query

```python
def is_editor_only_query() -> bool
```

x.is_editor_only_query() -> bool
Determines if this query is only respected when run within the editor. Used for providing a UI hint.

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroupQueryBase.get_operation_type"></a>

#### get_operation_type

```python
def get_operation_type() -> MovieGraphConditionGroupQueryOpType
```

x.get_operation_type() -> MovieGraphConditionGroupQueryOpType
Gets the condition group query operation type.

Returns:
    MovieGraphConditionGroupQueryOpType:

<a id="unreal.MovieGraphConditionGroupQueryBase.evaluate"></a>

#### evaluate

```python
def evaluate(actors_to_query: Array[Actor], world: World) -> Set[Actor]
```

x.evaluate(actors_to_query, world) -> Set[Actor]
Determines which of the provided actors (in the given world) match the query. Matches are added to OutMatchingActors.

Args:
    actors_to_query (Array[Actor]): 
    world (World): 

Returns:
    Set[Actor]: 

    out_matching_actors (Set[Actor]):

<a id="unreal.MovieGraphConditionGroupQuery_Actor"></a>