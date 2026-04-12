## DCPEffectSelectParam Objects

```python
class DCPEffectSelectParam(ParamsBase)
```

DCPEffect Select Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPEffectSelectAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effect_name`` (str):  [Read-Write]
- ``effect_type`` (DCPEffectMaterialType):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.DCPEffectSelectParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(effect_type: DCPEffectMaterialType = DCPEffectMaterialType.
             EFFECT_DCP_BIM_HIGHT_LIGHT,
             effect_name: str = "") -> None
```

<a id="unreal.DCPEffectSelectParam.effect_type"></a>

#### effect\_type

```python
@property
def effect_type() -> DCPEffectMaterialType
```

(DCPEffectMaterialType):  [Read-Write]

<a id="unreal.DCPEffectSelectParam.effect_type"></a>

#### effect\_type

```python
@effect_type.setter
def effect_type(value: DCPEffectMaterialType) -> None
```

<a id="unreal.DCPEffectSelectParam.effect_name"></a>

#### effect\_name

```python
@property
def effect_name() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPEffectSelectParam.effect_name"></a>

#### effect\_name

```python
@effect_name.setter
def effect_name(value: str) -> None
```

<a id="unreal.DcpAlreadyEventEventParam"></a>