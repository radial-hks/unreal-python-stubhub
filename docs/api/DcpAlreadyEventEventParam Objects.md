## DcpAlreadyEventEventParam Objects

```python
class DcpAlreadyEventEventParam(EventArgsBase)
```

Dcp Already Event Event Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPInitAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``already`` (bool):  [Read-Write]
- ``api_version`` (str):  [Read-Write]
- ``save_entity_eid`` (str):  [Read-Write]

<a id="unreal.DcpAlreadyEventEventParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(already: bool = False,
             api_version: str = "",
             save_entity_eid: str = "") -> None
```

<a id="unreal.DcpAlreadyEventEventParam.already"></a>

#### already

```python
@property
def already() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DcpAlreadyEventEventParam.already"></a>

#### already

```python
@already.setter
def already(value: bool) -> None
```

<a id="unreal.DcpAlreadyEventEventParam.api_version"></a>

#### api\_version

```python
@property
def api_version() -> str
```

(str):  [Read-Write]

<a id="unreal.DcpAlreadyEventEventParam.api_version"></a>

#### api\_version

```python
@api_version.setter
def api_version(value: str) -> None
```

<a id="unreal.DcpAlreadyEventEventParam.save_entity_eid"></a>

#### save\_entity\_eid

```python
@property
def save_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DcpAlreadyEventEventParam.save_entity_eid"></a>

#### save\_entity\_eid

```python
@save_entity_eid.setter
def save_entity_eid(value: str) -> None
```

<a id="unreal.DCPAPIVersionParam"></a>