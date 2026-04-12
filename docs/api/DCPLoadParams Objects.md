## DCPLoadParams Objects

```python
class DCPLoadParams(ParamsBase)
```

DCPLoad Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPModelAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_json_path`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]

<a id="unreal.DCPLoadParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_json_path: str = "",
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPLoadParams.asset_json_path"></a>

#### asset\_json\_path

```python
@property
def asset_json_path() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPLoadParams.asset_json_path"></a>

#### asset\_json\_path

```python
@asset_json_path.setter
def asset_json_path(value: str) -> None
```

<a id="unreal.DCPLoadParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPLoadParams.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.DCPLoadParams_Batch"></a>