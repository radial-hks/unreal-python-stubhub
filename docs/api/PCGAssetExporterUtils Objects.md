## PCGAssetExporterUtils Objects

```python
class PCGAssetExporterUtils(BlueprintFunctionLibrary)
```

Asset export utils - will work only in editor builds.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAssetExporterUtils.h

<a id="unreal.PCGAssetExporterUtils.update_assets"></a>

#### update_assets

```python
@classmethod
def update_assets(
        cls,
        pcg_assets: Array[AssetData],
        parameters: PCGAssetExporterParameters = [True, "", "", True]) -> None
```

X.update_assets(pcg_assets, parameters=[True, "", "", True]) -> None
Updates assets based on their embedded exporter & metadata.

Args:
    pcg_assets (Array[AssetData]): 
    parameters (PCGAssetExporterParameters):

<a id="unreal.PCGAssetExporterUtils.create_asset"></a>

#### create_asset

```python
@classmethod
def create_asset(
        cls,
        exporter: PCGAssetExporter,
        parameters: PCGAssetExporterParameters = [True, "", "",
                                                  True]) -> Package
```

X.create_asset(exporter, parameters=[True, "", "", True]) -> Package
Exports an asset from the given exporter. When calling this function, the exporter should be able to create its own data and as such needs prior information (world, etc.) before calling this method.

Args:
    exporter (PCGAssetExporter): 
    parameters (PCGAssetExporterParameters): 

Returns:
    Package:

<a id="unreal.PCGAttractSettings"></a>