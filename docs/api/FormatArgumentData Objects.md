## FormatArgumentData Objects

```python
class FormatArgumentData(StructBase)
```

Used to pass argument/value pairs into FText::Format.
The full C++ struct is located here: Engine\Source\Runtime\Core\Public\Internationalization\Text.h

**C++ Source:**

- **Module**: Engine
- **File**: KismetTextLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument_name`` (str):  [Read-Write]
- ``argument_value`` (Text):  [Read-Write]
- ``argument_value_double`` (double):  [Read-Write]
- ``argument_value_float`` (float):  [Read-Write]
- ``argument_value_gender`` (TextGender):  [Read-Write]
- ``argument_value_int`` (int64):  [Read-Write]
- ``argument_value_type`` (FormatArgumentType):  [Read-Write]

<a id="unreal.FormatArgumentData.__init__"></a>

#### __init__

```python
def __init__(argument_name: str = "",
             argument_value_type: FormatArgumentType = FormatArgumentType.INT,
             argument_value: Text = "",
             argument_value_int: int = 0,
             argument_value_float: float = 0.000000,
             argument_value_double: float = 0.000000,
             argument_value_gender: TextGender = TextGender.MASCULINE) -> None
```

<a id="unreal.FormatArgumentData.argument_name"></a>

#### argument_name

```python
@property
def argument_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_name"></a>

#### argument_name

```python
@argument_name.setter
def argument_name(value: str) -> None
```

<a id="unreal.FormatArgumentData.argument_value_type"></a>

#### argument_value_type

```python
@property
def argument_value_type() -> FormatArgumentType
```

(FormatArgumentType):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value_type"></a>

#### argument_value_type

```python
@argument_value_type.setter
def argument_value_type(value: FormatArgumentType) -> None
```

<a id="unreal.FormatArgumentData.argument_value"></a>

#### argument_value

```python
@property
def argument_value() -> Text
```

(Text):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value"></a>

#### argument_value

```python
@argument_value.setter
def argument_value(value: Text) -> None
```

<a id="unreal.FormatArgumentData.text_value"></a>

#### text_value

```python
@property
def text_value() -> Text
```

deprecated: 'text_value' was renamed to 'argument_value'.

<a id="unreal.FormatArgumentData.text_value"></a>

#### text_value

```python
@text_value.setter
def text_value(value: Text) -> None
```

<a id="unreal.FormatArgumentData.argument_value_int"></a>

#### argument_value_int

```python
@property
def argument_value_int() -> int
```

(int64):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value_int"></a>

#### argument_value_int

```python
@argument_value_int.setter
def argument_value_int(value: int) -> None
```

<a id="unreal.FormatArgumentData.argument_value_float"></a>

#### argument_value_float

```python
@property
def argument_value_float() -> float
```

(float):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value_float"></a>

#### argument_value_float

```python
@argument_value_float.setter
def argument_value_float(value: float) -> None
```

<a id="unreal.FormatArgumentData.argument_value_double"></a>

#### argument_value_double

```python
@property
def argument_value_double() -> float
```

(double):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value_double"></a>

#### argument_value_double

```python
@argument_value_double.setter
def argument_value_double(value: float) -> None
```

<a id="unreal.FormatArgumentData.argument_value_gender"></a>

#### argument_value_gender

```python
@property
def argument_value_gender() -> TextGender
```

(TextGender):  [Read-Write]

<a id="unreal.FormatArgumentData.argument_value_gender"></a>

#### argument_value_gender

```python
@argument_value_gender.setter
def argument_value_gender(value: TextGender) -> None
```

<a id="unreal.FormatTextArgument"></a>