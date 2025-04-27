## PCGMatchAndSetBase Objects

```python
class PCGMatchAndSetBase(Object)
```

Base class for Match & Set objects. Note that while it currently deals with points, it might be extended in the future.
This class is extensible and can be implemented in different ways, but its role should be simple:
For a given point, if it matches some criteria ("Match"), apply it some value ("Set").
It can be a lookup, a random process or something more involved.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetBase.h

<a id="unreal.PCGMatchAndSetBase.validate_preconditions"></a>

#### validate_preconditions

```python
def validate_preconditions(point_data: PCGPointData) -> bool
```

x.validate_preconditions(point_data) -> bool
Early check to prevent issues when the data does not contain the required information to perform the operation

Args:
    point_data (PCGPointData): 

Returns:
    bool:

<a id="unreal.PCGMatchAndSetBase.match_and_set"></a>

#### match_and_set

```python
def match_and_set(context: PCGContext, settings: PCGPointMatchAndSetSettings,
                  point_data: PCGPointData,
                  out_point_data: PCGPointData) -> PCGContext
```

x.match_and_set(context, settings, point_data, out_point_data) -> PCGContext
Main function to process points, and pass them through the Match & Set logic.

Args:
    context (PCGContext): 
    settings (PCGPointMatchAndSetSettings): 
    point_data (PCGPointData): 
    out_point_data (PCGPointData): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGMatchAndSetByAttribute"></a>