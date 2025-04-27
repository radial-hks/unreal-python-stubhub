## CEClonerLayoutBase Objects

```python
class CEClonerLayoutBase(Object)
```

Base class for layouts available in the cloner actor
Steps to add a new layout :
1. Create a new system that extends from NS_ClonerBase and expose all the parent parameters (examples can be found in Content)
2. Extend this layout class and give it a unique name with the newly created system path
3. Expose all new system specific parameters in the layout extended class and update them when required
Your new layout is ready and will be available in the cloner in the layout dropdown

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerLayoutBase.h

<a id="unreal.CEClonerLayoutBase.is_layout_active"></a>

#### is_layout_active

```python
def is_layout_active() -> bool
```

x.is_layout_active() -> bool
Is this layout system in use within the cloner

Returns:
    bool:

<a id="unreal.CEClonerLayoutBase.get_layout_name"></a>

#### get_layout_name

```python
def get_layout_name() -> Name
```

x.get_layout_name() -> Name
Get Layout Name

Returns:
    Name:

<a id="unreal.AvaClonerLayoutBase"></a>