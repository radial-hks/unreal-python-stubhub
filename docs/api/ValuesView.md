## ValuesView

<a id="unreal._T"></a>

#### _T

<a id="unreal._ElemType"></a>

#### _ElemType

<a id="unreal._KeyType"></a>

#### _KeyType

<a id="unreal._ValueType"></a>

#### _ValueType

<a id="unreal._ValueType"></a>

#### _ValueType

<a id="unreal._EngineSubsystemTypeVar"></a>

#### _EngineSubsystemTypeVar

<a id="unreal._EditorSubsystemTypeVar"></a>

#### _EditorSubsystemTypeVar

<a id="unreal.log"></a>

#### log

```python
def log(arg: Any) -> None
```

log(arg: Any) -> None -- log the given argument as information in the LogPython category

<a id="unreal.log_warning"></a>

#### log_warning

```python
def log_warning(arg: Any) -> None
```

log_warning(arg: Any) -> None -- log the given argument as a warning in the LogPython category

<a id="unreal.log_error"></a>

#### log_error

```python
def log_error(arg: Any) -> None
```

log_error(arg: Any) -> None -- log the given argument as an error in the LogPython category

<a id="unreal.log_flush"></a>

#### log_flush

```python
def log_flush() -> None
```

log_flush() -> None -- flush the log to disk.

<a id="unreal.reload"></a>

#### reload

```python
def reload(module: str) -> None
```

reload(module: str) -> None -- reload the given Unreal Python module.

<a id="unreal.load_module"></a>

#### load_module

```python
def load_module(module: str) -> None
```

load_module(module: str) -> None -- load the given Unreal module and generate any Python code for its reflected types

<a id="unreal.new_object"></a>

#### new_object

```python
def new_object(type: Union[Class, type],
               outer: Optional[Object] = None,
               name: Union[Name, str] = "",
               base_type: Optional[Object] = None) -> Any
```

new_object(type: Union[Class, type], outer: Optional[Object]=None, name: Union[Name, str]="", base_type: Optional[Object]=None) -> Any -- create an Unreal object of the given class (and optional outer and name), optionally validating its type

<a id="unreal.find_object"></a>

#### find_object

```python
def find_object(outer: Optional[Object],
                name: str,
                type: Union[Class, type] = Object.static_class(),
                follow_redirectors: bool = True) -> Any
```

find_object(outer: Optional[Object], name: str, type: Union[Class, type]=Object.static_class(), follow_redirectors: bool=True) -> Any -- find an already loaded Unreal object with the given outer and name, optionally validating its type

<a id="unreal.load_object"></a>

#### load_object

```python
def load_object(outer: Optional[Object],
                name: str,
                type: Union[Class, type] = Object.static_class(),
                follow_redirectors: bool = True) -> Any
```

load_object(outer: Optional[Object], name: str, type: Union[Class, type]=Object.static_class(), follow_redirectors: bool=True) -> Any -- load an Unreal object with the given outer and name, optionally validating its type

<a id="unreal.load_class"></a>

#### load_class

```python
def load_class(
    outer: Optional[Object],
    name: str,
    type: Union[Class, type] = Object.static_class()
) -> Optional[Class]
```

load_class(outer: Optional[Object], name: str, type: Union[Class, type]=Object.static_class()) -> Optional[Class] -- load an Unreal class with the given outer and name, optionally validating its base type

<a id="unreal.find_asset"></a>

#### find_asset

```python
def find_asset(name: str,
               type: Union[Class, type] = Object.static_class(),
               follow_redirectors: bool = True) -> Any
```

find_asset(name: str, type: Union[Class, type]=Object.static_class(), follow_redirectors: bool = True) -> Any -- find an already loaded Unreal asset with the given name, optionally validating its type

<a id="unreal.load_asset"></a>

#### load_asset

```python
def load_asset(name: str,
               type: Union[Class, type] = Object.static_class(),
               follow_redirectors: bool = True) -> Any
```

load_asset(name: str, type: Union[Class, type]=Object.static_class(), follow_redirectors: bool = True) -> Any -- load an Unreal asset with the given name, optionally validating its type

<a id="unreal.find_package"></a>

#### find_package

```python
def find_package(name: str) -> Optional[Package]
```

find_package(name: str) -> Optional[Package] -- find an already loaded Unreal package with the given name

<a id="unreal.load_package"></a>

#### load_package

```python
def load_package(name: str) -> Optional[Package]
```

load_package(name: str) -> Optional[Package] -- load an Unreal package with the given name

<a id="unreal.get_default_object"></a>

#### get_default_object

```python
def get_default_object(type: Union[Class, type]) -> Any
```

get_default_object(type: Union[Class, type]) -> Any -- get the Unreal class default object (CDO) of the given type

<a id="unreal.purge_object_references"></a>

#### purge_object_references

```python
def purge_object_references(obj: Object, include_inners: bool = True) -> None
```

purge_object_references(obj: Object, include_inners: bool = True) -> None -- purge all references to the given Unreal object from any living Python objects

<a id="unreal.generate_class"></a>

#### generate_class

```python
def generate_class(class_type: type) -> None
```

generate_class(class_type: type) -> None -- generate an Unreal class for the given Python type

<a id="unreal.generate_struct"></a>

#### generate_struct

```python
def generate_struct(struct_type: type) -> None
```

generate_struct(struct_type: type) -> None -- generate an Unreal struct for the given Python type

<a id="unreal.generate_enum"></a>

#### generate_enum

```python
def generate_enum(enum_type: type) -> None
```

generate_enum(enum_type: type) -> None -- generate an Unreal enum for the given Python type

<a id="unreal.flush_generated_type_reinstancing"></a>

#### flush_generated_type_reinstancing

```python
def flush_generated_type_reinstancing() -> None
```

flush_generated_type_reinstancing() -> None -- flush any pending reinstancing requests for Python generated types

<a id="unreal.get_type_from_class"></a>

#### get_type_from_class

```python
def get_type_from_class(class_: Class) -> type
```

get_type_from_class(class_: Class) -> type -- get the best matching Python type for the given Unreal class

<a id="unreal.get_type_from_struct"></a>

#### get_type_from_struct

```python
def get_type_from_struct(struct: Struct) -> type
```

get_type_from_struct(struct: Struct) -> type -- get the best matching Python type for the given Unreal struct

<a id="unreal.get_type_from_enum"></a>

#### get_type_from_enum

```python
def get_type_from_enum(enum: Enum) -> type
```

get_type_from_enum(enum: Enum) -> type -- get the best matching Python type for the given Unreal enum

<a id="unreal.register_python_shutdown_callback"></a>

#### register_python_shutdown_callback

```python
def register_python_shutdown_callback(callable: Callable[[], None]) -> object
```

register_python_shutdown_callback(callable: Callable[[], None]) -> object -- register the given callable (with no input arguments) as a callback to execute immediately before Python shutdown

<a id="unreal.unregister_python_shutdown_callback"></a>

#### unregister_python_shutdown_callback

```python
def unregister_python_shutdown_callback(handle: object) -> None
```

unregister_python_shutdown_callback(handle: object) -> None -- unregister the given handle from a previous call to register_python_shutdown_callback

<a id="unreal.NSLOCTEXT"></a>

#### NSLOCTEXT

```python
def NSLOCTEXT(ns: str, key: str, source: str) -> Text
```

NSLOCTEXT(ns: str, key: str, source: str) -> Text -- create a localized Text from the given namespace, key, and source string

<a id="unreal.LOCTABLE"></a>

#### LOCTABLE

```python
def LOCTABLE(id: Union[Name, str], key: str) -> Text
```

LOCTABLE(id: Union[Name, str], key: str) -> Text -- get a localized Text from the given string table id and key

<a id="unreal.is_editor"></a>

#### is_editor

```python
def is_editor() -> bool
```

is_editor() -> bool -- tells if the editor is running or not

<a id="unreal.get_interpreter_executable_path"></a>

#### get_interpreter_executable_path

```python
def get_interpreter_executable_path() -> str
```

get_interpreter_executable_path() -> str -- get the path to the Python interpreter executable of the Python SDK this plugin was compiled against

<a id="unreal.create_python_object_handle"></a>

#### create_python_object_handle

```python
def create_python_object_handle(
        obj: Optional[Any]) -> Optional[PythonObjectHandle]
```

create_python_object_handle(obj: Optional[Any]) -> Optional[PythonObjectHandle] -- create a PythonObjectHandle from the given PyObject

<a id="unreal.resolve_python_object_handle"></a>

#### resolve_python_object_handle

```python
def resolve_python_object_handle(
        handle: Optional[PythonObjectHandle]) -> Optional[Any]
```

resolve_python_object_handle(handle: Optional[PythonObjectHandle]) -> Optional[Any] -- resolve a PythonObjectHandle to its PyObject, or None

<a id="unreal.destroy_python_object_handle"></a>

#### destroy_python_object_handle

```python
def destroy_python_object_handle(*args)
```

destroy_python_object_handle(handle: Optional[PythonObjectHandle]) -- destroy a PythonObjectHandle (clearing its PyObject reference)

<a id="unreal.ScopedSlowTask"></a>