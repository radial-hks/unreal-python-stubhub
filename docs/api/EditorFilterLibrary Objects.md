## EditorFilterLibrary Objects

```python
class EditorFilterLibrary(BlueprintFunctionLibrary)
```

Utility class to filter a list of objects. Object should be in the World Editor.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorFilterLibrary.h

<a id="unreal.EditorFilterLibrary.by_selection"></a>

#### by_selection

```python
@classmethod
def by_selection(
    cls,
    target_array: Array[Actor],
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Actor]
```

X.by_selection(target_array, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Actor]
Filter the array based on Object's selection.

Args:
    target_array (Array[Actor]): Array of Object to filter. The array will not change.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Actor]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_level_name"></a>

#### by_level_name

```python
@classmethod
def by_level_name(
    cls,
    target_array: Array[Actor],
    level_name: Name,
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Actor]
```

X.by_level_name(target_array, level_name, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Actor]
Filter the array by Level the Actor belongs to.

Args:
    target_array (Array[Actor]): Array of Actor to filter. The array will not change.
    level_name (Name): The name of the Level the actor belongs to (same name as in the ContentBrowser).
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Actor]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_layer"></a>

#### by_layer

```python
@classmethod
def by_layer(
    cls,
    target_array: Array[Actor],
    layer_name: Name,
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Actor]
```

X.by_layer(target_array, layer_name, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Actor]
Filter the array by Layer the Actor belongs to.

Args:
    target_array (Array[Actor]): Array of Actor to filter. The array will not change.
    layer_name (Name): The exact name of the Layer the actor belongs to.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Actor]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_id_name"></a>

#### by_id_name

```python
@classmethod
def by_id_name(
    cls,
    target_array: Array[Object],
    name_sub_string: str,
    string_match:
    EditorScriptingStringMatchType = EditorScriptingStringMatchType.CONTAINS,
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Object]
```

X.by_id_name(target_array, name_sub_string, string_match=EditorScriptingStringMatchType.CONTAINS, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Object]
Filter the array based on the Object's ID name.

Args:
    target_array (Array[Object]): Array of Object to filter. The array will not change.
    name_sub_string (str): The text the Object's ID name.
    string_match (EditorScriptingStringMatchType): Contains the NameSubString OR matches with the wildcard *? OR exactly the same value.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Object]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_class"></a>

#### by_class

```python
@classmethod
def by_class(
    cls,
    target_array: Array[Object],
    object_class: Class,
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Object]
```

X.by_class(target_array, object_class, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Object]
Filter the array based on the Object's class.

Args:
    target_array (Array[Object]): Array of Object to filter. The array will not change.
    object_class (type(Class)): The Class of the object.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Object]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_actor_tag"></a>

#### by_actor_tag

```python
@classmethod
def by_actor_tag(
    cls,
    target_array: Array[Actor],
    tag: Name,
    filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE
) -> Array[Actor]
```

X.by_actor_tag(target_array, tag, filter_type=EditorScriptingFilterType.INCLUDE) -> Array[Actor]
Filter the array by Tag the Actor contains

Args:
    target_array (Array[Actor]): Array of Actor to filter. The array will not change.
    tag (Name): The exact name of the Tag the actor contains.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.

Returns:
    Array[Actor]: The filtered list.

<a id="unreal.EditorFilterLibrary.by_actor_label"></a>

#### by_actor_label

```python
@classmethod
def by_actor_label(
        cls,
        target_array: Array[Actor],
        name_sub_string: str,
        string_match:
    EditorScriptingStringMatchType = EditorScriptingStringMatchType.CONTAINS,
        filter_type: EditorScriptingFilterType = EditorScriptingFilterType.
    INCLUDE,
        ignore_case: bool = True) -> Array[Actor]
```

X.by_actor_label(target_array, name_sub_string, string_match=EditorScriptingStringMatchType.CONTAINS, filter_type=EditorScriptingFilterType.INCLUDE, ignore_case=True) -> Array[Actor]
Filter the array based on the Actor's label (what we see in the editor)

Args:
    target_array (Array[Actor]): Array of Actor to filter. The array will not change.
    name_sub_string (str): The text the Actor's Label.
    string_match (EditorScriptingStringMatchType): Contains the NameSubString OR matches with the wildcard *? OR exactly the same value.
    filter_type (EditorScriptingFilterType): Should include or not the array's item if it respects the condition.
    ignore_case (bool): Determines case sensitivity options for string comparisons.

Returns:
    Array[Actor]: The filtered list.

<a id="unreal.EditorLevelLibrary"></a>