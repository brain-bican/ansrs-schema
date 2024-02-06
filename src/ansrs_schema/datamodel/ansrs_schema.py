# Auto generated from ansrs_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-02-06T10:46:00
# Schema: ansrs-schema
#
# id: https://w3id.org/my-org/ansrs-schema
# description: Schema for ANSRS
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ANSRS = CurieNamespace('ANSRS', 'https://w3id.org/my-org/ansrs-schema/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ANSRS = CurieNamespace('ansrs', 'https://w3id.org/my-org/ansrs-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = ANSRS


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ParcellationTermSetId(NamedThingId):
    pass


class ParcellationTermId(NamedThingId):
    pass


class VersionedNamedThingId(NamedThingId):
    pass


class ImageDatasetId(VersionedNamedThingId):
    pass


class AnatomicalSpaceId(VersionedNamedThingId):
    pass


class ParcellationTerminologyId(VersionedNamedThingId):
    pass


class ParcellationColorSchemeId(VersionedNamedThingId):
    pass


class AnatomicalAnnotationSetId(VersionedNamedThingId):
    pass


class ParcellationAtlasId(VersionedNamedThingId):
    pass


@dataclass
class ParcellationColorAssignment(YAMLRoot):
    """
    The parcellation color assignment associates hex color value to a parcellation term within a versioned release of
    a color scheme. A parcellation term is uniquely denoted by a parcellation term identifier and the parcellation
    terminology it belongs to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationColorAssignment"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationColorAssignment"
    class_name: ClassVar[str] = "ParcellationColorAssignment"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationColorAssignment

    part_of_parcellation_color_scheme: Union[str, ParcellationColorSchemeId] = None
    subject_parcellation_term: Union[str, ParcellationTermId] = None
    color: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.part_of_parcellation_color_scheme):
            self.MissingRequiredField("part_of_parcellation_color_scheme")
        if not isinstance(self.part_of_parcellation_color_scheme, ParcellationColorSchemeId):
            self.part_of_parcellation_color_scheme = ParcellationColorSchemeId(self.part_of_parcellation_color_scheme)

        if self._is_empty(self.subject_parcellation_term):
            self.MissingRequiredField("subject_parcellation_term")
        if not isinstance(self.subject_parcellation_term, ParcellationTermId):
            self.subject_parcellation_term = ParcellationTermId(self.subject_parcellation_term)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationAnnotation(YAMLRoot):
    """
    A parcellation annotation defines a specific segment of an anatomical space denoted by an internal identifier and
    is a unique and exclusive member of a versioned release anatomical annotation set. For example, in the case where
    the anatomical annotation set is a single multi-value image mask (e.g. Allen Mouse CCF), a specific annotation
    corresponds to a specific label index (internal identifier) in the mask.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationAnnotation"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationAnnotation"
    class_name: ClassVar[str] = "ParcellationAnnotation"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationAnnotation

    part_of_anatomical_annotation_set: Union[str, AnatomicalAnnotationSetId] = None
    internal_identifier: str = None
    voxel_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.part_of_anatomical_annotation_set):
            self.MissingRequiredField("part_of_anatomical_annotation_set")
        if not isinstance(self.part_of_anatomical_annotation_set, AnatomicalAnnotationSetId):
            self.part_of_anatomical_annotation_set = AnatomicalAnnotationSetId(self.part_of_anatomical_annotation_set)

        if self._is_empty(self.internal_identifier):
            self.MissingRequiredField("internal_identifier")
        if not isinstance(self.internal_identifier, str):
            self.internal_identifier = str(self.internal_identifier)

        if self.voxel_count is not None and not isinstance(self.voxel_count, int):
            self.voxel_count = int(self.voxel_count)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationAnnotationTermMap(YAMLRoot):
    """
    The parcellation annotation term map table defines the relationship between parcellation annotations and
    parcellation terms. A parcellation term is uniquely denoted by a parcellation term identifier and the parcellation
    terminology it belongs to. A parcellation term can be spatially parameterized by the union of one or more
    parcellation annotations within a versioned release of an anatomical annotation set. For example, annotations
    defining individual cortical layers in cortical region R (R1, R2/3, R4, etc) can be combined to define the parent
    region R.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationAnnotationTermMap"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationAnnotationTermMap"
    class_name: ClassVar[str] = "ParcellationAnnotationTermMap"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationAnnotationTermMap

    subject_parcellation_annotation: Union[dict, ParcellationAnnotation] = None
    subject_parcellation_term: Union[str, ParcellationTermId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_parcellation_annotation):
            self.MissingRequiredField("subject_parcellation_annotation")
        if not isinstance(self.subject_parcellation_annotation, ParcellationAnnotation):
            self.subject_parcellation_annotation = ParcellationAnnotation(**as_dict(self.subject_parcellation_annotation))

        if self._is_empty(self.subject_parcellation_term):
            self.MissingRequiredField("subject_parcellation_term")
        if not isinstance(self.subject_parcellation_term, ParcellationTermId):
            self.subject_parcellation_term = ParcellationTermId(self.subject_parcellation_term)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    Core base entity for ANSRS schema representing an entity with an identifier  name and description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["NamedThing"]
    class_class_curie: ClassVar[str] = "ANSRS:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = ANSRS.NamedThing

    id: Union[str, NamedThingId] = None
    name: str = None
    description: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationTermSet(NamedThing):
    """
    A parcellation term set is the set of parcellation terms within a specific parcellation terminology. A
    parcellation term set belongs to one and only one parcellation terminology and each parcellation term in a
    parcellation terminology belongs to one and only one term set. If the parcellation terminology is a taxonomy,
    parcellation term sets can be used to represent taxonomic ranks. For consistency, if the terminology does not have
    the notion of taxonomic ranks, all terms are grouped into a single parcellation term set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationTermSet"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationTermSet"
    class_name: ClassVar[str] = "ParcellationTermSet"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationTermSet

    id: Union[str, ParcellationTermSetId] = None
    name: str = None
    description: str = None
    part_of_parcellation_terminology: Union[str, ParcellationTerminologyId] = None
    ordinal: Optional[int] = None
    has_parent_parcellation_term_set: Optional[Union[str, ParcellationTermSetId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParcellationTermSetId):
            self.id = ParcellationTermSetId(self.id)

        if self._is_empty(self.part_of_parcellation_terminology):
            self.MissingRequiredField("part_of_parcellation_terminology")
        if not isinstance(self.part_of_parcellation_terminology, ParcellationTerminologyId):
            self.part_of_parcellation_terminology = ParcellationTerminologyId(self.part_of_parcellation_terminology)

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if self.has_parent_parcellation_term_set is not None and not isinstance(self.has_parent_parcellation_term_set, ParcellationTermSetId):
            self.has_parent_parcellation_term_set = ParcellationTermSetId(self.has_parent_parcellation_term_set)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationTerm(NamedThing):
    """
    A parcellation term is an individual term within a specific parcellation terminology describing a single
    anatomical entity by a persistent identifier, name, symbol and description. A parcellation term is a unique and
    exclusive member of a versioned release parcellation terminology. Although term identifiers must be unique within
    the context of one versioned release of a parcellation terminology, they can be reused in different parcellation
    terminology versions enabling the representation of terminology updates and modifications over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationTerm"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationTerm"
    class_name: ClassVar[str] = "ParcellationTerm"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationTerm

    id: Union[str, ParcellationTermId] = None
    name: str = None
    description: str = None
    part_of_parcellation_term_set: Union[str, ParcellationTermSetId] = None
    symbol: Optional[str] = None
    ordinal: Optional[int] = None
    has_parent_parcellation_term: Optional[Union[str, ParcellationTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParcellationTermId):
            self.id = ParcellationTermId(self.id)

        if self._is_empty(self.part_of_parcellation_term_set):
            self.MissingRequiredField("part_of_parcellation_term_set")
        if not isinstance(self.part_of_parcellation_term_set, ParcellationTermSetId):
            self.part_of_parcellation_term_set = ParcellationTermSetId(self.part_of_parcellation_term_set)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.ordinal is not None and not isinstance(self.ordinal, int):
            self.ordinal = int(self.ordinal)

        if self.has_parent_parcellation_term is not None and not isinstance(self.has_parent_parcellation_term, ParcellationTermId):
            self.has_parent_parcellation_term = ParcellationTermId(self.has_parent_parcellation_term)

        super().__post_init__(**kwargs)


@dataclass
class VersionedNamedThing(NamedThing):
    """
    Core base entity for ANSRS schema representing an versioned named thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["VersionedNamedThing"]
    class_class_curie: ClassVar[str] = "ANSRS:VersionedNamedThing"
    class_name: ClassVar[str] = "VersionedNamedThing"
    class_model_uri: ClassVar[URIRef] = ANSRS.VersionedNamedThing

    id: Union[str, VersionedNamedThingId] = None
    name: str = None
    description: str = None
    version: str = None
    revision_of: Optional[Union[str, VersionedNamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.revision_of is not None and not isinstance(self.revision_of, VersionedNamedThingId):
            self.revision_of = VersionedNamedThingId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class ImageDataset(VersionedNamedThing):
    """
    An image dataset is versioned release of a multidimensional regular grid of measurements and metadata required for
    a morphological representation of an entity such as an anatomical structure (ref: OBI_0003327, RRID:SCR_006266)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ImageDataset"]
    class_class_curie: ClassVar[str] = "ANSRS:ImageDataset"
    class_name: ClassVar[str] = "ImageDataset"
    class_model_uri: ClassVar[URIRef] = ANSRS.ImageDataset

    id: Union[str, ImageDatasetId] = None
    name: str = None
    description: str = None
    version: str = None
    x_direction: Optional[Union[str, "ANATOMICALDIRECTION"]] = None
    y_direction: Optional[Union[str, "ANATOMICALDIRECTION"]] = None
    z_direction: Optional[Union[str, "ANATOMICALDIRECTION"]] = None
    x_size: Optional[int] = None
    y_size: Optional[int] = None
    z_size: Optional[int] = None
    x_resolution: Optional[float] = None
    y_resolution: Optional[float] = None
    z_resolution: Optional[float] = None
    unit: Optional[Union[str, "DISTANCEUNIT"]] = None
    revision_of: Optional[Union[str, ImageDatasetId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageDatasetId):
            self.id = ImageDatasetId(self.id)

        if self.x_direction is not None and not isinstance(self.x_direction, ANATOMICALDIRECTION):
            self.x_direction = ANATOMICALDIRECTION(self.x_direction)

        if self.y_direction is not None and not isinstance(self.y_direction, ANATOMICALDIRECTION):
            self.y_direction = ANATOMICALDIRECTION(self.y_direction)

        if self.z_direction is not None and not isinstance(self.z_direction, ANATOMICALDIRECTION):
            self.z_direction = ANATOMICALDIRECTION(self.z_direction)

        if self.x_size is not None and not isinstance(self.x_size, int):
            self.x_size = int(self.x_size)

        if self.y_size is not None and not isinstance(self.y_size, int):
            self.y_size = int(self.y_size)

        if self.z_size is not None and not isinstance(self.z_size, int):
            self.z_size = int(self.z_size)

        if self.x_resolution is not None and not isinstance(self.x_resolution, float):
            self.x_resolution = float(self.x_resolution)

        if self.y_resolution is not None and not isinstance(self.y_resolution, float):
            self.y_resolution = float(self.y_resolution)

        if self.z_resolution is not None and not isinstance(self.z_resolution, float):
            self.z_resolution = float(self.z_resolution)

        if self.unit is not None and not isinstance(self.unit, DISTANCEUNIT):
            self.unit = DISTANCEUNIT(self.unit)

        if self.revision_of is not None and not isinstance(self.revision_of, ImageDatasetId):
            self.revision_of = ImageDatasetId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalSpace(VersionedNamedThing):
    """
    An anatomical space is versioned release of a mathematical space with a defined mapping between the anatomical
    axes and the mathematical axes. An anatomical space may be defined by a reference image chosen as the biological
    reference for an anatomical structure of interest derived from a single or multiple specimens (ref: ILX:0777106,
    RRID:SCR_023499)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["AnatomicalSpace"]
    class_class_curie: ClassVar[str] = "ANSRS:AnatomicalSpace"
    class_name: ClassVar[str] = "AnatomicalSpace"
    class_model_uri: ClassVar[URIRef] = ANSRS.AnatomicalSpace

    id: Union[str, AnatomicalSpaceId] = None
    name: str = None
    description: str = None
    version: str = None
    measures: Union[str, ImageDatasetId] = None
    revision_of: Optional[Union[str, AnatomicalSpaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalSpaceId):
            self.id = AnatomicalSpaceId(self.id)

        if self._is_empty(self.measures):
            self.MissingRequiredField("measures")
        if not isinstance(self.measures, ImageDatasetId):
            self.measures = ImageDatasetId(self.measures)

        if self.revision_of is not None and not isinstance(self.revision_of, AnatomicalSpaceId):
            self.revision_of = AnatomicalSpaceId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationTerminology(VersionedNamedThing):
    """
    A parcellation terminology is a versioned release set of terms that can be used to label annotations in an atlas,
    providing human readability and context and allowing communication about brain locations and structural
    properties. Typically, a terminology is a set of descriptive anatomical terms following a specific naming
    convention and/or approach to organization scheme. The terminology may be a flat list of controlled vocabulary, a
    taxonomy and partonomy, or an ontology (ref: ILX:0777107, RRID:SCR_023499)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationTerminology"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationTerminology"
    class_name: ClassVar[str] = "ParcellationTerminology"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationTerminology

    id: Union[str, ParcellationTerminologyId] = None
    name: str = None
    description: str = None
    version: str = None
    revision_of: Optional[Union[str, ParcellationTerminologyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParcellationTerminologyId):
            self.id = ParcellationTerminologyId(self.id)

        if self.revision_of is not None and not isinstance(self.revision_of, ParcellationTerminologyId):
            self.revision_of = ParcellationTerminologyId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationColorScheme(VersionedNamedThing):
    """
    A parcellation color scheme is a versioned release color palette that can be used to visualize a parcellation
    terminology or its related parcellation annotation. A parcellation terminology may have zero or more parcellation
    color schemes and each color scheme is in context of a specific parcellation terminology, where each parcellation
    term is assigned a hex color value. A parcellation color scheme is defined as a part of one and only one
    parcellation terminology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationColorScheme"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationColorScheme"
    class_name: ClassVar[str] = "ParcellationColorScheme"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationColorScheme

    id: Union[str, ParcellationColorSchemeId] = None
    name: str = None
    description: str = None
    version: str = None
    subject_parcellation_terminology: Union[str, ParcellationTerminologyId] = None
    revision_of: Optional[Union[str, ParcellationTerminologyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParcellationColorSchemeId):
            self.id = ParcellationColorSchemeId(self.id)

        if self._is_empty(self.subject_parcellation_terminology):
            self.MissingRequiredField("subject_parcellation_terminology")
        if not isinstance(self.subject_parcellation_terminology, ParcellationTerminologyId):
            self.subject_parcellation_terminology = ParcellationTerminologyId(self.subject_parcellation_terminology)

        if self.revision_of is not None and not isinstance(self.revision_of, ParcellationTerminologyId):
            self.revision_of = ParcellationTerminologyId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalAnnotationSet(VersionedNamedThing):
    """
    An anatomical annotation set is a versioned release of a set of anatomical annotations anchored in the same
    anatomical space that divides the space into distinct segments following some annotation criteria or parcellation
    scheme. For example, the anatomical annotation set of 3D image based reference atlases (e.g. Allen Mouse CCF) can
    be expressed as a set of label indices of single multi-valued image annotations or as a set of segmentation masks
    (ref: ILX:0777108, RRID:SCR_023499)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["AnatomicalAnnotationSet"]
    class_class_curie: ClassVar[str] = "ANSRS:AnatomicalAnnotationSet"
    class_name: ClassVar[str] = "AnatomicalAnnotationSet"
    class_model_uri: ClassVar[URIRef] = ANSRS.AnatomicalAnnotationSet

    id: Union[str, AnatomicalAnnotationSetId] = None
    name: str = None
    description: str = None
    version: str = None
    parameterizes: Union[str, AnatomicalSpaceId] = None
    revision_of: Optional[Union[str, ParcellationTerminologyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalAnnotationSetId):
            self.id = AnatomicalAnnotationSetId(self.id)

        if self._is_empty(self.parameterizes):
            self.MissingRequiredField("parameterizes")
        if not isinstance(self.parameterizes, AnatomicalSpaceId):
            self.parameterizes = AnatomicalSpaceId(self.parameterizes)

        if self.revision_of is not None and not isinstance(self.revision_of, ParcellationTerminologyId):
            self.revision_of = ParcellationTerminologyId(self.revision_of)

        super().__post_init__(**kwargs)


@dataclass
class ParcellationAtlas(VersionedNamedThing):
    """
    A parcellation atlas is a versioned release reference used to guide experiments or deal with the spatial
    relationship between objects or the location of objects within the context of some anatomical structure. An atlas
    is minimally defined by a notion of space (either implicit or explicit) and an annotation set. Reference atlases
    usually have additional parts that make them more useful in certain situations, such as a well defined coordinate
    system, delineations indicating the boundaries of various regions or cell populations, landmarks, and labels and
    names to make it easier to communicate about well known and useful locations (ref: ILX:0777109, RRID:SCR_023499).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANSRS["ParcellationAtlas"]
    class_class_curie: ClassVar[str] = "ANSRS:ParcellationAtlas"
    class_name: ClassVar[str] = "ParcellationAtlas"
    class_model_uri: ClassVar[URIRef] = ANSRS.ParcellationAtlas

    id: Union[str, ParcellationAtlasId] = None
    name: str = None
    description: str = None
    version: str = None
    has_anatomical_space: Union[str, AnatomicalSpaceId] = None
    has_anatomical_annotation_set: Union[str, AnatomicalAnnotationSetId] = None
    has_parcellation_terminology: Union[str, ParcellationTerminologyId] = None
    specialization_of: Optional[Union[str, ParcellationAtlasId]] = None
    revision_of: Optional[Union[str, AnatomicalSpaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParcellationAtlasId):
            self.id = ParcellationAtlasId(self.id)

        if self._is_empty(self.has_anatomical_space):
            self.MissingRequiredField("has_anatomical_space")
        if not isinstance(self.has_anatomical_space, AnatomicalSpaceId):
            self.has_anatomical_space = AnatomicalSpaceId(self.has_anatomical_space)

        if self._is_empty(self.has_anatomical_annotation_set):
            self.MissingRequiredField("has_anatomical_annotation_set")
        if not isinstance(self.has_anatomical_annotation_set, AnatomicalAnnotationSetId):
            self.has_anatomical_annotation_set = AnatomicalAnnotationSetId(self.has_anatomical_annotation_set)

        if self._is_empty(self.has_parcellation_terminology):
            self.MissingRequiredField("has_parcellation_terminology")
        if not isinstance(self.has_parcellation_terminology, ParcellationTerminologyId):
            self.has_parcellation_terminology = ParcellationTerminologyId(self.has_parcellation_terminology)

        if self.specialization_of is not None and not isinstance(self.specialization_of, ParcellationAtlasId):
            self.specialization_of = ParcellationAtlasId(self.specialization_of)

        if self.revision_of is not None and not isinstance(self.revision_of, AnatomicalSpaceId):
            self.revision_of = AnatomicalSpaceId(self.revision_of)

        super().__post_init__(**kwargs)


# Enumerations
class ANATOMICALDIRECTION(EnumDefinitionImpl):

    left_to_right = PermissibleValue(
        text="left_to_right",
        description="A controlled vocabulary term defining the x axis direction in terms of  anatomical direction.")
    posterior_to_anterior = PermissibleValue(text="posterior_to_anterior")
    inferior_to_superior = PermissibleValue(text="inferior_to_superior")

    _defn = EnumDefinition(
        name="ANATOMICALDIRECTION",
    )

class DISTANCEUNIT(EnumDefinitionImpl):

    mm = PermissibleValue(text="mm")
    um = PermissibleValue(text="um")
    m = PermissibleValue(text="m")

    _defn = EnumDefinition(
        name="DISTANCEUNIT",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ANSRS.id, name="id", curie=ANSRS.curie('id'),
                   model_uri=ANSRS.id, domain=None, range=URIRef)

slots.name = Slot(uri=ANSRS.name, name="name", curie=ANSRS.curie('name'),
                   model_uri=ANSRS.name, domain=None, range=str)

slots.description = Slot(uri=ANSRS.description, name="description", curie=ANSRS.curie('description'),
                   model_uri=ANSRS.description, domain=None, range=str)

slots.version = Slot(uri=ANSRS.version, name="version", curie=ANSRS.curie('version'),
                   model_uri=ANSRS.version, domain=None, range=str)

slots.revision_of = Slot(uri=ANSRS.revision_of, name="revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.revision_of, domain=None, range=Optional[Union[str, VersionedNamedThingId]])

slots.imageDataset__x_direction = Slot(uri=ANSRS.x_direction, name="imageDataset__x_direction", curie=ANSRS.curie('x_direction'),
                   model_uri=ANSRS.imageDataset__x_direction, domain=None, range=Optional[Union[str, "ANATOMICALDIRECTION"]])

slots.imageDataset__y_direction = Slot(uri=ANSRS.y_direction, name="imageDataset__y_direction", curie=ANSRS.curie('y_direction'),
                   model_uri=ANSRS.imageDataset__y_direction, domain=None, range=Optional[Union[str, "ANATOMICALDIRECTION"]])

slots.imageDataset__z_direction = Slot(uri=ANSRS.z_direction, name="imageDataset__z_direction", curie=ANSRS.curie('z_direction'),
                   model_uri=ANSRS.imageDataset__z_direction, domain=None, range=Optional[Union[str, "ANATOMICALDIRECTION"]])

slots.imageDataset__x_size = Slot(uri=ANSRS.x_size, name="imageDataset__x_size", curie=ANSRS.curie('x_size'),
                   model_uri=ANSRS.imageDataset__x_size, domain=None, range=Optional[int])

slots.imageDataset__y_size = Slot(uri=ANSRS.y_size, name="imageDataset__y_size", curie=ANSRS.curie('y_size'),
                   model_uri=ANSRS.imageDataset__y_size, domain=None, range=Optional[int])

slots.imageDataset__z_size = Slot(uri=ANSRS.z_size, name="imageDataset__z_size", curie=ANSRS.curie('z_size'),
                   model_uri=ANSRS.imageDataset__z_size, domain=None, range=Optional[int])

slots.imageDataset__x_resolution = Slot(uri=ANSRS.x_resolution, name="imageDataset__x_resolution", curie=ANSRS.curie('x_resolution'),
                   model_uri=ANSRS.imageDataset__x_resolution, domain=None, range=Optional[float])

slots.imageDataset__y_resolution = Slot(uri=ANSRS.y_resolution, name="imageDataset__y_resolution", curie=ANSRS.curie('y_resolution'),
                   model_uri=ANSRS.imageDataset__y_resolution, domain=None, range=Optional[float])

slots.imageDataset__z_resolution = Slot(uri=ANSRS.z_resolution, name="imageDataset__z_resolution", curie=ANSRS.curie('z_resolution'),
                   model_uri=ANSRS.imageDataset__z_resolution, domain=None, range=Optional[float])

slots.imageDataset__unit = Slot(uri=ANSRS.unit, name="imageDataset__unit", curie=ANSRS.curie('unit'),
                   model_uri=ANSRS.imageDataset__unit, domain=None, range=Optional[Union[str, "DISTANCEUNIT"]])

slots.anatomicalSpace__measures = Slot(uri=ANSRS.measures, name="anatomicalSpace__measures", curie=ANSRS.curie('measures'),
                   model_uri=ANSRS.anatomicalSpace__measures, domain=None, range=Union[str, ImageDatasetId])

slots.parcellationTermSet__part_of_parcellation_terminology = Slot(uri=ANSRS.part_of_parcellation_terminology, name="parcellationTermSet__part_of_parcellation_terminology", curie=ANSRS.curie('part_of_parcellation_terminology'),
                   model_uri=ANSRS.parcellationTermSet__part_of_parcellation_terminology, domain=None, range=Union[str, ParcellationTerminologyId])

slots.parcellationTermSet__ordinal = Slot(uri=ANSRS.ordinal, name="parcellationTermSet__ordinal", curie=ANSRS.curie('ordinal'),
                   model_uri=ANSRS.parcellationTermSet__ordinal, domain=None, range=Optional[int])

slots.parcellationTermSet__has_parent_parcellation_term_set = Slot(uri=ANSRS.has_parent_parcellation_term_set, name="parcellationTermSet__has_parent_parcellation_term_set", curie=ANSRS.curie('has_parent_parcellation_term_set'),
                   model_uri=ANSRS.parcellationTermSet__has_parent_parcellation_term_set, domain=None, range=Optional[Union[str, ParcellationTermSetId]])

slots.parcellationTerm__symbol = Slot(uri=ANSRS.symbol, name="parcellationTerm__symbol", curie=ANSRS.curie('symbol'),
                   model_uri=ANSRS.parcellationTerm__symbol, domain=None, range=Optional[str])

slots.parcellationTerm__part_of_parcellation_term_set = Slot(uri=ANSRS.part_of_parcellation_term_set, name="parcellationTerm__part_of_parcellation_term_set", curie=ANSRS.curie('part_of_parcellation_term_set'),
                   model_uri=ANSRS.parcellationTerm__part_of_parcellation_term_set, domain=None, range=Union[str, ParcellationTermSetId])

slots.parcellationTerm__ordinal = Slot(uri=ANSRS.ordinal, name="parcellationTerm__ordinal", curie=ANSRS.curie('ordinal'),
                   model_uri=ANSRS.parcellationTerm__ordinal, domain=None, range=Optional[int])

slots.parcellationTerm__has_parent_parcellation_term = Slot(uri=ANSRS.has_parent_parcellation_term, name="parcellationTerm__has_parent_parcellation_term", curie=ANSRS.curie('has_parent_parcellation_term'),
                   model_uri=ANSRS.parcellationTerm__has_parent_parcellation_term, domain=None, range=Optional[Union[str, ParcellationTermId]])

slots.parcellationColorScheme__subject_parcellation_terminology = Slot(uri=ANSRS.subject_parcellation_terminology, name="parcellationColorScheme__subject_parcellation_terminology", curie=ANSRS.curie('subject_parcellation_terminology'),
                   model_uri=ANSRS.parcellationColorScheme__subject_parcellation_terminology, domain=None, range=Union[str, ParcellationTerminologyId])

slots.parcellationColorAssignment__part_of_parcellation_color_scheme = Slot(uri=ANSRS.part_of_parcellation_color_scheme, name="parcellationColorAssignment__part_of_parcellation_color_scheme", curie=ANSRS.curie('part_of_parcellation_color_scheme'),
                   model_uri=ANSRS.parcellationColorAssignment__part_of_parcellation_color_scheme, domain=None, range=Union[str, ParcellationColorSchemeId])

slots.parcellationColorAssignment__subject_parcellation_term = Slot(uri=ANSRS.subject_parcellation_term, name="parcellationColorAssignment__subject_parcellation_term", curie=ANSRS.curie('subject_parcellation_term'),
                   model_uri=ANSRS.parcellationColorAssignment__subject_parcellation_term, domain=None, range=Union[str, ParcellationTermId])

slots.parcellationColorAssignment__color = Slot(uri=ANSRS.color, name="parcellationColorAssignment__color", curie=ANSRS.curie('color'),
                   model_uri=ANSRS.parcellationColorAssignment__color, domain=None, range=Optional[str])

slots.anatomicalAnnotationSet__parameterizes = Slot(uri=ANSRS.parameterizes, name="anatomicalAnnotationSet__parameterizes", curie=ANSRS.curie('parameterizes'),
                   model_uri=ANSRS.anatomicalAnnotationSet__parameterizes, domain=None, range=Union[str, AnatomicalSpaceId])

slots.parcellationAnnotation__part_of_anatomical_annotation_set = Slot(uri=ANSRS.part_of_anatomical_annotation_set, name="parcellationAnnotation__part_of_anatomical_annotation_set", curie=ANSRS.curie('part_of_anatomical_annotation_set'),
                   model_uri=ANSRS.parcellationAnnotation__part_of_anatomical_annotation_set, domain=None, range=Union[str, AnatomicalAnnotationSetId])

slots.parcellationAnnotation__internal_identifier = Slot(uri=ANSRS.internal_identifier, name="parcellationAnnotation__internal_identifier", curie=ANSRS.curie('internal_identifier'),
                   model_uri=ANSRS.parcellationAnnotation__internal_identifier, domain=None, range=str)

slots.parcellationAnnotation__voxel_count = Slot(uri=ANSRS.voxel_count, name="parcellationAnnotation__voxel_count", curie=ANSRS.curie('voxel_count'),
                   model_uri=ANSRS.parcellationAnnotation__voxel_count, domain=None, range=Optional[int])

slots.parcellationAnnotationTermMap__subject_parcellation_annotation = Slot(uri=ANSRS.subject_parcellation_annotation, name="parcellationAnnotationTermMap__subject_parcellation_annotation", curie=ANSRS.curie('subject_parcellation_annotation'),
                   model_uri=ANSRS.parcellationAnnotationTermMap__subject_parcellation_annotation, domain=None, range=Union[dict, ParcellationAnnotation])

slots.parcellationAnnotationTermMap__subject_parcellation_term = Slot(uri=ANSRS.subject_parcellation_term, name="parcellationAnnotationTermMap__subject_parcellation_term", curie=ANSRS.curie('subject_parcellation_term'),
                   model_uri=ANSRS.parcellationAnnotationTermMap__subject_parcellation_term, domain=None, range=Union[str, ParcellationTermId])

slots.parcellationAtlas__has_anatomical_space = Slot(uri=ANSRS.has_anatomical_space, name="parcellationAtlas__has_anatomical_space", curie=ANSRS.curie('has_anatomical_space'),
                   model_uri=ANSRS.parcellationAtlas__has_anatomical_space, domain=None, range=Union[str, AnatomicalSpaceId])

slots.parcellationAtlas__has_anatomical_annotation_set = Slot(uri=ANSRS.has_anatomical_annotation_set, name="parcellationAtlas__has_anatomical_annotation_set", curie=ANSRS.curie('has_anatomical_annotation_set'),
                   model_uri=ANSRS.parcellationAtlas__has_anatomical_annotation_set, domain=None, range=Union[str, AnatomicalAnnotationSetId])

slots.parcellationAtlas__has_parcellation_terminology = Slot(uri=ANSRS.has_parcellation_terminology, name="parcellationAtlas__has_parcellation_terminology", curie=ANSRS.curie('has_parcellation_terminology'),
                   model_uri=ANSRS.parcellationAtlas__has_parcellation_terminology, domain=None, range=Union[str, ParcellationTerminologyId])

slots.parcellationAtlas__specialization_of = Slot(uri=ANSRS.specialization_of, name="parcellationAtlas__specialization_of", curie=ANSRS.curie('specialization_of'),
                   model_uri=ANSRS.parcellationAtlas__specialization_of, domain=None, range=Optional[Union[str, ParcellationAtlasId]])

slots.ImageDataset_revision_of = Slot(uri=ANSRS.revision_of, name="ImageDataset_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.ImageDataset_revision_of, domain=ImageDataset, range=Optional[Union[str, ImageDatasetId]])

slots.AnatomicalSpace_revision_of = Slot(uri=ANSRS.revision_of, name="AnatomicalSpace_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.AnatomicalSpace_revision_of, domain=AnatomicalSpace, range=Optional[Union[str, AnatomicalSpaceId]])

slots.ParcellationTerminology_revision_of = Slot(uri=ANSRS.revision_of, name="ParcellationTerminology_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.ParcellationTerminology_revision_of, domain=ParcellationTerminology, range=Optional[Union[str, ParcellationTerminologyId]])

slots.ParcellationColorScheme_revision_of = Slot(uri=ANSRS.revision_of, name="ParcellationColorScheme_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.ParcellationColorScheme_revision_of, domain=ParcellationColorScheme, range=Optional[Union[str, ParcellationTerminologyId]])

slots.AnatomicalAnnotationSet_revision_of = Slot(uri=ANSRS.revision_of, name="AnatomicalAnnotationSet_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.AnatomicalAnnotationSet_revision_of, domain=AnatomicalAnnotationSet, range=Optional[Union[str, ParcellationTerminologyId]])

slots.ParcellationAtlas_revision_of = Slot(uri=ANSRS.revision_of, name="ParcellationAtlas_revision_of", curie=ANSRS.curie('revision_of'),
                   model_uri=ANSRS.ParcellationAtlas_revision_of, domain=ParcellationAtlas, range=Optional[Union[str, AnatomicalSpaceId]])