## AIDynamicParam Objects

```python
class AIDynamicParam(StructBase)
```

AIDynamic Param

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_bb_key`` (bool):  [Read-Write]
- ``bb_key`` (BlackboardKeySelector):  [Read-Write]
- ``param_name`` (Name):  [Read-Only]
- ``param_type`` (AIParamType):  [Read-Only]
- ``value`` (float):  [Read-Write]

<a id="unreal.AIDynamicParam.__init__"></a>

#### __init__

```python
def __init__(
        param_name: Name = "None",
        param_type: AIParamType = AIParamType.FLOAT,
        allow_bb_key: bool = False,
        value: float = 0.000000,
        bb_key: BlackboardKeySelector = [[], "None", None, 65535,
                                         False]) -> None
```

<a id="unreal.AIDynamicParam.param_name"></a>

#### param_name

```python
@property
def param_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.AIDynamicParam.param_type"></a>

#### param_type

```python
@property
def param_type() -> AIParamType
```

(AIParamType):  [Read-Only]

<a id="unreal.AIDynamicParam.allow_bb_key"></a>

#### allow_bb_key

```python
@property
def allow_bb_key() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AIDynamicParam.allow_bb_key"></a>

#### allow_bb_key

```python
@allow_bb_key.setter
def allow_bb_key(value: bool) -> None
```

<a id="unreal.AIDynamicParam.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.AIDynamicParam.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.AIDynamicParam.bb_key"></a>

#### bb_key

```python
@property
def bb_key() -> BlackboardKeySelector
```

(BlackboardKeySelector):  [Read-Write]

<a id="unreal.AIDynamicParam.bb_key"></a>

#### bb_key

```python
@bb_key.setter
def bb_key(value: BlackboardKeySelector) -> None
```

<a id="unreal.BlackboardKeySelector"></a>