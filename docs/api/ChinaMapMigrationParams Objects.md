## ChinaMapMigrationParams Objects

```python
class ChinaMapMigrationParams(ParamsBase)
```

China Map Migration Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ChinaMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gathered`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``hub_province_code`` (str):  [Read-Write]
- ``migration_id`` (str):  [Read-Write]
- ``peripheral_provinces_info`` (Array[MigarationPeripheralProvinceInfo]):  [Read-Write]
- ``type`` (int32):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    migration_id: str = "",
    type: int = 0,
    hub_province_code: str = "",
    gathered: bool = False,
    peripheral_provinces_info: Array[MigarationPeripheralProvinceInfo] = []
) -> None
```

<a id="unreal.ChinaMapMigrationParams.migration_id"></a>

#### migration\_id

```python
@property
def migration_id() -> str
```

(str):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.migration_id"></a>

#### migration\_id

```python
@migration_id.setter
def migration_id(value: str) -> None
```

<a id="unreal.ChinaMapMigrationParams.type"></a>

#### type

```python
@property
def type() -> int
```

(int32):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.type"></a>

#### type

```python
@type.setter
def type(value: int) -> None
```

<a id="unreal.ChinaMapMigrationParams.hub_province_code"></a>

#### hub\_province\_code

```python
@property
def hub_province_code() -> str
```

(str):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.hub_province_code"></a>

#### hub\_province\_code

```python
@hub_province_code.setter
def hub_province_code(value: str) -> None
```

<a id="unreal.ChinaMapMigrationParams.gathered"></a>

#### gathered

```python
@property
def gathered() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.gathered"></a>

#### gathered

```python
@gathered.setter
def gathered(value: bool) -> None
```

<a id="unreal.ChinaMapMigrationParams.peripheral_provinces_info"></a>

#### peripheral\_provinces\_info

```python
@property
def peripheral_provinces_info() -> Array[MigarationPeripheralProvinceInfo]
```

(Array[MigarationPeripheralProvinceInfo]):  [Read-Write]

<a id="unreal.ChinaMapMigrationParams.peripheral_provinces_info"></a>

#### peripheral\_provinces\_info

```python
@peripheral_provinces_info.setter
def peripheral_provinces_info(
        value: Array[MigarationPeripheralProvinceInfo]) -> None
```

<a id="unreal.ChinaMapMigrationIdParams"></a>