## Name Objects

```python
class Name(_WrapperBase)
```

Type for all Unreal exposed name instances

<a id="unreal.Name.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: Union[Name, str] = "None") -> None
```

<a id="unreal.Name.cast"></a>

#### cast

```python
@classmethod
def cast(cls, object: object) -> Name
```

cast(cls, object: object) -> Name -- cast the given object to this Unreal name type

<a id="unreal.Name.is_valid"></a>

#### is\_valid

```python
def is_valid() -> bool
```

is_valid(self) -> bool -- is this Unreal name valid?

<a id="unreal.Name.is_none"></a>

#### is\_none

```python
def is_none() -> bool
```

is_none(self) -> bool -- is this Unreal name set to NAME_None?

<a id="unreal.Text"></a>