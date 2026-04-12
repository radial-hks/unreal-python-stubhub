## PythonBPAssetLib Objects

```python
class PythonBPAssetLib(BlueprintFunctionLibrary)
```

Python BPAsset Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonBPAssetLib.h

<a id="unreal.PythonBPAssetLib.log_schema"></a>

#### log\_schema

```python
@classmethod
def log_schema(cls, blueprint: Blueprint) -> None
```

X.log_schema(blueprint) -> None
Log Schema

Args:
    blueprint (Blueprint):

<a id="unreal.PythonBPAssetLib.log_all_schemas"></a>

#### log\_all\_schemas

```python
@classmethod
def log_all_schemas(cls) -> Array[Class]
```

X.log_all_schemas() -> Array[type(Class)]
Log all available Schemas, and return UClass array
note: add in v1.2.0

Returns:
    Array[type(Class)]: The UClass array

<a id="unreal.PythonBPAssetLib.log_all_k2_nodes"></a>

#### log\_all\_k2\_nodes

```python
@classmethod
def log_all_k2_nodes(cls) -> None
```

X.log_all_k2_nodes() -> None
Log All K2Nodes

<a id="unreal.PythonBPAssetLib.get_selected_nodes"></a>

#### get\_selected\_nodes

```python
@classmethod
def get_selected_nodes(cls, blueprint: Blueprint) -> None
```

X.get_selected_nodes(blueprint) -> None
Get Selected Nodes

Args:
    blueprint (Blueprint):

<a id="unreal.PythonBPAssetLib.get_graph_node_by_name"></a>

#### get\_graph\_node\_by\_name

```python
@classmethod
def get_graph_node_by_name(cls, name: str) -> Class
```

X.get_graph_node_by_name(name) -> type(Class)
Get Graph Node by Name

Args:
    name (str): 

Returns:
    type(Class):

<a id="unreal.PythonBPAssetLib.get_classes_from_module"></a>

#### get\_classes\_from\_module

```python
@classmethod
def get_classes_from_module(cls, module_name: Name) -> Array[Object]
```

X.get_classes_from_module(module_name) -> Array[Object]
Get the UClass from the specified module name
note: add in v1.2.0

Args:
    module_name (Name): The module name

Returns:
    Array[Object]: The UClass array

<a id="unreal.PythonBPAssetLib.get_children_classes"></a>

#### get\_children\_classes

```python
@classmethod
def get_children_classes(cls, class_: Class) -> Array[Class]
```

X.get_children_classes(class_) -> Array[type(Class)]
Get the children classes from the specified UClass
note: add in v1.2.0

Args:
    class_ (type(Class)): The UClass

Returns:
    Array[type(Class)]: The UClass array of children classes

<a id="unreal.PythonBPAssetLib.get_bp_functions_spawners"></a>

#### get\_bp\_functions\_spawners

```python
@classmethod
def get_bp_functions_spawners(cls, class_in: Class = None) -> Array[Object]
```

X.get_bp_functions_spawners(class_in=None) -> Array[Object]
Get the UFunction from the specified UClass
note: add in v1.2.0

Args:
    class_in (type(Class)): The UClass

Returns:
    Array[Object]: The UFunction array

<a id="unreal.PythonBPAssetLib.get_bp_function_spawner"></a>

#### get\_bp\_function\_spawner

```python
@classmethod
def get_bp_function_spawner(cls, class_in: Class,
                            function_name: str) -> Object
```

X.get_bp_function_spawner(class_in, function_name) -> Object
Get the Spawner of the specified Blueprint function name, used to create nodes in SGraphPanel
note: add in v1.2.0

Args:
    class_in (type(Class)): The UClass
    function_name (str): The function name

Returns:
    Object: The Spawner of the specified Blueprint function name

<a id="unreal.PythonBPAssetLib.get_all_k2_nodes"></a>

#### get\_all\_k2\_nodes

```python
@classmethod
def get_all_k2_nodes(cls) -> None
```

X.get_all_k2_nodes() -> None
Get All K2Nodes

<a id="unreal.PythonBPLib"></a>