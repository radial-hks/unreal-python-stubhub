## DatasmithOptionsBase Objects

```python
class DatasmithOptionsBase(Object)
```

Base class for all import options in datasmith.

Notable feature: forces a full serialization of its properties (by opposition
to the standard delta serialization which stores only the diff wrt the CDO)
The intent is to store the exact options used in a previous import.

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

<a id="unreal.DatasmithCommonTessellationOptions"></a>