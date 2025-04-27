## MoviePipelineFCPXMLExporter Objects

```python
class MoviePipelineFCPXMLExporter(MoviePipelineOutputBase)
```

Movie Pipeline FCPXMLExporter

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineFCPXMLExporterSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_source`` (FCPXMLExportDataSource):  [Read-Write] Whether to build the FCPXML from sequence data directly (for reimporting) or from actual frame output data (for post processing)
- ``file_name_format_override`` (str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting. Can include folder prefixes, and format string tags ({sequence_name}, etc.)

<a id="unreal.MoviePipelineFCPXMLExporter.file_name_format_override"></a>

#### file_name_format_override

```python
@property
def file_name_format_override() -> str
```

(str):  [Read-Write] File name format string override. If specified it will override the FileNameFormat from the Output setting. Can include folder prefixes, and format string tags ({sequence_name}, etc.)

<a id="unreal.MoviePipelineFCPXMLExporter.file_name_format_override"></a>

#### file_name_format_override

```python
@file_name_format_override.setter
def file_name_format_override(value: str) -> None
```

<a id="unreal.MoviePipelineFCPXMLExporter.data_source"></a>

#### data_source

```python
@property
def data_source() -> FCPXMLExportDataSource
```

(FCPXMLExportDataSource):  [Read-Write] Whether to build the FCPXML from sequence data directly (for reimporting) or from actual frame output data (for post processing)

<a id="unreal.MoviePipelineFCPXMLExporter.data_source"></a>

#### data_source

```python
@data_source.setter
def data_source(value: FCPXMLExportDataSource) -> None
```

<a id="unreal.MoviePipelineGameOverrideSetting"></a>