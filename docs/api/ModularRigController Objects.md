## ModularRigController Objects

```python
class ModularRigController(Object)
```

Modular Rig Controller

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ModularRigController.h

<a id="unreal.ModularRigController.un_bind_module_variable"></a>

#### un_bind_module_variable

```python
def un_bind_module_variable(module_path: str,
                            variable_name: Name,
                            setup_undo: bool = True) -> bool
```

x.un_bind_module_variable(module_path, variable_name, setup_undo=True) -> bool
Un Bind Module Variable

Args:
    module_path (str): 
    variable_name (Name): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.swap_modules_of_class"></a>

#### swap_modules_of_class

```python
def swap_modules_of_class(old_class: Class,
                          new_class: Class,
                          setup_undo: bool = True) -> bool
```

x.swap_modules_of_class(old_class, new_class, setup_undo=True) -> bool
Swap Modules Of Class

Args:
    old_class (type(Class)): 
    new_class (type(Class)): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.swap_module_class"></a>

#### swap_module_class

```python
def swap_module_class(module_path: str,
                      new_class: Class,
                      setup_undo: bool = True) -> bool
```

x.swap_module_class(module_path, new_class, setup_undo=True) -> bool
Swap Module Class

Args:
    module_path (str): 
    new_class (type(Class)): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.set_module_short_name"></a>

#### set_module_short_name

```python
def set_module_short_name(module_path: str,
                          new_short_name: str,
                          setup_undo: bool = True) -> bool
```

x.set_module_short_name(module_path, new_short_name, setup_undo=True) -> bool
Set Module Short Name

Args:
    module_path (str): 
    new_short_name (str): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.set_module_selection"></a>

#### set_module_selection

```python
def set_module_selection(module_paths: Array[str]) -> bool
```

x.set_module_selection(module_paths) -> bool
Set Module Selection

Args:
    module_paths (Array[str]): 

Returns:
    bool:

<a id="unreal.ModularRigController.set_config_value_in_module"></a>

#### set_config_value_in_module

```python
def set_config_value_in_module(module_path: str,
                               variable_name: Name,
                               value: str,
                               setup_undo: bool = True) -> bool
```

x.set_config_value_in_module(module_path, variable_name, value, setup_undo=True) -> bool
Set Config Value in Module

Args:
    module_path (str): 
    variable_name (Name): 
    value (str): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.select_module"></a>

#### select_module

```python
def select_module(module_path: str, selected: bool = True) -> bool
```

x.select_module(module_path, selected=True) -> bool
Select Module

Args:
    module_path (str): 
    selected (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.reparent_module"></a>

#### reparent_module

```python
def reparent_module(module_path: str,
                    new_parent_module_path: str,
                    setup_undo: bool = True) -> str
```

x.reparent_module(module_path, new_parent_module_path, setup_undo=True) -> str
Reparent Module

Args:
    module_path (str): 
    new_parent_module_path (str): 
    setup_undo (bool): 

Returns:
    str:

<a id="unreal.ModularRigController.rename_module"></a>

#### rename_module

```python
def rename_module(module_path: str,
                  new_name: Name,
                  setup_undo: bool = True) -> str
```

x.rename_module(module_path, new_name, setup_undo=True) -> str
Rename Module

Args:
    module_path (str): 
    new_name (Name): 
    setup_undo (bool): 

Returns:
    str:

<a id="unreal.ModularRigController.mirror_module"></a>

#### mirror_module

```python
def mirror_module(module_path: str,
                  settings: RigVMMirrorSettings,
                  setup_undo: bool = True) -> str
```

x.mirror_module(module_path, settings, setup_undo=True) -> str
Mirror Module

Args:
    module_path (str): 
    settings (RigVMMirrorSettings): 
    setup_undo (bool): 

Returns:
    str:

<a id="unreal.ModularRigController.get_selected_modules"></a>

#### get_selected_modules

```python
def get_selected_modules() -> Array[str]
```

x.get_selected_modules() -> Array[str]
Get Selected Modules

Returns:
    Array[str]:

<a id="unreal.ModularRigController.disconnect_cyclic_connectors"></a>

#### disconnect_cyclic_connectors

```python
def disconnect_cyclic_connectors(
        setup_undo: bool = True) -> Array[RigElementKey]
```

x.disconnect_cyclic_connectors(setup_undo=True) -> Array[RigElementKey]
Disconnect Cyclic Connectors

Args:
    setup_undo (bool): 

Returns:
    Array[RigElementKey]:

<a id="unreal.ModularRigController.disconnect_connector"></a>

#### disconnect_connector

```python
def disconnect_connector(connector_key: RigElementKey,
                         disconnect_sub_modules: bool = False,
                         setup_undo: bool = True) -> bool
```

x.disconnect_connector(connector_key, disconnect_sub_modules=False, setup_undo=True) -> bool
Disconnect Connector

Args:
    connector_key (RigElementKey): 
    disconnect_sub_modules (bool): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.deselect_module"></a>

#### deselect_module

```python
def deselect_module(module_path: str) -> bool
```

x.deselect_module(module_path) -> bool
Deselect Module

Args:
    module_path (str): 

Returns:
    bool:

<a id="unreal.ModularRigController.delete_module"></a>

#### delete_module

```python
def delete_module(module_path: str, setup_undo: bool = True) -> bool
```

x.delete_module(module_path, setup_undo=True) -> bool
Delete Module

Args:
    module_path (str): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.connect_connector_to_element"></a>

#### connect_connector_to_element

```python
def connect_connector_to_element(connector_key: RigElementKey,
                                 target_key: RigElementKey,
                                 setup_undo: bool = True,
                                 auto_resolve_other_connectors: bool = True,
                                 check_valid_connection: bool = True) -> bool
```

x.connect_connector_to_element(connector_key, target_key, setup_undo=True, auto_resolve_other_connectors=True, check_valid_connection=True) -> bool
Connect Connector to Element

Args:
    connector_key (RigElementKey): 
    target_key (RigElementKey): 
    setup_undo (bool): 
    auto_resolve_other_connectors (bool): 
    check_valid_connection (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.can_connect_connector_to_element"></a>

#### can_connect_connector_to_element

```python
def can_connect_connector_to_element(
        connector_key: RigElementKey,
        target_key: RigElementKey) -> Optional[Text]
```

x.can_connect_connector_to_element(connector_key, target_key) -> Text or None
Can Connect Connector to Element

Args:
    connector_key (RigElementKey): 
    target_key (RigElementKey): 

Returns:
    Text or None: 

    out_error_message (Text):

<a id="unreal.ModularRigController.bind_module_variable"></a>

#### bind_module_variable

```python
def bind_module_variable(module_path: str,
                         variable_name: Name,
                         source_path: str,
                         setup_undo: bool = True) -> bool
```

x.bind_module_variable(module_path, variable_name, source_path, setup_undo=True) -> bool
Bind Module Variable

Args:
    module_path (str): 
    variable_name (Name): 
    source_path (str): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.auto_connect_secondary_connectors"></a>

#### auto_connect_secondary_connectors

```python
def auto_connect_secondary_connectors(connector_keys: Array[RigElementKey],
                                      replace_existing_connections: bool,
                                      setup_undo: bool = True) -> bool
```

x.auto_connect_secondary_connectors(connector_keys, replace_existing_connections, setup_undo=True) -> bool
Auto Connect Secondary Connectors

Args:
    connector_keys (Array[RigElementKey]): 
    replace_existing_connections (bool): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.auto_connect_modules"></a>

#### auto_connect_modules

```python
def auto_connect_modules(module_paths: Array[str],
                         replace_existing_connections: bool,
                         setup_undo: bool = True) -> bool
```

x.auto_connect_modules(module_paths, replace_existing_connections, setup_undo=True) -> bool
Auto Connect Modules

Args:
    module_paths (Array[str]): 
    replace_existing_connections (bool): 
    setup_undo (bool): 

Returns:
    bool:

<a id="unreal.ModularRigController.add_module"></a>

#### add_module

```python
def add_module(module_name: Name,
               class_: Class,
               parent_module_path: str,
               setup_undo: bool = True) -> str
```

x.add_module(module_name, class_, parent_module_path, setup_undo=True) -> str
Add Module

Args:
    module_name (Name): 
    class_ (type(Class)): 
    parent_module_path (str): 
    setup_undo (bool): 

Returns:
    str:

<a id="unreal.ModularRigRuleManager"></a>