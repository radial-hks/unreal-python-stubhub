## PythonStructLib Objects

```python
class PythonStructLib(BlueprintFunctionLibrary)
```

Python Struct Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonStructLib.h

<a id="unreal.PythonStructLib.rename_variable"></a>

#### rename\_variable

```python
@classmethod
def rename_variable(cls, struct: UserDefinedStruct, var_guid: Guid,
                    new_friendly_name: str) -> bool
```

X.rename_variable(struct, var_guid, new_friendly_name) -> bool
Rename Variable

Args:
    struct (UserDefinedStruct): 
    var_guid (Guid): 
    new_friendly_name (str): 

Returns:
    bool:

<a id="unreal.PythonStructLib.remove_variable_by_name"></a>

#### remove\_variable\_by\_name

```python
@classmethod
def remove_variable_by_name(cls, struct: UserDefinedStruct,
                            var_name: Name) -> bool
```

X.remove_variable_by_name(struct, var_name) -> bool
Remove the specified Variable in User Defined Struct by property name.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to modify.
    var_name (Name): The Property name of the variable.

Returns:
    bool: None

<a id="unreal.PythonStructLib.log_var_desc_by_friendly_name"></a>

#### log\_var\_desc\_by\_friendly\_name

```python
@classmethod
def log_var_desc_by_friendly_name(cls, struct: UserDefinedStruct,
                                  var_name: str) -> None
```

X.log_var_desc_by_friendly_name(struct, var_name) -> None
Print out the detail info of the specified Variable of User Defined Struct.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.
    var_name (str): The friend name of the specified variable.

<a id="unreal.PythonStructLib.log_var_desc"></a>

#### log\_var\_desc

```python
@classmethod
def log_var_desc(cls, struct: UserDefinedStruct) -> None
```

X.log_var_desc(struct) -> None
Print out the detail infos of the given User Defined Struct. Include VarName, Category, Guid, PinValue and so on.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.

<a id="unreal.PythonStructLib.is_unique_friendly_name"></a>

#### is\_unique\_friendly\_name

```python
@classmethod
def is_unique_friendly_name(cls, struct: UserDefinedStruct,
                            friendly_name: str) -> bool
```

X.is_unique_friendly_name(struct, friendly_name) -> bool
Query is the Friendly Name unique or not.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.
    friendly_name (str): The New Friendly Name

Returns:
    bool: True if the friendly name is unique in the struct.

<a id="unreal.PythonStructLib.get_variable_names"></a>

#### get\_variable\_names

```python
@classmethod
def get_variable_names(cls, struct: UserDefinedStruct) -> Array[Name]
```

X.get_variable_names(struct) -> Array[Name]
Get the Variable Names of specified User Defined Struct.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.

Returns:
    Array[Name]: The variable name list.

<a id="unreal.PythonStructLib.get_variable_description"></a>

#### get\_variable\_description

```python
@classmethod
def get_variable_description(cls, struct: UserDefinedStruct,
                             friendly_name: str) -> Map[str, str]
```

X.get_variable_description(struct, friendly_name) -> Map[str, str]
Get the content of VariableDescription of the specified Variable in User Defined Struct.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.
    friendly_name (str): The friend name of the specified variable.

Returns:
    Map[str, str]: The content of VariableDescription as a Key, Value String Map.

<a id="unreal.PythonStructLib.get_variable_default_value"></a>

#### get\_variable\_default\_value

```python
@classmethod
def get_variable_default_value(cls, struct: UserDefinedStruct,
                               var_guid: Guid) -> str
```

X.get_variable_default_value(struct, var_guid) -> str
Get Variable Default Value

Args:
    struct (UserDefinedStruct): 
    var_guid (Guid): 

Returns:
    str:

<a id="unreal.PythonStructLib.get_guid_from_property_name"></a>

#### get\_guid\_from\_property\_name

```python
@classmethod
def get_guid_from_property_name(cls, name: Name) -> Guid
```

X.get_guid_from_property_name(name) -> Guid
Get the Guid of specified Variable in User Defined Struct by property name.
note: The Guid of a Property Name is independent of which struct it belongs to

Args:
    name (Name): The Property name of the Property variable.

Returns:
    Guid: The Guid of the variable.

<a id="unreal.PythonStructLib.get_guid_from_friendly_name"></a>

#### get\_guid\_from\_friendly\_name

```python
@classmethod
def get_guid_from_friendly_name(cls, struct: UserDefinedStruct,
                                friendly_name: str) -> Guid
```

X.get_guid_from_friendly_name(struct, friendly_name) -> Guid
Get the Guid of specified Variable in User Defined Struct by friendly name.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.
    friendly_name (str): The friendly name of the variable.

Returns:
    Guid: The Guid of the variable.

<a id="unreal.PythonStructLib.get_friendly_names"></a>

#### get\_friendly\_names

```python
@classmethod
def get_friendly_names(cls, struct: UserDefinedStruct) -> Array[str]
```

X.get_friendly_names(struct) -> Array[str]
Get the Friendly Names of specified User Defined Struct.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to query.

Returns:
    Array[str]: The friendly names list.

<a id="unreal.PythonStructLib.change_variable_default_value"></a>

#### change\_variable\_default\_value

```python
@classmethod
def change_variable_default_value(cls, struct: UserDefinedStruct,
                                  var_guid: Guid,
                                  new_default_value: str) -> bool
```

X.change_variable_default_value(struct, var_guid, new_default_value) -> bool
Modify the default value of specified Variable in User Defined Struct.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to modify.
    var_guid (Guid): The Guid of the variable.
    new_default_value (str): The new default value in string format.

Returns:
    bool: True if the default value has been set

<a id="unreal.PythonStructLib.add_variable"></a>

#### add\_variable

```python
@classmethod
def add_variable(cls,
                 struct: UserDefinedStruct,
                 category: Name = "PythonEditor",
                 sub_category: Name = ...,
                 sub_category_object: Object = ...,
                 container_type_value: int = ...,
                 is_reference: bool = False,
                 friendly_name: str = "") -> bool
```

X.add_variable(struct, category="PythonEditor", sub_category, sub_category_object, container_type_value, is_reference=False, friendly_name="") -> bool
Add a new variable to specified User Defined Struct
note: More example can be found in the website, or print out a exists variable with log_var_desc_by_friendly_name for reference.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to modify.
    category (Name): The Category of the new Variable
    sub_category (Name): The SubCategory of the new Variable
    sub_category_object (Object): The SubCategoryObject of the new Variable
    container_type_value (int32): Container type. 0: single, 1: array, 2: set. Use add_directory_variable if you want add a dict variable
    is_reference (bool): Whether e new Variable passed as reference
    friendly_name (str): Friendly name of the new variable

Returns:
    bool: True if the new variable has been added

<a id="unreal.PythonStructLib.add_directory_variable"></a>

#### add\_directory\_variable

```python
@classmethod
def add_directory_variable(cls,
                           struct: UserDefinedStruct,
                           category: Name = "PythonEditor",
                           sub_category: Name = ...,
                           sub_category_object: Object = ...,
                           terminal_category: Name = ...,
                           terminal_sub_category: Name = ...,
                           terminal_sub_category_object: Object = ...,
                           is_reference: bool = False,
                           friendly_name: str = "") -> bool
```

X.add_directory_variable(struct, category="PythonEditor", sub_category, sub_category_object, terminal_category, terminal_sub_category, terminal_sub_category_object, is_reference=False, friendly_name="") -> bool
Add a new variable to specified User Defined Struct
note: More example can be found in the website, or print out a exists variable with log_var_desc_by_friendly_name for reference.

Args:
    struct (UserDefinedStruct): The User Defined Struct you want to modify.
    category (Name): The Category of the new Variable's key
    sub_category (Name): The SubCategory of the new Variable's key
    sub_category_object (Object): The SubCategoryObject of the new Variable's key
    terminal_category (Name): The Category of the new Variable's value
    terminal_sub_category (Name): The SubCategory of the new Variable's value
    terminal_sub_category_object (Object): The SubCategoryObject of the new Variable's value
    is_reference (bool): Whether e new Variable passed as reference
    friendly_name (str): Friendly name of the new variable

Returns:
    bool: True if the new variable has been added

<a id="unreal.PythonTestLib"></a>