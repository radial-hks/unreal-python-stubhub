## EnvNamedValue Objects

```python
class EnvNamedValue(StructBase)
```

Env Named Value

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``param_name`` (Name):  [Read-Write]
- ``param_type`` (AIParamType):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.EnvNamedValue.__init__"></a>

#### __init__

```python
def __init__(param_name: Name = "None",
             param_type: AIParamType = AIParamType.FLOAT,
             value: float = 0.000000) -> None
```

<a id="unreal.EnvNamedValue.param_name"></a>

#### param_name

```python
@property
def param_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EnvNamedValue.param_name"></a>

#### param_name

```python
@param_name.setter
def param_name(value: Name) -> None
```

<a id="unreal.EnvNamedValue.param_type"></a>

#### param_type

```python
@property
def param_type() -> AIParamType
```

(AIParamType):  [Read-Write]

<a id="unreal.EnvNamedValue.param_type"></a>

#### param_type

```python
@param_type.setter
def param_type(value: AIParamType) -> None
```

<a id="unreal.EnvNamedValue.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.EnvNamedValue.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.EnvQueryResult"></a>