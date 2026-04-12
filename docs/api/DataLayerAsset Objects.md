## DataLayerAsset Objects

```python
class DataLayerAsset(DataAsset)
```

Data Layer Asset

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_layer_type`` (DataLayerType):  [Read-Write] Whether the Data Layer affects actor runtime loading
- ``debug_color`` (Color):  [Read-Write]
- ``load_filter`` (DataLayerLoadFilter):  [Read-Write]
- ``supports_actor_filters`` (bool):  [Read-Write]

<a id="unreal.DataLayerAsset.is_server_only"></a>

#### is\_server\_only

```python
def is_server_only() -> bool
```

x.is_server_only() -> bool
Is Server Only

Returns:
    bool:

<a id="unreal.DataLayerAsset.is_runtime"></a>

#### is\_runtime

```python
def is_runtime() -> bool
```

x.is_runtime() -> bool
Is Runtime

Returns:
    bool:

<a id="unreal.DataLayerAsset.is_client_only"></a>

#### is\_client\_only

```python
def is_client_only() -> bool
```

x.is_client_only() -> bool
Is Client Only

Returns:
    bool:

<a id="unreal.DataLayerAsset.get_type"></a>

#### get\_type

```python
def get_type() -> DataLayerType
```

x.get_type() -> DataLayerType
Get Type

Returns:
    DataLayerType:

<a id="unreal.DataLayerAsset.get_debug_color"></a>

#### get\_debug\_color

```python
def get_debug_color() -> Color
```

x.get_debug_color() -> Color
Get Debug Color

Returns:
    Color:

<a id="unreal.ExternalDataLayerAsset"></a>