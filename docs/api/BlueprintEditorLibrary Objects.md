## BlueprintEditorLibrary Objects

```python
class BlueprintEditorLibrary(BlueprintFunctionLibrary)
```

Blueprint Editor Library

**C++ Source:**

- **Module**: BlueprintEditorLibrary
- **File**: BlueprintEditorLibrary.h

<a id="unreal.BlueprintEditorLibrary.upgrade_operator_nodes"></a>

#### upgrade_operator_nodes

```python
@classmethod
def upgrade_operator_nodes(cls, blueprint: Blueprint) -> None
```

X.upgrade_operator_nodes(blueprint) -> None
Replace any old operator nodes (float + float, vector + float, int + vector, etc)
with the newer Promotable Operator version of the node. Preserve any connections the
original node had to the newer version of the node.

Args:
    blueprint (Blueprint): Blueprint to upgrade

<a id="unreal.BlueprintEditorLibrary.set_blueprint_variable_instance_editable"></a>

#### set_blueprint_variable_instance_editable

```python
@classmethod
def set_blueprint_variable_instance_editable(cls, blueprint: Blueprint,
                                             variable_name: Name,
                                             instance_editable: bool) -> None
```

X.set_blueprint_variable_instance_editable(blueprint, variable_name, instance_editable) -> None
Sets "Instance Editable" to true/false on a Blueprint variable

Args:
    blueprint (Blueprint): The blueprint object
    variable_name (Name): The variable name
    instance_editable (bool): Toggle InstanceEditable

<a id="unreal.BlueprintEditorLibrary.set_blueprint_variable_expose_to_cinematics"></a>

#### set_blueprint_variable_expose_to_cinematics

```python
@classmethod
def set_blueprint_variable_expose_to_cinematics(
        cls, blueprint: Blueprint, variable_name: Name,
        expose_to_cinematics: bool) -> None
```

X.set_blueprint_variable_expose_to_cinematics(blueprint, variable_name, expose_to_cinematics) -> None
Sets "Expose To Cinematics" to true/false on a Blueprint variable

Args:
    blueprint (Blueprint): The blueprint object
    variable_name (Name): The variable name
    expose_to_cinematics (bool): Set to true to expose to cinematics

<a id="unreal.BlueprintEditorLibrary.set_blueprint_variable_expose_on_spawn"></a>

#### set_blueprint_variable_expose_on_spawn

```python
@classmethod
def set_blueprint_variable_expose_on_spawn(cls, blueprint: Blueprint,
                                           variable_name: Name,
                                           expose_on_spawn: bool) -> None
```

X.set_blueprint_variable_expose_on_spawn(blueprint, variable_name, expose_on_spawn) -> None
Sets "Expose On Spawn" to true/false on a Blueprint variable

Args:
    blueprint (Blueprint): The blueprint object
    variable_name (Name): The variable name
    expose_on_spawn (bool): Set to true to expose on spawn

<a id="unreal.BlueprintEditorLibrary.replace_variable_references"></a>

#### replace_variable_references

```python
@classmethod
def replace_variable_references(cls, blueprint: Blueprint, old_var_name: Name,
                                new_var_name: Name) -> None
```

X.replace_variable_references(blueprint, old_var_name, new_var_name) -> None
Replace any references of variables with the OldVarName to references of those with the NewVarName if possible

Args:
    blueprint (Blueprint): Blueprint to replace the variable references on
    old_var_name (Name): The variable you want replaced
    new_var_name (Name): The new variable that will be used in the old one's place

<a id="unreal.BlueprintEditorLibrary.reparent_blueprint"></a>

#### reparent_blueprint

```python
@classmethod
def reparent_blueprint(cls, blueprint: Blueprint,
                       new_parent_class: Class) -> None
```

X.reparent_blueprint(blueprint, new_parent_class) -> None
Attempts to reparent the given blueprint to the new chosen parent class.

Args:
    blueprint (Blueprint): Blueprint that you would like to reparent
    new_parent_class (type(Class)): The new parent class to use

<a id="unreal.BlueprintEditorLibrary.rename_graph"></a>

#### rename_graph

```python
@classmethod
def rename_graph(cls, graph: EdGraph, new_name_str: str = "NewGraph") -> None
```

X.rename_graph(graph, new_name_str="NewGraph") -> None
Attempts to rename the given graph with a new name

Args:
    graph (EdGraph): The graph to rename
    new_name_str (str): The new name of the graph

<a id="unreal.BlueprintEditorLibrary.remove_unused_variables"></a>

#### remove_unused_variables

```python
@classmethod
def remove_unused_variables(cls, blueprint: Blueprint) -> int
```

X.remove_unused_variables(blueprint) -> int32
Deletes any unused blueprint created variables the given blueprint.
An Unused variable is any BP variable that is not referenced in any
blueprint graphs

Args:
    blueprint (Blueprint): Blueprint that you would like to remove variables from

Returns:
    int32: Number of variables removed

<a id="unreal.BlueprintEditorLibrary.remove_unused_nodes"></a>

#### remove_unused_nodes

```python
@classmethod
def remove_unused_nodes(cls, blueprint: Blueprint) -> None
```

X.remove_unused_nodes(blueprint) -> None
Remove any nodes in this blueprint that have no connections made to them.

Args:
    blueprint (Blueprint): The blueprint to remove the nodes from

<a id="unreal.BlueprintEditorLibrary.remove_graph"></a>

#### remove_graph

```python
@classmethod
def remove_graph(cls, blueprint: Blueprint, graph: EdGraph) -> None
```

X.remove_graph(blueprint, graph) -> None
Removes the given graph from the blueprint if possible

Args:
    blueprint (Blueprint): The blueprint the graph will be removed from
    graph (EdGraph): The graph to remove

<a id="unreal.BlueprintEditorLibrary.remove_function_graph"></a>

#### remove_function_graph

```python
@classmethod
def remove_function_graph(cls, blueprint: Blueprint, func_name: Name) -> None
```

X.remove_function_graph(blueprint, func_name) -> None
Deletes the function of the given name on this blueprint. Does NOT replace function call sites.

Args:
    blueprint (Blueprint): The blueprint to remove the function from
    func_name (Name): The name of the function to remove

<a id="unreal.BlueprintEditorLibrary.refresh_open_editors_for_blueprint"></a>

#### refresh_open_editors_for_blueprint

```python
@classmethod
def refresh_open_editors_for_blueprint(cls, bp: Blueprint) -> None
```

X.refresh_open_editors_for_blueprint(bp) -> None
Attempt to refresh any open blueprint editors for the given asset

Args:
    bp (Blueprint):

<a id="unreal.BlueprintEditorLibrary.refresh_all_open_blueprint_editors"></a>

#### refresh_all_open_blueprint_editors

```python
@classmethod
def refresh_all_open_blueprint_editors(cls) -> None
```

X.refresh_all_open_blueprint_editors() -> None
Refresh any open blueprint editors

<a id="unreal.BlueprintEditorLibrary.get_struct_type"></a>

#### get_struct_type

```python
@classmethod
def get_struct_type(cls, struct_type: ScriptStruct) -> EdGraphPinType
```

X.get_struct_type(struct_type) -> EdGraphPinType


Args:
    struct_type (ScriptStruct): 

Returns:
    EdGraphPinType: a pintype for the provided struct - returns 'int' type if invalid struct is provided

<a id="unreal.BlueprintEditorLibrary.get_set_type"></a>

#### get_set_type

```python
@classmethod
def get_set_type(cls, contained_type: EdGraphPinType) -> EdGraphPinType
```

X.get_set_type(contained_type) -> EdGraphPinType


Args:
    contained_type (EdGraphPinType): 

Returns:
    EdGraphPinType: a set of ContainedType type - returns 'int' type if invalid type is provided

<a id="unreal.BlueprintEditorLibrary.get_object_reference_type"></a>

#### get_object_reference_type

```python
@classmethod
def get_object_reference_type(cls, object_type: Class) -> EdGraphPinType
```

X.get_object_reference_type(object_type) -> EdGraphPinType


Args:
    object_type (type(Class)): 

Returns:
    EdGraphPinType: a object reference pintype for the provided class - returns 'int' type if invalid object type is provided

<a id="unreal.BlueprintEditorLibrary.get_map_type"></a>

#### get_map_type

```python
@classmethod
def get_map_type(cls, key_type: EdGraphPinType,
                 value_type: EdGraphPinType) -> EdGraphPinType
```

X.get_map_type(key_type, value_type) -> EdGraphPinType


Args:
    key_type (EdGraphPinType): 
    value_type (EdGraphPinType): 

Returns:
    EdGraphPinType: a map of KeyType to ValueType type - returns 'int' type if invalid type is provided

<a id="unreal.BlueprintEditorLibrary.get_class_reference_type"></a>

#### get_class_reference_type

```python
@classmethod
def get_class_reference_type(cls, class_type: Class) -> EdGraphPinType
```

X.get_class_reference_type(class_type) -> EdGraphPinType


Args:
    class_type (type(Class)): 

Returns:
    EdGraphPinType: a class reference pintype for the provided class - returns 'int' type if invalid class is provided

<a id="unreal.BlueprintEditorLibrary.get_blueprint_asset"></a>

#### get_blueprint_asset

```python
@classmethod
def get_blueprint_asset(cls, object: Object) -> Blueprint
```

X.get_blueprint_asset(object) -> Blueprint
Casts the provided Object to a Blueprint - the root asset type of a blueprint asset. Note
that the blueprint asset itself is editor only and not present in cooked assets.

Args:
    object (Object): The object we need to get the UBlueprint from

Returns:
    Blueprint: UBlueprint*   The blueprint type of the given object, nullptr if the object is not a blueprint.

<a id="unreal.BlueprintEditorLibrary.get_basic_type_by_name"></a>

#### get_basic_type_by_name

```python
@classmethod
def get_basic_type_by_name(cls, type_name: Name) -> EdGraphPinType
```

X.get_basic_type_by_name(type_name) -> EdGraphPinType


Args:
    type_name (Name): 

Returns:
    EdGraphPinType: a pintype for 'int', 'byte', 'bool', 'real', 'name', 'string' or 'text' - returns 'int' type if invalid type is provided

<a id="unreal.BlueprintEditorLibrary.get_array_type"></a>

#### get_array_type

```python
@classmethod
def get_array_type(cls, contained_type: EdGraphPinType) -> EdGraphPinType
```

X.get_array_type(contained_type) -> EdGraphPinType


Args:
    contained_type (EdGraphPinType): 

Returns:
    EdGraphPinType: a array of ContainedType type - returns 'int' type if invalid type is provided

<a id="unreal.BlueprintEditorLibrary.generated_class"></a>

#### generated_class

```python
@classmethod
def generated_class(cls, blueprint_obj: Blueprint) -> Class
```

X.generated_class(blueprint_obj) -> type(Class)
Gets the class generated when this blueprint is compiled

Args:
    blueprint_obj (Blueprint): The blueprint object

Returns:
    type(Class): UClass*                      The generated class

<a id="unreal.BlueprintEditorLibrary.find_graph"></a>

#### find_graph

```python
@classmethod
def find_graph(cls, blueprint: Blueprint, graph_name: Name) -> EdGraph
```

X.find_graph(blueprint, graph_name) -> EdGraph
Finds the graph with the given name on the blueprint. Null if it doesn't have one.

Args:
    blueprint (Blueprint): Blueprint to search
    graph_name (Name): The name of the graph to search for

Returns:
    EdGraph: UEdGraph*             Pointer to the graph with the given name, null if not found

<a id="unreal.BlueprintEditorLibrary.find_event_graph"></a>

#### find_event_graph

```python
@classmethod
def find_event_graph(cls, blueprint: Blueprint) -> EdGraph
```

X.find_event_graph(blueprint) -> EdGraph
Finds the event graph of the given blueprint. Null if it doesn't have one. This will only return
the primary event graph of the blueprint (the graph named "EventGraph").

Args:
    blueprint (Blueprint): Blueprint to search for the event graph on

Returns:
    EdGraph: UEdGraph*             Event graph of the blueprint if it has one, null if it doesn't have one

<a id="unreal.BlueprintEditorLibrary.create_blueprint_asset_with_parent"></a>

#### create_blueprint_asset_with_parent

```python
@classmethod
def create_blueprint_asset_with_parent(cls, asset_path: str,
                                       parent_class: Class) -> Blueprint
```

X.create_blueprint_asset_with_parent(asset_path, parent_class) -> Blueprint
Creates a blueprint based on a specific parent, honoring registered custom blueprint types

Args:
    asset_path (str): The full path that the asset should be created with
    parent_class (type(Class)): The parent class that the blueprint should be based on

Returns:
    Blueprint:

<a id="unreal.BlueprintEditorLibrary.compile_blueprint"></a>

#### compile_blueprint

```python
@classmethod
def compile_blueprint(cls, blueprint: Blueprint) -> None
```

X.compile_blueprint(blueprint) -> None
Compiles the given blueprint.

Args:
    blueprint (Blueprint): Blueprint to compile

<a id="unreal.BlueprintEditorLibrary.add_member_variable"></a>

#### add_member_variable

```python
@classmethod
def add_member_variable(cls, blueprint: Blueprint, member_name: Name,
                        variable_type: EdGraphPinType) -> bool
```

X.add_member_variable(blueprint, member_name, variable_type) -> bool
Adds a member variable to the specified blueprint with the specified type.

Args:
    blueprint (Blueprint): 
    member_name (Name): 
    variable_type (EdGraphPinType): 

Returns:
    bool: true if it succeeds, false if it fails.

<a id="unreal.BlueprintEditorLibrary.add_function_graph"></a>

#### add_function_graph

```python
@classmethod
def add_function_graph(cls,
                       blueprint: Blueprint,
                       func_name: str = "NewFunction") -> EdGraph
```

X.add_function_graph(blueprint, func_name="NewFunction") -> EdGraph
Adds a function to the given blueprint

Args:
    blueprint (Blueprint): The blueprint to add the function to
    func_name (str): Name of the function to add

Returns:
    EdGraph: UEdGraph*

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenu"></a>