## PCGContext Objects

```python
class PCGContext(StructBase)
```

PCGContext

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGContext.h

<a id="unreal.PCGContext.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PCGContext.get_task_id"></a>

#### get_task_id

```python
def get_task_id() -> int
```

x.get_task_id() -> int64
Get Task Id

Returns:
    int64:

<a id="unreal.PCGContext.get_target_actor"></a>

#### get_target_actor

```python
def get_target_actor(spatial_data: PCGSpatialData) -> Actor
```

x.get_target_actor(spatial_data) -> Actor
Get Target Actor

Args:
    spatial_data (PCGSpatialData): 

Returns:
    Actor:

<a id="unreal.PCGContext.get_settings"></a>

#### get_settings

```python
def get_settings() -> PCGSettings
```

x.get_settings() -> PCGSettings
Get Settings

Returns:
    PCGSettings:

<a id="unreal.PCGContext.get_original_component"></a>

#### get_original_component

```python
def get_original_component() -> PCGComponent
```

x.get_original_component() -> PCGComponent
Get Original Component

Returns:
    PCGComponent:

<a id="unreal.PCGContext.get_input_data"></a>

#### get_input_data

```python
def get_input_data() -> PCGData
```

x.get_input_data() -> PCGData
Get Input Data

Returns:
    PCGData:

<a id="unreal.PCGContext.get_component"></a>

#### get_component

```python
def get_component() -> PCGComponent
```

x.get_component() -> PCGComponent
Get Component

Returns:
    PCGComponent:

<a id="unreal.PCGContext.get_actor_data"></a>

#### get_actor_data

```python
def get_actor_data() -> PCGData
```

x.get_actor_data() -> PCGData
Get Actor Data

Returns:
    PCGData:

<a id="unreal.PCGStaticMeshSpawnerContext"></a>