## EnumBase Objects

```python
class EnumBase(_WrapperBase)
```

Type for all Unreal exposed enum instances

<a id="unreal.EnumBase.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.EnumBase.cast"></a>

#### cast

```python
@classmethod
def cast(cls: Type[_T], object: object) -> _T
```

cast(cls: Type[_T], object: object) -> _T -- cast the given object to this Unreal enum type

<a id="unreal.EnumBase.static_enum"></a>

#### static_enum

```python
@classmethod
def static_enum(cls) -> Enum
```

static_enum(cls) -> Enum -- get the Unreal enum of this type

<a id="unreal.EnumBase.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

get_display_name(self) -> Text -- get the UMETA display name of this type in the current culture

<a id="unreal._EnumEntry"></a>