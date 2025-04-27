## MovieGraphConditionGroup Objects

```python
class MovieGraphConditionGroup(Object)
```

A group of queries which can be added to a collection.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``op_type`` (MovieGraphConditionGroupOpType):  [Read-Write] The operation type that the condition group is using.
- ``queries`` (Array[MovieGraphConditionGroupQueryBase]):  [Read-Write] The queries that are contained within the condition group.

<a id="unreal.MovieGraphConditionGroup.set_operation_type"></a>

#### set_operation_type

```python
def set_operation_type(operation_type: MovieGraphConditionGroupOpType) -> None
```

x.set_operation_type(operation_type) -> None
Sets how the condition group interacts with the collection. This call is ignored for the first condition group
in the collection (the first is always Union).

Args:
    operation_type (MovieGraphConditionGroupOpType):

<a id="unreal.MovieGraphConditionGroup.remove_query"></a>

#### remove_query

```python
def remove_query(query: MovieGraphConditionGroupQueryBase) -> bool
```

x.remove_query(query) -> bool
Removes the specified query from the condition group if it exists. Returns true on success, else false.

Args:
    query (MovieGraphConditionGroupQueryBase): 

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroup.move_query_to_index"></a>

#### move_query_to_index

```python
def move_query_to_index(query: MovieGraphConditionGroupQueryBase,
                        new_index: int) -> bool
```

x.move_query_to_index(query, new_index) -> bool
Move the specified query to a new index within the condition group. Returns false if the query was not found or the index
specified is invalid, else true.

Args:
    query (MovieGraphConditionGroupQueryBase): 
    new_index (int32): 

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroup.is_first_condition_group"></a>

#### is_first_condition_group

```python
def is_first_condition_group() -> bool
```

x.is_first_condition_group() -> bool
Determines if this is the first condition group under the parent collection.

Returns:
    bool:

<a id="unreal.MovieGraphConditionGroup.get_queries"></a>

#### get_queries

```python
def get_queries() -> Array[MovieGraphConditionGroupQueryBase]
```

x.get_queries() -> Array[MovieGraphConditionGroupQueryBase]
Gets all queries currently contained in the condition group.

Returns:
    Array[MovieGraphConditionGroupQueryBase]:

<a id="unreal.MovieGraphConditionGroup.get_operation_type"></a>

#### get_operation_type

```python
def get_operation_type() -> MovieGraphConditionGroupOpType
```

x.get_operation_type() -> MovieGraphConditionGroupOpType
Gets the condition group operation type.

Returns:
    MovieGraphConditionGroupOpType:

<a id="unreal.MovieGraphConditionGroup.evaluate"></a>

#### evaluate

```python
def evaluate(world: World) -> Set[Actor]
```

x.evaluate(world) -> Set[Actor]
Determines the actors that match the condition group by running the queries contained in it.

Args:
    world (World): 

Returns:
    Set[Actor]:

<a id="unreal.MovieGraphConditionGroup.duplicate_query"></a>

#### duplicate_query

```python
def duplicate_query(query_index: int) -> MovieGraphConditionGroupQueryBase
```

x.duplicate_query(query_index) -> MovieGraphConditionGroupQueryBase
Duplicates the condition group query at the specified index. The duplicate is placed at the end of the query list. Returns the duplicate
query on success, else nullptr.

Args:
    query_index (int32): 

Returns:
    MovieGraphConditionGroupQueryBase:

<a id="unreal.MovieGraphConditionGroup.add_query"></a>

#### add_query

```python
def add_query(query_type: Class,
              insert_index: int = -1) -> MovieGraphConditionGroupQueryBase
```

x.add_query(query_type, insert_index=-1) -> MovieGraphConditionGroupQueryBase
Adds a new condition group query to the condition group and returns a ptr to it. The condition group owns the
created query. By default the query is added to the end, but an optional index can be provided if the query
should be placed in a specific location among the existing queries.

Args:
    query_type (type(Class)): 
    insert_index (int32): 

Returns:
    MovieGraphConditionGroupQueryBase:

<a id="unreal.MovieGraphCollection"></a>