## PCGLoadAlembicFunctionLibrary Objects

```python
class PCGLoadAlembicFunctionLibrary(BlueprintFunctionLibrary)
```

PCGLoad Alembic Function Library

**C++ Source:**

- **Plugin**: PCGExternalDataInterop
- **Module**: PCGExternalDataInteropEditor
- **File**: PCGLoadAlembic.h

<a id="unreal.PCGLoadAlembicFunctionLibrary.setup_from_standard"></a>

#### setup_from_standard

```python
@classmethod
def setup_from_standard(
        cls, data: PCGLoadAlembicBPData,
        setup: PCGLoadAlembicStandardSetup) -> PCGLoadAlembicBPData
```

X.setup_from_standard(data, setup) -> PCGLoadAlembicBPData
Setup from Standard

Args:
    data (PCGLoadAlembicBPData): 
    setup (PCGLoadAlembicStandardSetup): 

Returns:
    PCGLoadAlembicBPData: 

    data (PCGLoadAlembicBPData):

<a id="unreal.PCGLoadAlembicFunctionLibrary.load_alembic_file_to_pcg"></a>

#### load_alembic_file_to_pcg

```python
@classmethod
def load_alembic_file_to_pcg(cls, settings: PCGLoadAlembicBPData,
                             target_outer: Object) -> PCGDataCollection
```

X.load_alembic_file_to_pcg(settings, target_outer) -> PCGDataCollection
Load Alembic File to PCG
deprecated: The LoadAlembicFileToPCG function has been replaced by ExportAlembicFileToPCG

Args:
    settings (PCGLoadAlembicBPData): 
    target_outer (Object): 

Returns:
    PCGDataCollection: 

    data (PCGDataCollection):

<a id="unreal.PCGLoadAlembicFunctionLibrary.export_alembic_file_to_pcg"></a>

#### export_alembic_file_to_pcg

```python
@classmethod
def export_alembic_file_to_pcg(
        cls,
        settings: PCGLoadAlembicBPData,
        parameters: PCGAssetExporterParameters = [True, "", "", True]) -> None
```

X.export_alembic_file_to_pcg(settings, parameters=[True, "", "", True]) -> None
Export Alembic File to PCG

Args:
    settings (PCGLoadAlembicBPData): 
    parameters (PCGAssetExporterParameters):

<a id="unreal.PCGDynamicMeshBaseSettings"></a>