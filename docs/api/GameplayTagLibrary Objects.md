## GameplayTagLibrary Objects

```python
class GameplayTagLibrary(BlueprintFunctionLibrary)
```

Blueprint Gameplay Tag Library

**C++ Source:**

- **Module**: GameplayTags
- **File**: BlueprintGameplayTagLibrary.h

<a id="unreal.GameplayTagLibrary.remove_gameplay_tag"></a>

#### remove_gameplay_tag

```python
@classmethod
def remove_gameplay_tag(cls, tag_container: GameplayTagContainer,
                        tag: GameplayTag) -> Optional[GameplayTagContainer]
```

X.remove_gameplay_tag(tag_container, tag) -> GameplayTagContainer or None
Remove a single tag from the passed in tag container, returns true if found

Args:
    tag_container (GameplayTagContainer): 
    tag (GameplayTag): The tag to add to the container

Returns:
    GameplayTagContainer or None: 

    tag_container (GameplayTagContainer):

<a id="unreal.GameplayTagLibrary.not_equal_gameplay_tag_container"></a>

#### not_equal_gameplay_tag_container

```python
@classmethod
def not_equal_gameplay_tag_container(cls, a: GameplayTagContainer,
                                     b: GameplayTagContainer) -> bool
```

X.not_equal_gameplay_tag_container(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (GameplayTagContainer): 
    b (GameplayTagContainer): 

Returns:
    bool:

<a id="unreal.GameplayTagLibrary.not_equal_gameplay_tag"></a>

#### not_equal_gameplay_tag

```python
@classmethod
def not_equal_gameplay_tag(cls, a: GameplayTag, b: GameplayTag) -> bool
```

X.not_equal_gameplay_tag(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (GameplayTag): 
    b (GameplayTag): 

Returns:
    bool:

<a id="unreal.GameplayTagLibrary.matches_tag"></a>

#### matches_tag

```python
@classmethod
def matches_tag(cls, tag_one: GameplayTag, tag_two: GameplayTag,
                exact_match: bool) -> bool
```

X.matches_tag(tag_one, tag_two, exact_match) -> bool
Determine if TagOne matches against TagTwo

Args:
    tag_one (GameplayTag): Tag to check for match
    tag_two (GameplayTag): Tag to check match against
    exact_match (bool): If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching

Returns:
    bool: True if TagOne matches TagTwo

<a id="unreal.GameplayTagLibrary.do_gameplay_tags_match"></a>

#### do_gameplay_tags_match

```python
@classmethod
def do_gameplay_tags_match(cls, tag_one: GameplayTag, tag_two: GameplayTag,
                           exact_match: bool) -> bool
```

deprecated: 'do_gameplay_tags_match' was renamed to 'matches_tag'.

<a id="unreal.GameplayTagLibrary.matches_any_tags"></a>

#### matches_any_tags

```python
@classmethod
def matches_any_tags(cls, tag_one: GameplayTag,
                     other_container: GameplayTagContainer,
                     exact_match: bool) -> bool
```

X.matches_any_tags(tag_one, other_container, exact_match) -> bool
Determine if TagOne matches against any tag in OtherContainer

Args:
    tag_one (GameplayTag): Tag to check for match
    other_container (GameplayTagContainer): Container to check against.
    exact_match (bool): If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching

Returns:
    bool: True if TagOne matches any tags explicitly present in OtherContainer

<a id="unreal.GameplayTagLibrary.make_literal_gameplay_tag_container"></a>

#### make_literal_gameplay_tag_container

```python
@classmethod
def make_literal_gameplay_tag_container(
        cls, value: GameplayTagContainer) -> GameplayTagContainer
```

X.make_literal_gameplay_tag_container(value) -> GameplayTagContainer
Creates a literal FGameplayTagContainer

Args:
    value (GameplayTagContainer): 

Returns:
    GameplayTagContainer:

<a id="unreal.GameplayTagLibrary.make_literal_gameplay_tag"></a>

#### make_literal_gameplay_tag

```python
@classmethod
def make_literal_gameplay_tag(cls, value: GameplayTag) -> GameplayTag
```

X.make_literal_gameplay_tag(value) -> GameplayTag
Creates a literal FGameplayTag

Args:
    value (GameplayTag): 

Returns:
    GameplayTag:

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_query_match_no_tags"></a>

#### make_gameplay_tag_query_match_no_tags

```python
@classmethod
def make_gameplay_tag_query_match_no_tags(
        cls, tags: GameplayTagContainer) -> GameplayTagQuery
```

X.make_gameplay_tag_query_match_no_tags(tags) -> GameplayTagQuery
Creates a literal FGameplayTagQuery with a prepopulated NoTagsMatch expression

Args:
    tags (GameplayTagContainer): value to set the FGameplayTagQuery expression

Returns:
    GameplayTagQuery: The literal FGameplayTagQuery

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_query_match_any_tags"></a>

#### make_gameplay_tag_query_match_any_tags

```python
@classmethod
def make_gameplay_tag_query_match_any_tags(
        cls, tags: GameplayTagContainer) -> GameplayTagQuery
```

X.make_gameplay_tag_query_match_any_tags(tags) -> GameplayTagQuery
Creates a literal FGameplayTagQuery with a prepopulated AnyTagsMatch expression

Args:
    tags (GameplayTagContainer): value to set the FGameplayTagQuery expression

Returns:
    GameplayTagQuery: The literal FGameplayTagQuery

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_query_match_all_tags"></a>

#### make_gameplay_tag_query_match_all_tags

```python
@classmethod
def make_gameplay_tag_query_match_all_tags(
        cls, tags: GameplayTagContainer) -> GameplayTagQuery
```

X.make_gameplay_tag_query_match_all_tags(tags) -> GameplayTagQuery
Creates a literal FGameplayTagQuery with a prepopulated AllTagsMatch expression

Args:
    tags (GameplayTagContainer): value to set the FGameplayTagQuery expression

Returns:
    GameplayTagQuery: The literal FGameplayTagQuery

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_query"></a>

#### make_gameplay_tag_query

```python
@classmethod
def make_gameplay_tag_query(cls,
                            tag_query: GameplayTagQuery) -> GameplayTagQuery
```

X.make_gameplay_tag_query(tag_query) -> GameplayTagQuery
Creates a literal FGameplayTagQuery

Args:
    tag_query (GameplayTagQuery): value to set the FGameplayTagQuery to

Returns:
    GameplayTagQuery: The literal FGameplayTagQuery

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_container_from_tag"></a>

#### make_gameplay_tag_container_from_tag

```python
@classmethod
def make_gameplay_tag_container_from_tag(
        cls, single_tag: GameplayTag) -> GameplayTagContainer
```

X.make_gameplay_tag_container_from_tag(single_tag) -> GameplayTagContainer
Creates a FGameplayTagContainer containing a single tag

Args:
    single_tag (GameplayTag): 

Returns:
    GameplayTagContainer:

<a id="unreal.GameplayTagLibrary.make_gameplay_tag_container_from_array"></a>

#### make_gameplay_tag_container_from_array

```python
@classmethod
def make_gameplay_tag_container_from_array(
        cls, gameplay_tags: Array[GameplayTag]) -> GameplayTagContainer
```

X.make_gameplay_tag_container_from_array(gameplay_tags) -> GameplayTagContainer
Creates a FGameplayTagContainer from the array of passed in tags

Args:
    gameplay_tags (Array[GameplayTag]): 

Returns:
    GameplayTagContainer:

<a id="unreal.GameplayTagLibrary.is_tag_query_empty"></a>

#### is_tag_query_empty

```python
@classmethod
def is_tag_query_empty(cls, tag_query: GameplayTagQuery) -> bool
```

X.is_tag_query_empty(tag_query) -> bool
Check if the specified tag query is empty

Args:
    tag_query (GameplayTagQuery): Query to check

Returns:
    bool: True if the query is empty, false otherwise.

<a id="unreal.GameplayTagLibrary.is_gameplay_tag_valid"></a>

#### is_gameplay_tag_valid

```python
@classmethod
def is_gameplay_tag_valid(cls, gameplay_tag: GameplayTag) -> bool
```

X.is_gameplay_tag_valid(gameplay_tag) -> bool
Returns true if the passed in gameplay tag is non-null

Args:
    gameplay_tag (GameplayTag): 

Returns:
    bool:

<a id="unreal.GameplayTagLibrary.has_tag"></a>

#### has_tag

```python
@classmethod
def has_tag(cls, tag_container: GameplayTagContainer, tag: GameplayTag,
            exact_match: bool) -> bool
```

X.has_tag(tag_container, tag, exact_match) -> bool
Check if the tag container has the specified tag

Args:
    tag_container (GameplayTagContainer): Container to check for the tag
    tag (GameplayTag): Tag to check for in the container
    exact_match (bool): If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

Returns:
    bool: True if the container has the specified tag, false if it does not

<a id="unreal.GameplayTagLibrary.does_container_have_tag"></a>

#### does_container_have_tag

```python
@classmethod
def does_container_have_tag(cls, tag_container: GameplayTagContainer,
                            tag: GameplayTag, exact_match: bool) -> bool
```

deprecated: 'does_container_have_tag' was renamed to 'has_tag'.

<a id="unreal.GameplayTagLibrary.has_any_tags"></a>

#### has_any_tags

```python
@classmethod
def has_any_tags(cls, tag_container: GameplayTagContainer,
                 other_container: GameplayTagContainer,
                 exact_match: bool) -> bool
```

X.has_any_tags(tag_container, other_container, exact_match) -> bool
Check if the specified tag container has ANY of the tags in the other container

Args:
    tag_container (GameplayTagContainer): Container to check if it matches any of the tags in the other container
    other_container (GameplayTagContainer): Container to check against.
    exact_match (bool): If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

Returns:
    bool: True if the container has ANY of the tags in the other container

<a id="unreal.GameplayTagLibrary.does_container_match_any_tags_in_container"></a>

#### does_container_match_any_tags_in_container

```python
@classmethod
def does_container_match_any_tags_in_container(
        cls, tag_container: GameplayTagContainer,
        other_container: GameplayTagContainer, exact_match: bool) -> bool
```

deprecated: 'does_container_match_any_tags_in_container' was renamed to 'has_any_tags'.

<a id="unreal.GameplayTagLibrary.has_all_tags"></a>

#### has_all_tags

```python
@classmethod
def has_all_tags(cls, tag_container: GameplayTagContainer,
                 other_container: GameplayTagContainer,
                 exact_match: bool) -> bool
```

X.has_all_tags(tag_container, other_container, exact_match) -> bool
Check if the specified tag container has ALL of the tags in the other container

Args:
    tag_container (GameplayTagContainer): Container to check if it matches all of the tags in the other container
    other_container (GameplayTagContainer): Container to check against. If this is empty, the check will succeed
    exact_match (bool): If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching

Returns:
    bool: True if the container has ALL of the tags in the other container

<a id="unreal.GameplayTagLibrary.does_container_match_all_tags_in_container"></a>

#### does_container_match_all_tags_in_container

```python
@classmethod
def does_container_match_all_tags_in_container(
        cls, tag_container: GameplayTagContainer,
        other_container: GameplayTagContainer, exact_match: bool) -> bool
```

deprecated: 'does_container_match_all_tags_in_container' was renamed to 'has_all_tags'.

<a id="unreal.GameplayTagLibrary.get_tag_name"></a>

#### get_tag_name

```python
@classmethod
def get_tag_name(cls, gameplay_tag: GameplayTag) -> Name
```

X.get_tag_name(gameplay_tag) -> Name
Returns FName of this tag

Args:
    gameplay_tag (GameplayTag): 

Returns:
    Name:

<a id="unreal.GameplayTagLibrary.get_owned_gameplay_tags"></a>

#### get_owned_gameplay_tags

```python
@classmethod
def get_owned_gameplay_tags(
    cls, tag_container_interface: GameplayTagAssetInterface
) -> GameplayTagContainer
```

X.get_owned_gameplay_tags(tag_container_interface) -> GameplayTagContainer


Args:
    tag_container_interface (GameplayTagAssetInterface): 

Returns:
    GameplayTagContainer: the tags currently owned by the TagContainerInterface object

<a id="unreal.GameplayTagLibrary.get_num_gameplay_tags_in_container"></a>

#### get_num_gameplay_tags_in_container

```python
@classmethod
def get_num_gameplay_tags_in_container(
        cls, tag_container: GameplayTagContainer) -> int
```

X.get_num_gameplay_tags_in_container(tag_container) -> int32
Get the number of gameplay tags in the specified container

Args:
    tag_container (GameplayTagContainer): Tag container to get the number of tags from

Returns:
    int32: The number of tags in the specified container

<a id="unreal.GameplayTagLibrary.get_debug_string_from_gameplay_tag_container"></a>

#### get_debug_string_from_gameplay_tag_container

```python
@classmethod
def get_debug_string_from_gameplay_tag_container(
        cls, tag_container: GameplayTagContainer) -> str
```

X.get_debug_string_from_gameplay_tag_container(tag_container) -> str
Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

Args:
    tag_container (GameplayTagContainer): The tag container to get the debug string from.

Returns:
    str:

<a id="unreal.GameplayTagLibrary.get_debug_string_from_gameplay_tag"></a>

#### get_debug_string_from_gameplay_tag

```python
@classmethod
def get_debug_string_from_gameplay_tag(cls, gameplay_tag: GameplayTag) -> str
```

X.get_debug_string_from_gameplay_tag(gameplay_tag) -> str
Returns an FString representation of a gameplay tag for debugging purposes.

Args:
    gameplay_tag (GameplayTag): The tag to get the debug string from.

Returns:
    str:

<a id="unreal.GameplayTagLibrary.get_all_actors_of_class_matching_tag_query"></a>

#### get_all_actors_of_class_matching_tag_query

```python
@classmethod
def get_all_actors_of_class_matching_tag_query(
        cls, world_context_object: Object, actor_class: Class,
        gameplay_tag_query: GameplayTagQuery) -> Array[Actor]
```

X.get_all_actors_of_class_matching_tag_query(world_context_object, actor_class, gameplay_tag_query) -> Array[Actor]
Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

Args:
    world_context_object (Object): 
    actor_class (type(Class)): Class of actors to fetch
    gameplay_tag_query (GameplayTagQuery): Query to match against

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.GameplayTagLibrary.equal_equal_gameplay_tag_container"></a>

#### equal_equal_gameplay_tag_container

```python
@classmethod
def equal_equal_gameplay_tag_container(cls, a: GameplayTagContainer,
                                       b: GameplayTagContainer) -> bool
```

X.equal_equal_gameplay_tag_container(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (GameplayTagContainer): 
    b (GameplayTagContainer): 

Returns:
    bool:

<a id="unreal.GameplayTagLibrary.equal_equal_gameplay_tag"></a>

#### equal_equal_gameplay_tag

```python
@classmethod
def equal_equal_gameplay_tag(cls, a: GameplayTag, b: GameplayTag) -> bool
```

X.equal_equal_gameplay_tag(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (GameplayTag): 
    b (GameplayTag): 

Returns:
    bool:

<a id="unreal.GameplayTagLibrary.does_container_match_tag_query"></a>

#### does_container_match_tag_query

```python
@classmethod
def does_container_match_tag_query(cls, tag_container: GameplayTagContainer,
                                   tag_query: GameplayTagQuery) -> bool
```

X.does_container_match_tag_query(tag_container, tag_query) -> bool
Check if the specified tag container matches the given Tag Query

Args:
    tag_container (GameplayTagContainer): Container to check if it matches all of the tags in the other container
    tag_query (GameplayTagQuery): Query to match against

Returns:
    bool: True if the container matches the query, false otherwise.

<a id="unreal.GameplayTagLibrary.conv_object_to_gameplay_tag_asset_interface"></a>

#### conv_object_to_gameplay_tag_asset_interface

```python
@classmethod
def conv_object_to_gameplay_tag_asset_interface(
        cls, object: Object) -> GameplayTagAssetInterface
```

X.conv_object_to_gameplay_tag_asset_interface(object) -> GameplayTagAssetInterface
Converts a UObject to a GameplayTagAssetInterface. This specialty Autocast function exists so we can auto-convert the GameplayTagAssetInterface member functions to static Blueprint functions using redirects.

Args:
    object (Object): 

Returns:
    GameplayTagAssetInterface:

<a id="unreal.GameplayTagLibrary.break_gameplay_tag_container"></a>

#### break_gameplay_tag_container

```python
@classmethod
def break_gameplay_tag_container(
        cls,
        gameplay_tag_container: GameplayTagContainer) -> Array[GameplayTag]
```

X.break_gameplay_tag_container(gameplay_tag_container) -> Array[GameplayTag]
Breaks tag container into explicit array of tags

Args:
    gameplay_tag_container (GameplayTagContainer): 

Returns:
    Array[GameplayTag]: 

    gameplay_tags (Array[GameplayTag]):

<a id="unreal.GameplayTagLibrary.append_gameplay_tag_containers"></a>

#### append_gameplay_tag_containers

```python
@classmethod
def append_gameplay_tag_containers(
        cls, out_tag_container: GameplayTagContainer,
        tag_container: GameplayTagContainer) -> GameplayTagContainer
```

X.append_gameplay_tag_containers(out_tag_container, tag_container) -> GameplayTagContainer
Appends all tags in the InTagContainer to InOutTagContainer

Args:
    out_tag_container (GameplayTagContainer): The container that will be appended too.
    tag_container (GameplayTagContainer): The container to append.

Returns:
    GameplayTagContainer: 

    out_tag_container (GameplayTagContainer): The container that will be appended too.

<a id="unreal.GameplayTagLibrary.add_gameplay_tag"></a>

#### add_gameplay_tag

```python
@classmethod
def add_gameplay_tag(cls, tag_container: GameplayTagContainer,
                     tag: GameplayTag) -> GameplayTagContainer
```

X.add_gameplay_tag(tag_container, tag) -> GameplayTagContainer
Adds a single tag to the passed in tag container

Args:
    tag_container (GameplayTagContainer): 
    tag (GameplayTag): The tag to add to the container

Returns:
    GameplayTagContainer: 

    tag_container (GameplayTagContainer):

<a id="unreal.GameplayTagLibrary.add_gameplay_tag_to_container"></a>

#### add_gameplay_tag_to_container

```python
@classmethod
def add_gameplay_tag_to_container(cls, tag_container: GameplayTagContainer,
                                  tag: GameplayTag) -> GameplayTagContainer
```

deprecated: 'add_gameplay_tag_to_container' was renamed to 'add_gameplay_tag'.

<a id="unreal.GameplayTagAssetInterface"></a>