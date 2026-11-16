-- ============================================================================
-- 01_schema.sql — Cloud Spanner Multi-Model Knowledge Graph + Hybrid Search DDL
-- Project: ${GCP_PROJECT} | Region: ${GCP_REGION}
-- Features:
--   1. Spanner Native Vertex AI Embedding Model (${SPANNER_MODEL_NAME})
--   2. 5 Domain Node Tables (PlantUnits, Equipment, Instruments, ProcessBoundaries, GovernanceDocs)
--   3. Typed Relationship Edge Tables (BELONGS_TO_UNIT, FLOWS_TO, MONITORS, EXTRACTED_FROM, GOVERNED_BY)
--   4. Unified Hybrid Search Corpus (OkfChunks with TOKENLIST Search Index + 768d FLOAT32 Vector)
--   5. Spanner Property Graph (${SPANNER_GRAPH_NAME} — ISO GQL)
-- ============================================================================

-- 0. Enable Spanner Query Optimizer v7+ at database level (required by SCORE() Full-Text ranking)
ALTER DATABASE `${SPANNER_DATABASE}` SET OPTIONS (
  optimizer_version = 7
);

-- 1. Native Vertex AI Embedding Model (invoked directly via SQL ML.PREDICT)
CREATE MODEL ${SPANNER_MODEL_NAME}
INPUT(
  content STRING(MAX)
)
OUTPUT(
  embeddings STRUCT<
    statistics STRUCT<truncated BOOL, token_count FLOAT32>,
    values ARRAY<FLOAT32>
  >
)
REMOTE OPTIONS (
  endpoint = '//aiplatform.googleapis.com/projects/${GCP_PROJECT}/locations/${GENAI_LOCATION}/publishers/google/models/${EMBEDDING_MODEL}'
);

-- 2. Node Table 1: PlantUnits (Plant Systems & Subsystems: SI, SW, SF, SS, RH, CS, CBS, CC, DG)
CREATE TABLE PlantUnits (
  UnitId STRING(128) NOT NULL,
  UnitCode STRING(32) NOT NULL,
  Title STRING(512) NOT NULL,
  Facility STRING(128) NOT NULL,
  SafetyClassification STRING(128),
  Description STRING(MAX),
  HasWarning BOOL NOT NULL,
  GcsUri STRING(1024),
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (UnitId);

-- 3. Node Table 2: Equipment (61 P&ID Pumps, Heat Exchangers, Sumps, Vessels, Filters, Fans)
CREATE TABLE Equipment (
  EquipmentId STRING(128) NOT NULL,
  Tag STRING(128) NOT NULL,
  Title STRING(512) NOT NULL,
  EquipmentClass STRING(128) NOT NULL,
  UnitCode STRING(64) NOT NULL,
  SafetyClassification STRING(128),
  HasConflict BOOL NOT NULL,
  ConflictSummary STRING(MAX),
  Description STRING(MAX),
  GcsUri STRING(1024) NOT NULL,
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (EquipmentId);

CREATE INDEX EquipmentByTagIdx ON Equipment(Tag);

-- 4. Node Table 3: Instruments (24 Full SIS Instrument Specs + ~188 Inline P&ID Loop Instruments)
CREATE TABLE Instruments (
  InstrumentId STRING(128) NOT NULL,
  Tag STRING(128) NOT NULL,
  Title STRING(512) NOT NULL,
  InstrumentType STRING(128) NOT NULL,
  UnitCode STRING(64),
  SafetyClassification STRING(128),
  Location STRING(512),
  SetpointOrRange STRING(256),
  InterlockOrAlarm STRING(512),
  HasWarning BOOL NOT NULL,
  IsFullSpec BOOL NOT NULL,
  Description STRING(MAX),
  GcsUri STRING(1024),
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (InstrumentId);

CREATE INDEX InstrumentsByTagIdx ON Instruments(Tag);

-- 5. Node Table 4: ProcessBoundaries (Headers, Penetrations X-24..X-61, RWST, CCW Loops, Sumps)
CREATE TABLE ProcessBoundaries (
  BoundaryId STRING(160) NOT NULL,
  Tag STRING(160) NOT NULL,
  BoundaryType STRING(64) NOT NULL,
  Description STRING(MAX),
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (BoundaryId);

-- 6. Node Table 5: GovernanceDocs (HAZOP, RAM, Procedures, Standards, NRC P&ID Packages ML101620329)
CREATE TABLE GovernanceDocs (
  DocId STRING(256) NOT NULL,
  DocType STRING(128) NOT NULL,
  Tag STRING(128) NOT NULL,
  Title STRING(512) NOT NULL,
  GoverningStandard STRING(256),
  HasWarning BOOL NOT NULL,
  Description STRING(MAX),
  GcsUri STRING(1024) NOT NULL,
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (DocId);

-- 7. Edge Table: Equipment -> PlantUnit (BELONGS_TO_UNIT)
CREATE TABLE UnitEquipment (
  EdgeId STRING(128) NOT NULL,
  EquipmentId STRING(128) NOT NULL,
  UnitId STRING(128) NOT NULL,
  RelationshipRole STRING(64) NOT NULL,
  CONSTRAINT FK_UE_Equipment FOREIGN KEY (EquipmentId) REFERENCES Equipment (EquipmentId),
  CONSTRAINT FK_UE_Unit FOREIGN KEY (UnitId) REFERENCES PlantUnits (UnitId)
) PRIMARY KEY (EdgeId);

-- 8a. Edge Table: Equipment -> Equipment P&ID Streams (FLOWS_TO)
CREATE TABLE EquipmentFlows (
  EdgeId STRING(128) NOT NULL,
  SrcId STRING(160) NOT NULL,
  DstId STRING(160) NOT NULL,
  StreamId STRING(128) NOT NULL,
  Direction STRING(64) NOT NULL,
  LineSize STRING(128),
  InlineComponents STRING(MAX),
  Temperature STRING(128),
  Pressure STRING(128),
  SourceDrawing STRING(256),
  Description STRING(MAX),
  CONSTRAINT FK_EF_Src FOREIGN KEY (SrcId) REFERENCES Equipment (EquipmentId),
  CONSTRAINT FK_EF_Dst FOREIGN KEY (DstId) REFERENCES Equipment (EquipmentId)
) PRIMARY KEY (EdgeId);

-- 8b. Edge Table: ProcessBoundary -> Equipment P&ID Streams (FLOWS_TO)
CREATE TABLE BoundaryToEquipmentFlows (
  EdgeId STRING(128) NOT NULL,
  SrcId STRING(160) NOT NULL,
  DstId STRING(160) NOT NULL,
  StreamId STRING(128) NOT NULL,
  Direction STRING(64) NOT NULL,
  LineSize STRING(128),
  InlineComponents STRING(MAX),
  Temperature STRING(128),
  Pressure STRING(128),
  SourceDrawing STRING(256),
  Description STRING(MAX),
  CONSTRAINT FK_BEF_Src FOREIGN KEY (SrcId) REFERENCES ProcessBoundaries (BoundaryId),
  CONSTRAINT FK_BEF_Dst FOREIGN KEY (DstId) REFERENCES Equipment (EquipmentId)
) PRIMARY KEY (EdgeId);

-- 8c. Edge Table: Equipment -> ProcessBoundary P&ID Streams (FLOWS_TO)
CREATE TABLE EquipmentToBoundaryFlows (
  EdgeId STRING(128) NOT NULL,
  SrcId STRING(160) NOT NULL,
  DstId STRING(160) NOT NULL,
  StreamId STRING(128) NOT NULL,
  Direction STRING(64) NOT NULL,
  LineSize STRING(128),
  InlineComponents STRING(MAX),
  Temperature STRING(128),
  Pressure STRING(128),
  SourceDrawing STRING(256),
  Description STRING(MAX),
  CONSTRAINT FK_EBF_Src FOREIGN KEY (SrcId) REFERENCES Equipment (EquipmentId),
  CONSTRAINT FK_EBF_Dst FOREIGN KEY (DstId) REFERENCES ProcessBoundaries (BoundaryId)
) PRIMARY KEY (EdgeId);

-- 9. Edge Table: Instrument -> Equipment (MONITORS)
CREATE TABLE InstrumentMonitorsEquipment (
  EdgeId STRING(128) NOT NULL,
  InstrumentId STRING(128) NOT NULL,
  EquipmentId STRING(128) NOT NULL,
  LoopRole STRING(64) NOT NULL,
  Location STRING(512),
  SetpointOrRange STRING(256),
  InterlockOrAlarm STRING(512),
  SourceDrawing STRING(256),
  CONSTRAINT FK_IME_Inst FOREIGN KEY (InstrumentId) REFERENCES Instruments (InstrumentId),
  CONSTRAINT FK_IME_Eq FOREIGN KEY (EquipmentId) REFERENCES Equipment (EquipmentId)
) PRIMARY KEY (EdgeId);

-- 10a. Edge Table: Equipment -> GovernanceDoc (EXTRACTED_FROM)
CREATE TABLE EquipmentDocumentLineage (
  EdgeId STRING(128) NOT NULL,
  EntityId STRING(128) NOT NULL,
  DocId STRING(256) NOT NULL,
  SourceRef STRING(256) NOT NULL,
  HasConflict BOOL NOT NULL,
  CONSTRAINT FK_EDL_Eq FOREIGN KEY (EntityId) REFERENCES Equipment (EquipmentId),
  CONSTRAINT FK_EDL_Doc FOREIGN KEY (DocId) REFERENCES GovernanceDocs (DocId)
) PRIMARY KEY (EdgeId);

-- 10b. Edge Table: Instrument -> GovernanceDoc (EXTRACTED_FROM)
CREATE TABLE InstrumentDocumentLineage (
  EdgeId STRING(128) NOT NULL,
  EntityId STRING(128) NOT NULL,
  DocId STRING(256) NOT NULL,
  SourceRef STRING(256) NOT NULL,
  HasConflict BOOL NOT NULL,
  CONSTRAINT FK_IDL_Inst FOREIGN KEY (EntityId) REFERENCES Instruments (InstrumentId),
  CONSTRAINT FK_IDL_Doc FOREIGN KEY (DocId) REFERENCES GovernanceDocs (DocId)
) PRIMARY KEY (EdgeId);

-- 10c. Edge Table: PlantUnit -> GovernanceDoc (EXTRACTED_FROM)
CREATE TABLE UnitDocumentLineage (
  EdgeId STRING(128) NOT NULL,
  EntityId STRING(128) NOT NULL,
  DocId STRING(256) NOT NULL,
  SourceRef STRING(256) NOT NULL,
  HasConflict BOOL NOT NULL,
  CONSTRAINT FK_UDL_Unit FOREIGN KEY (EntityId) REFERENCES PlantUnits (UnitId),
  CONSTRAINT FK_UDL_Doc FOREIGN KEY (DocId) REFERENCES GovernanceDocs (DocId)
) PRIMARY KEY (EdgeId);

-- 11a. Edge Table: Equipment -> GovernanceDoc (GOVERNED_BY)
CREATE TABLE EquipmentSafetyGovernance (
  EdgeId STRING(128) NOT NULL,
  EntityId STRING(128) NOT NULL,
  DocId STRING(256) NOT NULL,
  GovernanceReason STRING(512) NOT NULL,
  CONSTRAINT FK_ESG_Eq FOREIGN KEY (EntityId) REFERENCES Equipment (EquipmentId),
  CONSTRAINT FK_ESG_Doc FOREIGN KEY (DocId) REFERENCES GovernanceDocs (DocId)
) PRIMARY KEY (EdgeId);

-- 11b. Edge Table: Instrument -> GovernanceDoc (GOVERNED_BY)
CREATE TABLE InstrumentSafetyGovernance (
  EdgeId STRING(128) NOT NULL,
  EntityId STRING(128) NOT NULL,
  DocId STRING(256) NOT NULL,
  GovernanceReason STRING(512) NOT NULL,
  CONSTRAINT FK_ISG_Inst FOREIGN KEY (EntityId) REFERENCES Instruments (InstrumentId),
  CONSTRAINT FK_ISG_Doc FOREIGN KEY (DocId) REFERENCES GovernanceDocs (DocId)
) PRIMARY KEY (EdgeId);

-- 12. Unified Section Chunks Table for Full-Text, Vector & RRF Hybrid Search
CREATE TABLE OkfChunks (
  ChunkId STRING(320) NOT NULL,
  EntityId STRING(256) NOT NULL,
  EntityLabel STRING(64) NOT NULL,
  ChunkIndex INT64 NOT NULL,
  SectionHeading STRING(512) NOT NULL,
  Tag STRING(128) NOT NULL,
  Title STRING(512) NOT NULL,
  UnitCode STRING(64),
  SafetyClassification STRING(128),
  HasConflict BOOL NOT NULL,
  GcsUri STRING(1024) NOT NULL,
  ChunkText STRING(MAX) NOT NULL,
  ChunkTokens TOKENLIST AS (
    TOKENIZE_FULLTEXT(ChunkText)
  ) HIDDEN,
  TagTokens TOKENLIST AS (
    TOKENIZE_SUBSTRING(Tag)
  ) HIDDEN,
  Embedding ARRAY<FLOAT32>(vector_length => ${EMBEDDING_DIMENSION}),
  UpdatedAt TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true)
) PRIMARY KEY (ChunkId);

CREATE SEARCH INDEX OkfChunksSearchIdx
  ON OkfChunks(ChunkTokens, TagTokens)
  STORING (EntityId, EntityLabel, SectionHeading, Tag, Title, UnitCode, SafetyClassification, HasConflict, GcsUri, ChunkText);

CREATE INDEX OkfChunksByEntityIdx ON OkfChunks(EntityId, ChunkIndex);

-- 13. Rich 5-Node / 5-Label Spanner Property Graph (ISO GQL)
CREATE OR REPLACE PROPERTY GRAPH ${SPANNER_GRAPH_NAME}
  NODE TABLES (
    PlantUnits AS PlantUnit
      KEY (UnitId)
      LABEL PlantUnit PROPERTIES (
        UnitId, UnitCode, Title, Facility, SafetyClassification, Description, HasWarning, GcsUri
      ),
    Equipment AS Equipment
      KEY (EquipmentId)
      LABEL Equipment PROPERTIES (
        EquipmentId, Tag, Title, EquipmentClass, UnitCode, SafetyClassification, HasConflict, ConflictSummary, Description, GcsUri
      ),
    Instruments AS Instrument
      KEY (InstrumentId)
      LABEL Instrument PROPERTIES (
        InstrumentId, Tag, Title, InstrumentType, UnitCode, SafetyClassification, Location, SetpointOrRange, InterlockOrAlarm, HasWarning, IsFullSpec, Description, GcsUri
      ),
    ProcessBoundaries AS ProcessBoundary
      KEY (BoundaryId)
      LABEL ProcessBoundary PROPERTIES (
        BoundaryId, Tag, BoundaryType, Description
      ),
    GovernanceDocs AS GovernanceDoc
      KEY (DocId)
      LABEL GovernanceDoc PROPERTIES (
        DocId, DocType, Tag, Title, GoverningStandard, HasWarning, Description, GcsUri
      )
  )
  EDGE TABLES (
    UnitEquipment
      KEY (EdgeId)
      SOURCE KEY (EquipmentId) REFERENCES Equipment (EquipmentId)
      DESTINATION KEY (UnitId) REFERENCES PlantUnit (UnitId)
      LABEL BELONGS_TO_UNIT PROPERTIES (EdgeId, RelationshipRole),

    EquipmentFlows
      KEY (EdgeId)
      SOURCE KEY (SrcId) REFERENCES Equipment (EquipmentId)
      DESTINATION KEY (DstId) REFERENCES Equipment (EquipmentId)
      LABEL FLOWS_TO PROPERTIES (EdgeId, StreamId, Direction, LineSize, InlineComponents, Temperature, Pressure, SourceDrawing, Description),

    BoundaryToEquipmentFlows
      KEY (EdgeId)
      SOURCE KEY (SrcId) REFERENCES ProcessBoundary (BoundaryId)
      DESTINATION KEY (DstId) REFERENCES Equipment (EquipmentId)
      LABEL FLOWS_TO PROPERTIES (EdgeId, StreamId, Direction, LineSize, InlineComponents, Temperature, Pressure, SourceDrawing, Description),

    EquipmentToBoundaryFlows
      KEY (EdgeId)
      SOURCE KEY (SrcId) REFERENCES Equipment (EquipmentId)
      DESTINATION KEY (DstId) REFERENCES ProcessBoundary (BoundaryId)
      LABEL FLOWS_TO PROPERTIES (EdgeId, StreamId, Direction, LineSize, InlineComponents, Temperature, Pressure, SourceDrawing, Description),

    InstrumentMonitorsEquipment
      KEY (EdgeId)
      SOURCE KEY (InstrumentId) REFERENCES Instrument (InstrumentId)
      DESTINATION KEY (EquipmentId) REFERENCES Equipment (EquipmentId)
      LABEL MONITORS PROPERTIES (EdgeId, LoopRole, Location, SetpointOrRange, InterlockOrAlarm, SourceDrawing),

    EquipmentDocumentLineage
      KEY (EdgeId)
      SOURCE KEY (EntityId) REFERENCES Equipment (EquipmentId)
      DESTINATION KEY (DocId) REFERENCES GovernanceDoc (DocId)
      LABEL EXTRACTED_FROM PROPERTIES (EdgeId, SourceRef, HasConflict),

    InstrumentDocumentLineage
      KEY (EdgeId)
      SOURCE KEY (EntityId) REFERENCES Instrument (InstrumentId)
      DESTINATION KEY (DocId) REFERENCES GovernanceDoc (DocId)
      LABEL EXTRACTED_FROM PROPERTIES (EdgeId, SourceRef, HasConflict),

    UnitDocumentLineage
      KEY (EdgeId)
      SOURCE KEY (EntityId) REFERENCES PlantUnit (UnitId)
      DESTINATION KEY (DocId) REFERENCES GovernanceDoc (DocId)
      LABEL EXTRACTED_FROM PROPERTIES (EdgeId, SourceRef, HasConflict),

    EquipmentSafetyGovernance
      KEY (EdgeId)
      SOURCE KEY (EntityId) REFERENCES Equipment (EquipmentId)
      DESTINATION KEY (DocId) REFERENCES GovernanceDoc (DocId)
      LABEL GOVERNED_BY PROPERTIES (EdgeId, GovernanceReason),

    InstrumentSafetyGovernance
      KEY (EdgeId)
      SOURCE KEY (EntityId) REFERENCES Instrument (InstrumentId)
      DESTINATION KEY (DocId) REFERENCES GovernanceDoc (DocId)
      LABEL GOVERNED_BY PROPERTIES (EdgeId, GovernanceReason)
  );
