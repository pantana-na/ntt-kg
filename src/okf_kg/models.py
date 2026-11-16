"""Domain models for the 5-Node / 5-Label Spanner Property Graph, Hybrid Search Chunks, and Dataplex Catalog."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PlantUnitNode:
    unit_id: str
    unit_code: str
    title: str
    facility: str
    safety_classification: Optional[str]
    description: str
    has_warning: bool
    gcs_uri: Optional[str]


@dataclass(frozen=True)
class EquipmentNode:
    equipment_id: str
    tag: str
    title: str
    equipment_class: str
    unit_code: str
    safety_classification: Optional[str]
    has_conflict: bool
    conflict_summary: Optional[str]
    description: str
    gcs_uri: str


@dataclass(frozen=True)
class InstrumentNode:
    instrument_id: str
    tag: str
    title: str
    instrument_type: str
    unit_code: Optional[str]
    safety_classification: Optional[str]
    location: Optional[str]
    setpoint_or_range: Optional[str]
    interlock_or_alarm: Optional[str]
    has_warning: bool
    is_full_spec: bool
    description: str
    gcs_uri: Optional[str]


@dataclass(frozen=True)
class ProcessBoundaryNode:
    boundary_id: str
    tag: str
    boundary_type: str
    description: str


@dataclass(frozen=True)
class GovernanceDocNode:
    doc_id: str
    doc_type: str
    tag: str
    title: str
    governing_standard: Optional[str]
    has_warning: bool
    description: str
    gcs_uri: str


@dataclass(frozen=True)
class UnitEquipmentEdge:
    edge_id: str
    equipment_id: str
    unit_id: str
    relationship_role: str


@dataclass(frozen=True)
class FlowStreamEdge:
    edge_id: str
    src_id: str
    dst_id: str
    src_kind: str  # EQUIPMENT | BOUNDARY
    dst_kind: str  # EQUIPMENT | BOUNDARY
    stream_id: str
    direction: str
    line_size: Optional[str]
    inline_components: Optional[str]
    temperature: Optional[str]
    pressure: Optional[str]
    source_drawing: Optional[str]
    description: Optional[str]


@dataclass(frozen=True)
class InstrumentMonitorEdge:
    edge_id: str
    instrument_id: str
    equipment_id: str
    loop_role: str
    location: Optional[str]
    setpoint_or_range: Optional[str]
    interlock_or_alarm: Optional[str]
    source_drawing: Optional[str]


@dataclass(frozen=True)
class DocumentLineageEdge:
    edge_id: str
    entity_id: str
    entity_kind: str  # EQUIPMENT | INSTRUMENT | UNIT
    doc_id: str
    source_ref: str
    has_conflict: bool


@dataclass(frozen=True)
class SafetyGovernanceEdge:
    edge_id: str
    entity_id: str
    entity_kind: str  # EQUIPMENT | INSTRUMENT
    doc_id: str
    governance_reason: str


@dataclass(frozen=True)
class OkfChunkRecord:
    chunk_id: str
    entity_id: str
    entity_label: str  # Equipment | Instrument | PlantUnit | GovernanceDoc
    chunk_index: int
    section_heading: str
    tag: str
    title: str
    unit_code: Optional[str]
    safety_classification: Optional[str]
    has_conflict: bool
    gcs_uri: str
    chunk_text: str


@dataclass(frozen=True)
class CatalogEntrySpec:
    entry_id: str
    spanner_entity_id: str
    entity_type: str
    tag: str
    display_name: str
    description: str
    unit_code: str
    equipment_or_instrument_class: str
    safety_classification: str
    has_discrepancy_warning: bool
    governing_standard_or_drawing: str
    gcs_markdown_uri: str
    overview_markdown: str
    labels: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class ParsedOkfBundle:
    units: Dict[str, PlantUnitNode]
    equipment: Dict[str, EquipmentNode]
    instruments: Dict[str, InstrumentNode]
    boundaries: Dict[str, ProcessBoundaryNode]
    governance_docs: Dict[str, GovernanceDocNode]
    unit_edges: List[UnitEquipmentEdge]
    flow_edges: List[FlowStreamEdge]
    monitor_edges: List[InstrumentMonitorEdge]
    lineage_edges: List[DocumentLineageEdge]
    governance_edges: List[SafetyGovernanceEdge]
    chunks: List[OkfChunkRecord]
    catalog_entries: List[CatalogEntrySpec]
