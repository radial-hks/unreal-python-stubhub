## OnVegetationCreatedEventArgs Objects

```python
class OnVegetationCreatedEventArgs(EventArgsBase)
```

On Vegetation Created Event Args

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: RuntimeModelerAPI
- **File**: WdpModelerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_id`` (int64):  [Read-Write]
- ``entity_type`` (Name):  [Read-Write]
- ``vegetation_num`` (int64):  [Read-Write]

<a id="unreal.OnVegetationCreatedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_id: int = 0,
             entity_type: Name = "None",
             vegetation_num: int = 0) -> None
```

<a id="unreal.OnVegetationCreatedEventArgs.entity_id"></a>

#### entity\_id

```python
@property
def entity_id() -> int
```

(int64):  [Read-Write]

<a id="unreal.OnVegetationCreatedEventArgs.entity_id"></a>

#### entity\_id

```python
@entity_id.setter
def entity_id(value: int) -> None
```

<a id="unreal.OnVegetationCreatedEventArgs.entity_type"></a>

#### entity\_type

```python
@property
def entity_type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.OnVegetationCreatedEventArgs.entity_type"></a>

#### entity\_type

```python
@entity_type.setter
def entity_type(value: Name) -> None
```

<a id="unreal.OnVegetationCreatedEventArgs.vegetation_num"></a>

#### vegetation\_num

```python
@property
def vegetation_num() -> int
```

(int64):  [Read-Write]

<a id="unreal.OnVegetationCreatedEventArgs.vegetation_num"></a>

#### vegetation\_num

```python
@vegetation_num.setter
def vegetation_num(value: int) -> None
```

<a id="unreal.DelaunayIndex"></a>