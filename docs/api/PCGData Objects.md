## PCGData Objects

```python
class PCGData(Object)
```

Base class for any "data" class in the PCG framework.
This is an intentionally vague base class so we can have the required
flexibility to pass in various concrete data types, settings, and more.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGData.h

<a id="unreal.PCGData.duplicate_data"></a>

#### duplicate_data

```python
def duplicate_data(
        context: PCGContext,
        initialize_metadata: bool = True) -> Tuple[PCGData, PCGContext]
```

x.duplicate_data(context, initialize_metadata=True) -> (PCGData, context=PCGContext)
Return a copy of the data, with Metadata inheritance for spatial data.

Args:
    context (PCGContext): 
    initialize_metadata (bool): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGSettingsInterface"></a>