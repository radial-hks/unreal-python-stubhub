## RigVMBlueprintLibrary Objects

```python
class RigVMBlueprintLibrary(BlueprintFunctionLibrary)
```

Rig VMEditor Blueprint Library

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMEditor
- **File**: RigVMEditorBlueprintLibrary.h

<a id="unreal.RigVMBlueprintLibrary.request_auto_vm_recompilation"></a>

#### request_auto_vm_recompilation

```python
@classmethod
def request_auto_vm_recompilation(cls, blueprint: RigVMBlueprint) -> None
```

X.request_auto_vm_recompilation(blueprint) -> None
Request Auto VMRecompilation

Args:
    blueprint (RigVMBlueprint):

<a id="unreal.RigVMBlueprintLibrary.recompile_vm_if_required"></a>

#### recompile_vm_if_required

```python
@classmethod
def recompile_vm_if_required(cls, blueprint: RigVMBlueprint) -> None
```

X.recompile_vm_if_required(blueprint) -> None
Recompile VMIf Required

Args:
    blueprint (RigVMBlueprint):

<a id="unreal.RigVMBlueprintLibrary.recompile_vm"></a>

#### recompile_vm

```python
@classmethod
def recompile_vm(cls, blueprint: RigVMBlueprint) -> None
```

X.recompile_vm(blueprint) -> None
Recompile VM

Args:
    blueprint (RigVMBlueprint):

<a id="unreal.RigVMBlueprintLibrary.load_assets_with_node_filter"></a>

#### load_assets_with_node_filter

```python
@classmethod
def load_assets_with_node_filter(
        cls, class_: Class,
        node_filter: RigVMNodeFilterDynamic) -> Array[RigVMBlueprint]
```

X.load_assets_with_node_filter(class_, node_filter) -> Array[RigVMBlueprint]
Load Assets with Node Filter for Blueprint

Args:
    class_ (type(Class)): 
    node_filter (RigVMNodeFilterDynamic): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets_with_blueprint_filter"></a>

#### load_assets_with_blueprint_filter

```python
@classmethod
def load_assets_with_blueprint_filter(
        cls, class_: Class, blueprint_filter: RigVMBlueprintFilterDynamic
) -> Array[RigVMBlueprint]
```

X.load_assets_with_blueprint_filter(class_, blueprint_filter) -> Array[RigVMBlueprint]
Load Assets with Blueprint Filter for Blueprint

Args:
    class_ (type(Class)): 
    blueprint_filter (RigVMBlueprintFilterDynamic): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets_with_asset_data_filter"></a>

#### load_assets_with_asset_data_filter

```python
@classmethod
def load_assets_with_asset_data_filter(
        cls, class_: Class, asset_data_filter: RigVMAssetDataFilterDynamic
) -> Array[RigVMBlueprint]
```

X.load_assets_with_asset_data_filter(class_, asset_data_filter) -> Array[RigVMBlueprint]
Load Assets with Asset Data Filter for Blueprint

Args:
    class_ (type(Class)): 
    asset_data_filter (RigVMAssetDataFilterDynamic): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets_with_asset_data_and_node_filters"></a>

#### load_assets_with_asset_data_and_node_filters

```python
@classmethod
def load_assets_with_asset_data_and_node_filters(
        cls, class_: Class, asset_data_filter: RigVMAssetDataFilterDynamic,
        node_filter: RigVMNodeFilterDynamic) -> Array[RigVMBlueprint]
```

X.load_assets_with_asset_data_and_node_filters(class_, asset_data_filter, node_filter) -> Array[RigVMBlueprint]
Load Assets with Asset Data and Node Filters for Blueprint

Args:
    class_ (type(Class)): 
    asset_data_filter (RigVMAssetDataFilterDynamic): 
    node_filter (RigVMNodeFilterDynamic): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets_with_asset_data_and_blueprint_filters"></a>

#### load_assets_with_asset_data_and_blueprint_filters

```python
@classmethod
def load_assets_with_asset_data_and_blueprint_filters(
        cls, class_: Class, asset_data_filter: RigVMAssetDataFilterDynamic,
        blueprint_filter: RigVMBlueprintFilterDynamic
) -> Array[RigVMBlueprint]
```

X.load_assets_with_asset_data_and_blueprint_filters(class_, asset_data_filter, blueprint_filter) -> Array[RigVMBlueprint]
Load Assets with Asset Data and Blueprint Filters for Blueprint

Args:
    class_ (type(Class)): 
    asset_data_filter (RigVMAssetDataFilterDynamic): 
    blueprint_filter (RigVMBlueprintFilterDynamic): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets_by_class"></a>

#### load_assets_by_class

```python
@classmethod
def load_assets_by_class(cls, class_: Class) -> Array[RigVMBlueprint]
```

X.load_assets_by_class(class_) -> Array[RigVMBlueprint]
Load Assets by Class

Args:
    class_ (type(Class)): 

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.load_assets"></a>

#### load_assets

```python
@classmethod
def load_assets(cls) -> Array[RigVMBlueprint]
```

X.load_assets() -> Array[RigVMBlueprint]
Load Assets

Returns:
    Array[RigVMBlueprint]:

<a id="unreal.RigVMBlueprintLibrary.get_model"></a>

#### get_model

```python
@classmethod
def get_model(cls, blueprint: RigVMBlueprint) -> RigVMGraph
```

X.get_model(blueprint) -> RigVMGraph
Get Model

Args:
    blueprint (RigVMBlueprint): 

Returns:
    RigVMGraph:

<a id="unreal.RigVMBlueprintLibrary.get_controller"></a>

#### get_controller

```python
@classmethod
def get_controller(cls, blueprint: RigVMBlueprint) -> RigVMController
```

X.get_controller(blueprint) -> RigVMController
Get Controller

Args:
    blueprint (RigVMBlueprint): 

Returns:
    RigVMController:

<a id="unreal.RigVMBlueprintLibrary.get_assets_with_filter"></a>

#### get_assets_with_filter

```python
@classmethod
def get_assets_with_filter(
        cls, class_: Class,
        asset_data_filter: RigVMAssetDataFilterDynamic) -> Array[AssetData]
```

X.get_assets_with_filter(class_, asset_data_filter) -> Array[AssetData]
Get Assets with Filter for Blueprint

Args:
    class_ (type(Class)): 
    asset_data_filter (RigVMAssetDataFilterDynamic): 

Returns:
    Array[AssetData]:

<a id="unreal.RigVMSchema"></a>