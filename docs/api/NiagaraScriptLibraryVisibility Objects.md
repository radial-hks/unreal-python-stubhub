## NiagaraScriptLibraryVisibility Objects

```python
class NiagaraScriptLibraryVisibility(EnumBase)
```

ENiagara Script Library Visibility

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraScript.h

<a id="unreal.NiagaraScriptLibraryVisibility.UNEXPOSED"></a>

#### UNEXPOSED

1: The script is not visible by default to the user, but can be made visible by disabling the "Library only" filter option.

<a id="unreal.NiagaraScriptLibraryVisibility.LIBRARY"></a>

#### LIBRARY

2: The script is exposed to the asset library and always visible to the user.

<a id="unreal.NiagaraScriptLibraryVisibility.HIDDEN"></a>

#### HIDDEN

3: The script is never visible to the user. This is useful to "soft deprecate" assets that should not be shown to a user, but should also not generate errors for existing usages.

<a id="unreal.NiagaraNumericOutputTypeSelectionMode"></a>