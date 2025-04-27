## DatasmithImportScene Objects

```python
class DatasmithImportScene(EnumBase)
```

EDatasmith Import Scene

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

<a id="unreal.DatasmithImportScene.NEW_LEVEL"></a>

#### NEW_LEVEL

0: Create a new Level and spawn the actors after the import.

<a id="unreal.DatasmithImportScene.CURRENT_LEVEL"></a>

#### CURRENT_LEVEL

1: Use the current Level to spawn the actors after the import.

<a id="unreal.DatasmithImportScene.ASSETS_ONLY"></a>

#### ASSETS_ONLY

2: Do not modify the Level after import. No actor will be created (including the Blueprint if requested by the ImportHierarchy

<a id="unreal.DatasmithCADStitchingTechnique"></a>